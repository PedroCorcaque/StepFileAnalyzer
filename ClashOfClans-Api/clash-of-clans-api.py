import urllib
import json
import pandas as pd 
import numpy as np 

class Barcher(object):

    def __init__(self,token):
        import requests
        self.requests = requests
        self.token = token
        self.api_endpoint = "https://api.clashofclans.com/v1"
        self.timeout = 30
    
    def get(self,url,params=None):
        headers = {
            'Accept':"application/json",
            'Authorization':"Bearer " + self.token 
        }

        url = self.api_endpoint + url

        try:
            response = self.requests.get(url,params=params,headers=headers,timeout=30)
            return response.json()
        except:
            if 400 <= response.status_code <= 599:
                return "Error {}".format(response.status_code)
    
    def find_clan(self,tag):
        return self.get('/clans/%23')
    
    def clan_members_for(self,tag):
        return self.get('/clans/%23' + tag + '/members')

    def current_war(self,tag):
        return self.get('/clans/%23' + tag + '/currentwar')
    
    def warlog(self,tag):
        return self.get('/clans/%23' + tag + '/warlog')
    
    def locations(self):
        return self.get('/locations')

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijk5NjlhNjM1LTI5YTYtNGYyZS1iOTYxLWQ1YTUwN2NkZmY5MCIsImlhdCI6MTYxMDY1MzUxMSwic3ViIjoiZGV2ZWxvcGVyLzU5MWU5MTYzLWRjMTMtMGQ3Ny01YTNkLWIxYmQ4NmM1YzY2ZCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE5MS4zNi4xNDkuNjEiXSwidHlwZSI6ImNsaWVudCJ9XX0.tGUkB7lRBoqSUP7Ok21nsHpo-eCIq-IKAxN6SSU6jsoNmMn_k58SRUX2xTPH-PnkM0QsrnVic_KjNx_9StKwIg"
client = Barcher(token)
data = client.clan_members_for("U99PGPV")

df = pd.DataFrame(data['items'])

for i in df.index:
    # print(df.loc[[i],['name','donations','donationsReceived']].values)
    print(df.loc[[i],['name']].values,end="\t\t")
    print(df.loc[[i],['donations']].values,end="\t\t")
    print(df.loc[[i],['donationsReceived']].values)
df.to_excel('Teste.xlsx',sheet_name='Doaçoes')