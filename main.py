import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

player = {
    'score': 0,
    'power': 1
}



def read_data():
    global player
    try:
        with open("play.json","s",encoding="utf-8") as file:
            player = json.load(file)
    except:
        print("невдача")


def save_data():
    global player
    try:
        with open("play.json","w",encoding="utf-8") as file:
            json.dump(player,file, indent=4, ensure_ascii=True)
    except:
        print("невдача")
save_data()

class MainScreen (Screen):

    def _init__(self, **kw):
        super()._init__(**kw)

    def lick(self):
        self.ids.ball.size_hint = (1,1)
        self.ids.ball.pos_hint = {"center_x": 0.5,'top':1}

    def jtnoc(self):
        self.ids.ball.size_hint = (3,3)
        self.ids.ball.pos_hint = {"center_x": 0.5,'top':1.8}

    def gcli(self):

        self.manager.current = "first"

class FirstScreen(Screen):

    def _init__(self, **kw):

        super()._init__(**kw)

def click(self):

    self.manager.current = "main"

class ClickerApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FirstScreen(name = 'first'))

        return sm

app = ClickerApp()

app.run()