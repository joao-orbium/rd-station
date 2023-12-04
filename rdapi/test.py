# import requests



# url = f"https://crm.rdstation.com/api/v1/deals?token={token}"

# headers = {"accept":"application/json"}

# res = requests.get(url, headers=headers)

# print(res.text)

from negotiations import Negotiations, NegotiationParser

token = "651c7575ba3ed8001684faab"

n = Negotiations("https://crm.rdstation.com/api/v1/deals", token)
np = NegotiationParser(n)
data = np.parse_all_deals()
print(data)