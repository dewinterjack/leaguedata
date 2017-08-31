import urllib.request, json

season = {0:'PRESEASON3', 1:'SEASON3', 2:'PRESEASON2014', 3:'SEASON2014', 4: 'PRESEASON2015', 5: 'SEASON2015', 6: 'PRESEASON2016', 7: 'SEASON2016', 8: 'PRESEASON2017', 9: 'SEASON2017'}

print('League Software\n')

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
    response.headers
    jsonData = json.loads(jsonRaw.decode('utf-8'))
    return jsonData

def getSummonerId(summ):
    id = summ['id']
    return id

def getAccountId(summ):
    id = summ['accountId']
    return id

def getMatchFromId(id):
    myurl = 'https://' + region + '.api.riotgames.com/lol/match/v3/matches/' + str(id) + '?api_key=' + API_KEY
    jsonData = openJSON(myurl)
    return jsonData

def getChampionName(id):
    myurl = 'https://' + region + '.api.riotgames.com/lol/static-data/v3/champions/' + str(id) + '?api_key=' + API_KEY
    champion = openJSON(myurl)
    return champion['name']

def printMostRecentGame(recent,summonerName): #Need the id for getting only that players stats.
    mostRecentId = recent['matches'][0]['gameId']
    match = getMatchFromId(mostRecentId)
    for player in match['participantIdentities']:
        if(player['player']['summonerName'] == summonerName):
            participantId = player['participantId']
            for participant in match['participants']:
                if(participantId == participant['participantId']):
                    champion = getChampionName(participant['championId'])
                    print("Champion: " + champion + '\n')
                    print("Kills: " + str(participant['stats']['kills']))
                    print("Deaths: " + str(participant['stats']['deaths']))
                    print("Assists: " + str(participant['stats']['assists']))
                    print("Wards: " + str(participant['stats']['wardsPlaced']))
                    print()


def printLeagueDetails(region,id,name):
    myurl = 'https://' + region + '.api.riotgames.com/lol/league/v3/leagues/by-summoner/' + str(id) + '?api_key=' + API_KEY
    league = openJSON(myurl)
    print(league[0]['queue'] + ':\n')
    print(league[0]['tier'])
    for player in league[0]['entries']:
        if(player['playerOrTeamName'] == name):
            print(player['rank'])
            print(str(player['leaguePoints']) + 'LP\n')
    print(league[1]['queue'] + ':\n')
    print(league[1]['tier'])
    for player in league[1]['entries']:
        if(player['playerOrTeamName'] == name):
            print(player['rank'])
            print(str(player['leaguePoints']) + 'LP\n')

summonerName = "shinameega" #Have this or the inputs commented out for quick testing or variety testing between accounts.
region = "euw1"

#summonerName = input("What is the summoner name?\n\n")
#region = input("What is the region?\n\n")

summoner = summonerRequest(summonerName,region)
accountId = getAccountId(summoner)
id = getSummonerId(summoner)
recent = getRecentGames(accountId,region)
printMostRecentGame(recent,summonerName)
printLeagueDetails(region,id,summonerName)