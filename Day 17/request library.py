
# import requests

# url = "https://markets.onlinekhabar.com/smtm/home/trending"

# r = requests.get(url=url)
# if r.status_code == 200:
#     data = r.json()['response']
#     for i in data:
#         print(i['ticker'], i['ticker_name'])
# else:
#     print("Request failed with status code:", r.status_code)



# import requests

# url = "https://markets.onlinekhabar.com/smtm/home/most-searched-stocks"

# r = requests.get(url=url)
# if r.status_code == 200:
#     data = r.json()['response']

#     for i in data:
#         print(i['ticker'], i['no_of_hits'],i['pointChange'],i['ltp'])
# else:
#     print("Request failed with status code:", r.status_code)



import requests

url = "https://markets.onlinekhabar.com/smtm/home/gainers-losers/Microfinance"
r = requests.get(url=url)
if r.status_code == 200:
    data = r.json()
    print(type(data))
    print(data.keys())
    data1 = data['response']
    print(type(data1))
    print(data1.keys())
    top_gainer = data1['topGainer']
    print(type(top_gainer))
    print(top_gainer['ticker_name'], top_gainer['ltp'])

    # top loser
    topLoser = data1['topLoser']
    print(type(topLoser))
    print(topLoser['ticker_name'], topLoser['ltp'])



else:
    print("Fail")