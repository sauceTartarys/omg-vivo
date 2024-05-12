from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def click(self):
        self.ids.ball.size_hint = (1,1)


    def clicktw(self):
        self.ids.ball.size_hint = (-1,-1)



class MyClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        return sm

app = MyClickerApp()
app.run()