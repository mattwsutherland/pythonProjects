'''
https://centipedenation.com/transmissions/bombshell-anon-crunches-voter-data-discovers-election-software-dominion-producing-massive-fraud/

to check how many votes were switched from Trump to Biden in a state, you then type findfraud(‘Hawaii’) for example, replace Hawaii with the name of the file of the state you want to check, the file for new hampshire is named newhamp for example, so findfraud(‘newhamp’), to check the total lost votes (For both candidates) do lostvotes(‘newhamp’) for example.
'''



import json



def findfraud(NAME):
    with open(NAME + '.json', encoding="utf8") as f:
        x = json.load(f)
    TotalVotesLost = 0
    for i in range(len(x["data"]["races"][0]["timeseries"])):
        if i != 0 and x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] < x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"]:
            if x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["bidenj"] > x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["bidenj"]:
                print ("Index : " + str(i) + " Past Index : " + str(i-1))
                print (x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] - x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"])
                TotalVotesLost += x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] - x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"]
    print (str(str(TotalVotesLost)  + " Flo"))

def findfraud2(NAME):
    with open(NAME + '.json', encoding="utf8") as f:
        x = json.load(f)
    TotalVotesLost = 0
    for i in range(len(x["data"]["races"][0]["timeseries"])):
        if i != 0 and x["data"]["races"][0]["timeseries"][i]["votes"] < x["data"]["races"][0]["timeseries"][i-1]["votes"]:
            TotalVotesLost += x["data"]["races"][0]["timeseries"][i]["votes"] - x["data"]["races"][0]["timeseries"][i-1]["votes"]
    print (TotalVotesLost)

print(findfraud('newyork'))