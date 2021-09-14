import tweepy
import os
import js2py
from datetime import date

# temp keys
keys= {}
keys['CONSUMER_KEY']=         "pGBDoAaEpkliVKBOLwjtcmHGc"
keys['CONSUMER_SECRET']=      "xF3g1wrP50b6BlZEd20u4oVfjgH1FGQcuWUzlQO5aUWOufvlhw"
keys['ACCESS_TOKEN']=         "622518493-6VcLIPprbQbv9wkcBBPvCle8vsjU9fE85Dq9oStl"
keys['ACCESS_TOKEN_SECRET']=  "tH9aKQbQQ1iRdYTcLSsPwitl44BkAc6jilrsU0ifnXvZhq"

# Get Computer EVN or device infomation
# IF you more decribe your system info, check the example blow a link.
# https://stackoverflow.com/questions/3103178/how-to-get-the-system-info-with-python
def getSystemInfomation():
  return f"{os.uname()}"

def connectChecker(api):
  try:
      api.verify_credentials()
      print("Authentication OK")
  except:
      print("Error during authentication")

# Firefox 
def getURL():
  get_url_js= 'document.URL'
  return js2py.eval_js(get_url_js)

def extracer(url):
    get_title_js= 'document.getElementsByTagName("h1")[0].textContent'
    return str.strip(js2py.eval_js(get_title_js))

# Get URL from NEW documentation.
def uploadURL():
  URL= getURL()
  title= extracer(URL)

  if(URL in "google.com/search" or URL in "duckduckgo.com" or URL in "yandex.com/search"):
    return 0
  elif (URL in "youtube.com/watch?v=dQw4w9WgXcQ&t=113s"):
    return -1
  else:
    api.update_status(f"{title}  ::\n{URL}")
    print("Post IT")

# Init
# Authenticate to Twitter
auth = tweepy.OAuthHandler(keys.get('CONSUMER_KEY'), keys.get('CONSUMER_SECRET'))
auth.set_access_token(keys.get('ACCESS_TOKEN'), keys.get('ACCESS_TOKEN_SECRET'))

api = tweepy.API(auth)

# Connect Test
connectChecker(api)

# Create a tweet, onece POST IT.
data_obj = getSystemInfomation()
d1 =  date.today().strftime("%d/%m/%Y")
api.update_status(f"#おはようございます {d1} via @youtube \n{data_obj} \nhttps://youtu.be/ac58ARaacAM")

while(1):
  if(uploadURL() == -1):
    break


# Reference
#   https://realpython.com/twitter-bot-python-tweepy/
#   https://twitterdev.github.io/search-tweets-python/
