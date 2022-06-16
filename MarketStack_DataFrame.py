import pandas as pd 

import requests
api_key="1cb8590dbf8618996e80b44c533047a1"
params = {
  'access_key': "YOUR_ACCESS_KEY"
}


params['access_key']=api_key

#api_result = requests.get('http://api.marketstack.com/v1/tickers/appl/eod',params)

api_result = requests.get('http://api.marketstack.com/v1/tickers/RELIANCE.XNSE/eod',params)


api_response = api_result.json()


new_df = pd.DataFrame.from_dict(api_response["data"]["eod"])
df2 = pd.DataFrame().assign(open=new_df['open'], high=new_df['high'],low=new_df['low'],close=new_df['close'],volume=new_df['volume'],date=new_df['date'])
df2