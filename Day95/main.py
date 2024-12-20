
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock

class SpaceGame(Widget):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.aliens = []
        self.alien_velocity_x = -2  # Negative for leftward movement
        Clock.schedule_once(self.create_aliens)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def create_aliens(self):
        self.clear_widgets()
        alien_width = 35 
        alien_height = 35  # Height of each alien
        spacing = 10  # Space between aliens
        total_width = 8 * alien_width + 7 * spacing
        start_x = (self.width - total_width) / 2  # Center horizontally
        start_y = self.height / 2 + alien_height

        for row in range(3):  # 3 rows
            for col in range(8):  # 8 aliens per row
                alien = Alien()
                x = start_x + col * (alien_width + spacing)
                y = start_y + row * (alien_height + spacing)
                alien.pos = (x, y)
                self.add_widget(alien)
                self.aliens.append(alien)

    def update(self, dt):
        # Move all aliens left
        for alien in self.aliens:
            alien.x += self.alien_velocity_x

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