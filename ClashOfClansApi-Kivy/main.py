import urllib
import json
import pandas as pd
from kivy.uix.button import Button
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.widget import Widget

api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijk5NjlhNjM1LTI5YTYtNGYyZS1iOTYxLWQ1YTUwN2NkZmY5MCIsImlhdCI6MTYxMDY1MzUxMSwic3ViIjoiZGV2ZWxvcGVyLzU5MWU5MTYzLWRjMTMtMGQ3Ny01YTNkLWIxYmQ4NmM1YzY2ZCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE5MS4zNi4xNDkuNjEiXSwidHlwZSI6ImNsaWVudCJ9XX0.tGUkB7lRBoqSUP7Ok21nsHpo-eCIq-IKAxN6SSU6jsoNmMn_k58SRUX2xTPH-PnkM0QsrnVic_KjNx_9StKwIg"

class Api(object):

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
    
    def clan_members_for(self,tag):
        return self.get('/clans/%23' + tag + '/members')

class ClashApp(App):

    def chamarApi(self):
        client = Api(api_token)
        data = client.clan_members_for("U99PGPV")

    button = Button(text='Hello-World',font_size=14)
    button.bind(on_press=chamarApi)

    def build(self):
        return self.button
        

if __name__ == '__main__':
    ClashApp().run()