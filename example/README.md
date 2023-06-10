### Testing the API

You can then try to do a GET to http://localhost:12000/api/private which will throw an error if you don't send an access token signed with RS256 with the appropriate issuer and audience in the Authorization header.