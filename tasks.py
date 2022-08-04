import string
import requests
import threading as th  
import datetime
import random
import tweepy
import re
import csv


# convert current date into timestamp
# defining a params dict for the parameters to be sent to the API
########################################## post tweet ############################################

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
 

########################################## Main API handling ############################################
timestamp = []
hash = []
timer = 0
def transfer(secs):
    URL = "https://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE&page=1&offset=4000&startblock=0&sort=desc&apikey=XYS1Z1DTCPUHEDHCNG8BSBSCHCTYRKNYDC"
    r = requests.get(url = URL)
    data = r.json()
    # print(len(data['result']))
    def time_duration():
        

        # times = datetime.datetime.fromtimestamp(int(data['result'][0]['timeStamp']))
        now = datetime.datetime.now()
        before = datetime.datetime.now() - datetime.timedelta(seconds=secs)

        # print(now)
        # print(before)


        mins = now.strftime("%H:%M:%S")

        t1 = datetime.datetime.strptime(mins,'%H:%M:%S')
        nowft = (t1.second + t1.minute*60 + t1.hour*3600)


        befmin = before.strftime("%H:%M:%S")
        t2 = datetime.datetime.strptime(befmin,'%H:%M:%S') 

        beft = (t2.second + t2.minute*60 + t2.hour*3600)

        newtime = nowft - secs
        # print("now : ",nowft)
        # print("before : ",newtime)
        # sec = newtime.total_seconds()



       
        
        try :
            for i in range(len(data['result'])):
                times = datetime.datetime.fromtimestamp(int(data['result'][i]['timeStamp']))
                deadadd = data['result'][i]['to']
                # print(deadadd)
            # timenow = datetime.timedelta(hours=1)
                mins = times.strftime("%H:%M:%S")

                pt = datetime.datetime.strptime(mins,'%H:%M:%S')
                todayt = datetime.datetime.strptime(str(datetime.datetime.today()),'%Y-%m-%d %H:%M:%S.%f')


                
                
                mins2 = times.strftime("%H:%M:%S")

                pt2 = datetime.datetime.strptime(mins2,'%H:%M:%S')
                todayt2 = datetime.datetime.strptime(str(datetime.datetime.today()),'%Y-%m-%d %H:%M:%S.%f')

                todayts = (str(todayt.year)+"-0" + str(todayt.month)+"-0"+ str(todayt.day))
        
                time1 = (pt.second + pt.minute*60 + pt.hour*3600)
                time2 = (pt2.second + pt2.minute*60 + pt2.hour*3600) - 3600

                # minti = (int(time1) - int(time2))

                if re.findall("^0xdead", deadadd):
                    # print(time1)
                    if (time1 >= newtime and time1 <= nowft)and(str(times.date())==str(todayt.date())):
                        timestamp.append(int(data['result'][i]['value']))
                        hash.append(data['result'][i]['hash'])
                        print("value going in ... !!!",int(data['result'][i]['value']))
                        # print("hash going in ... !!!",data['result'][i]['hash'])
                        
        except:
            print("Something went wrong...!!! ")
     
   





    time_duration()

       
        


                    












################### NEWS ############################################



##################################### FIND MAX VALUE TO TWEET ##################################

def hourly_burn():
    ran = random.randrange(3600, 7200)
    th.Timer(ran, hourly_burn).start()
    transfer(84000)  
    try : 
        if timestamp != []:
            maxs = max(timestamp)
            ind = timestamp.index(maxs)
            strmax = str(maxs)[:-18]
            com = "{:,}".format(int(strmax))

            hashxt = hash[ind]
            url = "https://etherscan.io/tx/"+hashxt
            stat = "Burn Alert : {} $SHIB -> transferred to dead wallet. \n{}".format(com,url)
            # print(stat)
            if int(strmax) >= 10000000:
                print(stat) 
                # tweet(stat)
            else:
                print("trasantion is smaller than 10000000")
            # print(stat)
        else:
            print("No transfer to Dead wallet in past 2 hours")
#           

    except:
        print("Something went wrong...!!! ")
    
##################################### NEWS ALERT ##################################

