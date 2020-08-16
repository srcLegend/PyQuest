import json, requests

with open("data/tokens.json") as f:
	x = json.load(f)

print(x['access_token'])
print(x['api_server'])
print(x['expires_in'])
print(x['refresh_token'])
print(x['token_type'])

#parameters = {"refresh_token": "Or87AaL4FDF6jhAqw8SsIf0T_i47lD-r0"}
#url = "https://login.questrade.com/oauth2/token?grant_type=refresh_token"
#r = requests.get(url, parameters)

#print(r.text)
