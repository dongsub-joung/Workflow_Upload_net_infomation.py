import tweepy
import os
frome datetime import date


def connectTest(apis):
  try:
    apis.verify_credentials()
    print("Authentication OK")
    return 1
  except:
    return 0

Keys= {}
Keys=['CONSUMER_KEY']=        "temp"
Keys=['CONSUMER_SECRET']=     "temp"
Keys=['ACCESS_TOKEN']=        "temp"
Keys=['ACCESS_TOKEN_SECRET']= "temp"

SeaOfJapan= "https://www.youtube.com/watch?v=-SMgI6S7YaY"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(Keys.'CONSUMER_KEY', Keys.'CONSUMER_SECRET')
auth.set_access_token(Keys.'ACCESS_TOKEN', Keys.'ACCESS_TOKEN_SECRET')

# Create API object
api = tweepy.API(auth)
d1= today.strftime("%d%m%Y")
os_info= os.uname()

# Create a tweet when your's day started.
connectTest(api) : api.update_status(f"#おはようございます \nTODAY: {d1} \n{os_info} \n@youtube \n{SeaOfJapan}") ? print("Error during authentication")
