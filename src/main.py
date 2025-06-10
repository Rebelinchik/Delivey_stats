from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def buil(self):
        return Label(text="Привет, Андроид!")

if __name__=="__main__":
    MyApp().run()