def news_tweet():
    th.Timer(43200, news_tweet).start()  
    now = datetime.datetime.now() 
  
    before = now - datetime.timedelta(hours= 24)
    t1 = before.strftime('%Y%m%dT%H%M')

    URL = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=CRYPTO:SHIB&topics=blockchain&apikey=GZUTMI1E03YRDOQG&sort=LATEST&time_from={}&limit=10".format(t1)
    r = requests.get(url = URL)
    print(URL)

    data = r.json()
    try :

        headline = data['feed'][0]['title']
        summary = data['feed'][0]['summary']
        newsurl = data['feed'][0]['url']
    

        
        news = "Headlines : \n"+headline+"\n" "\nRead More 👇🏻:"+newsurl+"\n"
        print(news)
        # tweet(news)
    except:
        print("News API is not working properly")

      
##################################### FIND MAX VALUE OF 24 HOUR TO TWEET ##################################

def day_burn():
    th.Timer(86400, day_burn).start()  
    URL = "https://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE&page=1&offset=5000&startblock=0&sort=desc&apikey=XYS1Z1DTCPUHEDHCNG8BSBSCHCTYRKNYDC"
    r = requests.get(url = URL)
    data = r.json()

    
  
    val = []
    hash1 = []

    try:
        for i in range(len(data['result'])):
            # print(i+1)
            times = datetime.datetime.fromtimestamp(int(data['result'][i]['timeStamp']))
        
       


            todayt = datetime.datetime.strptime(str(datetime.datetime.today()),'%Y-%m-%d %H:%M:%S.%f')

         
            deadadd = data['result'][i]['to']
            if re.findall("^0xdead", deadadd):
                if (str(times.date())==str(todayt.date())):
                    asd = data['result'][i]['value'][:-18]
                    # print(a)
                    if asd != "":
                        b = int(asd)
                        val.append(b)

                        hash1.append(data['result'][i]['hash'])





        sums = sum(val)    

        print(sums)
    
        com = "{:,}".format(sums)
        total = "Burn Alert : In the past 24 hours, there have been more than of {} $SHIB tokens burned  #shibarmy".format(com)
        print(total)
        print(val)
     
        
                    
            
        # tweet(total)
                    # return total 


                
                

    except:
            print("API give errors..!!!")



def whale():
    th.Timer(3500, whale).start()  
    URL = "https://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE&page=1&offset=5000&startblock=0&sort=desc&apikey=XYS1Z1DTCPUHEDHCNG8BSBSCHCTYRKNYDC"
    r = requests.get(url = URL)
    data = r.json()
    now = datetime.datetime.now()
    before = datetime.datetime.now() - datetime.timedelta(seconds=3600)

    # print(now)
    # print(before)


    mins = now.strftime("%H:%M:%S")

    t1 = datetime.datetime.strptime(mins,'%H:%M:%S')
    nowft = (t1.second + t1.minute*60 + t1.hour*3600)


    befmin = before.strftime("%H:%M:%S")
    t2 = datetime.datetime.strptime(befmin,'%H:%M:%S') 

    beft = (t2.second + t2.minute*60 + t2.hour*3600)

    newtime = nowft - 3600

    
  
    val = []
    hash1 = []

    try:  
        for i in range(len(data['result'])):
            # print(i+1)
            times = datetime.datetime.fromtimestamp(int(data['result'][i]['timeStamp']))
        
        
            mins = times.strftime("%H:%M:%S")
            pt = datetime.datetime.strptime(mins,'%H:%M:%S')
            todayt = datetime.datetime.strptime(str(datetime.datetime.today()),'%Y-%m-%d %H:%M:%S.%f')

            
            
            time1 = (pt.second + pt.minute*60 + pt.hour*3600)
            if (time1 >= newtime and time1 <= nowft)and(str(times.date())==str(todayt.date())):
                asd = data['result'][i]['value'][:-18]
                # print(a)
                if asd != "":
                    b = int(asd)
                    val.append(b)

                    hash1.append(data['result'][i]['hash'])





        sums = max(val)    

        print(sums)
        ind = val.index(sums)
        com = "{:,}".format(sums)
        
        hashxt = hash1[ind]
        if sums > 100000000:
            url = "https://etherscan.io/tx/"+hashxt
            total = "Whale Alert : $SHIB   {}  transferred. \ncheck details 👇🏻 \n{}".format(com,url)
            # tweet(total)
            print(total)
        else:
            print("No Whale alert in lsat hour")
         
        
            
                        
       


                
                

    except:
            print("API give errors..!!!")



    
hourly_burn()


whale()

news_tweet()

day_burn()


print("suceess...!!!")






