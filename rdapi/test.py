# import requests



# url = f"https://crm.rdstation.com/api/v1/deals?token={token}"

# headers = {"accept":"application/json"}

# res = requests.get(url, headers=headers)

# print(res.text)

from negotiations import Negotiations

token = "651c7575ba3ed8001684faab"

n = Negotiations("https://crm.rdstation.com/api/v1/deals", token)
abc = n.list_all()
print(abc)