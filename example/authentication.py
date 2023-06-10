"""Python Flask API Auth0 integration example
"""

from functools import wraps
import json
from os import environ as env
from typing import Dict

from six.moves.urllib.request import urlopen

from flask import Flask, request, jsonify, Response
from flask_cors import cross_origin
from jose import jwt

HOST = "localhost:7400"
ALGORITHMS = ["RS256"]
JWKS_URL = "http://" + HOST + "/.well-known/jwks.json"
APP = Flask(__name__)

# Format error response and append status code.
class AuthError(Exception):
    """
    An AuthError is raised whenever the authentication failed.
    """
    def __init__(self, error: Dict[str, str], status_code: int):
        super().__init__()
        self.error = error
        self.status_code = status_code


@APP.errorhandler(AuthError)
def handle_auth_error(ex: AuthError) -> Response:
    """
    serializes the given AuthError as json and sets the response status code accordingly.
    :param ex: an auth error
    :return: json serialized ex response
    """
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


def get_token_auth_header() -> str:
    """
    Obtains the access token from either the user token or the Authorization Header
    """
    user_token = request.headers.get("x-user-token", None)
    auth = request.headers.get("authorization", None)
    if auth:
        parts = auth.split()
        if parts[0].lower() != "bearer":
            raise AuthError({"code": "invalid_header",
                            "description": "Authorization header must start with Bearer"}, 401)
        elif len(parts) == 1:
            raise AuthError({"code": "invalid_header",
                            "description": "Token not found"}, 401)
        elif len(parts) > 2:
            raise AuthError({"code": "invalid_header",
                            "description": "Authorization header must be Bearer token"}, 401)
        user_token = parts[1]
    if not user_token:
        raise AuthError({"code": "authorization_header_missing",
                        "description": "Authorization header is expected"}, 401)
    return user_token

def requires_auth(func):
    """
    Determines if the access token is valid
    """
    
    @wraps(func)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        # fetching jwks, ideally this should be cached for a period of time
        jsonurl = urlopen(JWKS_URL)
        jwks = json.loads(jsonurl.read())
        try:
            unverified_header = jwt.get_unverified_header(token)
        except jwt.JWTError as jwt_error:
            raise AuthError({"code": "invalid_header",
                            "description": "Invalid header. Unsupported JWT"}, 401) from jwt_error
        if unverified_header["alg"] not in ALGORITHMS:
            raise AuthError({"code": "invalid_header",
                             "description": "Invalid header. Unsupported JWT Algo"}, 401)
        # find key that matches kid
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                _ = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                )
            except jwt.ExpiredSignatureError as expired_sign_error:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401) from expired_sign_error
            except jwt.JWTClaimsError as jwt_claims_error:
                raise AuthError({"code": "invalid_claims",
                                "description":
                                    "incorrect claims, please check the audience and issuer"}, 401) from jwt_claims_error
            except Exception as exc:
                raise AuthError({"code": "invalid_header",
                                "description":
                                    "Unable to parse authentication token."}, 401) from exc
            return func(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                         "description": "Unable to find appropriate key"}, 401)

    return decorated


# Controllers API
@APP.route("/api/public")
@cross_origin(headers=["Content-Type", "Authorization", "X-User-Token"])
def public():
    """
    No access token required to access this route
    """
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return jsonify(message=response)


@APP.route("/api/private")
@cross_origin(headers=["Content-Type", "Authorization", "X-User-Token"])
@cross_origin(headers=["Access-Control-Allow-Origin", "http://localhost:12000"])
@requires_auth
def private():
    """
    A valid access token is required to access this route
    """
    response = "Hello from a private endpoint! You need to be authenticated to see this."
    return jsonify(message=response)


if __name__ == "__main__":
    print("Starting server with endpoints ""/api/public"" and ""/api/private""")
    APP.run(host="0.0.0.0", port=env.get("PORT", 12000))