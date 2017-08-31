import urllib.request, json

print('League Software')


API_KEY = 'RGAPI-2d0ab476-0501-4bd1-8dae-6a2b0e9ed8ad'

def summonerRequest(summName,region):
    myurl = 'https://' + region + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summName + '?api_key=' + API_KEY
    jsonData = openJSON(myurl)
    return jsonData

def getRecentGames(id,region):
    myurl = 'https://' + region + '.api.riotgames.com/lol/match/v3/matchlists/by-account/' + str(id) + '?api_key=' + API_KEY
    jsonData = openJSON(myurl)
    return jsonData

def openJSON(myurl):
    response = urllib.request.urlopen(myurl)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw.decode('utf-8'))
    return jsonData

def getSummonerId(summ):
    id = summ['accountId']
    return id

def getMatchFromId(id):
    myurl = 'https://' + region + '.api.riotgames.com/lol/match/v3/matches/' + str(id) + '?api_key=' + API_KEY
    jsonData = openJSON(myurl)
    return jsonData

def printMostRecentGame(recent):
    mostRecentId = recent['matches'][0]['gameId']
    match = getMatchFromId(mostRecentId)
    print(match['seasonId'])


summonerName = "shinameega" #Have this or the inputs commented out for quick testing or variety testing between accounts.
region = "euw1"

#summonerName = input("What is the summoner name?\n\n")
#region = input("What is the region?\n\n")

summoner = summonerRequest(summonerName,region)
id = getSummonerId(summoner)
recent = getRecentGames(id,region)
printMostRecentGame(recent)