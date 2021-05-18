
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty





class app(GridLayout):
    name = ObjectProperty(None)
    age=ObjectProperty(None)

    def on_click(self):
        print("my name is {}  and i am {} yeras old".format(self.name.text,self.age.text))
        self.name.text=""
        self.age.text=""




class Myfirstapp(App):
    def build(self):
        return app()

Myfirstapp().run()