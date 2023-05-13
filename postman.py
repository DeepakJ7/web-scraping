import json
#import pandas as pd

import requests
url = 'https://www.naukri.com/jobapi/v3/search?noOfResults=40&urlType=search_by_keyword&searchType=adv&keyword=junior%20java%20developer&pageNo=1&k=junior%20java%20developer&nignbevent_src=jobsearchDeskGNB&seoKey=junior-java-developer-jobs&src=jobsearchDesk&latLong='
headers = {'accept-language':'en-GB,en-US;q=0.9,en;q=0.8,kn;q=0.7','appid':'109','systemid':'109'}
print(requests.get(url,headers=headers))
response = requests.get(url,headers=headers)
print(response.headers.get('content-type'))
resp_dict = response.json()
print(resp_dict)
json_file = json.dumps(resp_dict)
with open("naukri.json","w") as outfile:
    outfile.write(json_file)