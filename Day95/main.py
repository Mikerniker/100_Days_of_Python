
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector


class SpaceGame(Widget):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.aliens = []
        self.create_aliens()

   


class SpaceApp(App):
    def build(self):
        return SpaceGame()
    
class Alien(Widget):
    pass



if __name__ == '__main__':
    SpaceApp().run()

    
# import time
# from turtle import Screen


# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)