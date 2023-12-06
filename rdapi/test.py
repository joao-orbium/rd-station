# import requests



# url = f"https://crm.rdstation.com/api/v1/deals?token={token}"

# headers = {"accept":"application/json"}

# res = requests.get(url, headers=headers)

# print(res.text)

from negotiations import Negotiations, NegotiationParser
from sheets import Sheets

token = "651c7575ba3ed8001684faab"

n = Negotiations("https://crm.rdstation.com/api/v1/deals", token)
np = NegotiationParser(n)
data = np.parse_all_deals()
sheet = Sheets(data)
# sheet.make_simple_sheet('simple_sheet.xlsx')
sheet.make_revenue_sheet('revenue_sheet.xlsx')