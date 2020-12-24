import requests
import json
from collections import defaultdict
import pandas as pd

url = 'https://hypeauditor.com/api/method/auditor.report'
user =  "YOURID"
token = "YOURTOKEN"
username = ["vancityreynolds", "kevinhart4real", "kobebryant", "supersaf", "taylorswift", "selenagomez", "pepamack"]  #sandbox users

def instagram_audit(username):
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-auth-id': user,
        'x-auth-token': token}

    data = {
      'username': username,
      'v': '2'}

    response = requests.post(url, headers=headers, data=data).json()

    cust_dict = defaultdict(list)

    df = pd.concat({k: pd.DataFrame(v) for k, v in response.items()}, axis=0)

    df.to_excel(f"result_{username}.xlsx")
    
for name in username:
    instagram_audit(name)
