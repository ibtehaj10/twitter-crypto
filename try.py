import tweepy
def tweet(li):
    # # personal details
    consumer_key ="MbGkjnlSnCjjhZrPQkS3BuQFZ"
    consumer_secret ="HciH8GqLTTz0Memw35bLTq2TZ4lQbknXh5TXCihSmPHNKGb5lV"
    access_token ="1455915803585417216-293Fm9XpmwnS1XRz6CzyrxZCsWGlCN"
    access_token_secret ="wr5m9ZzLEzKvbjlTNmt9yzea8ZQXJ7M1hyzeaGOUjgjX5"

    # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # print("URL : \n "+li[1]+" \n News : \n"+li[0])
    api.update_status(status=li)
    # print("success..!!!")

tweet("This is a testing tweet...")
 