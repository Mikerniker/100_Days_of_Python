
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

class SpaceGame(Widget):
    player = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.aliens = []
        self.moving_left = False
        self.moving_right = False
        self.alien_velocity_x = -2  # Negative for leftward movement
        Clock.schedule_once(self.create_aliens)
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)
   
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
        
        # Check if any alien hits the left or right edge
        if any(alien.x < 0 for alien in self.aliens):
            self.alien_velocity_x *= -1  # Change direction to right
            self.lower_aliens()  # Drop aliens down when changing direction
        elif any(alien.right > self.width for alien in self.aliens):
            self.alien_velocity_x *= -1  # Change direction to left
            self.lower_aliens()
    
    def lower_aliens(self):
        """Drops all aliens down when they change horizontal direction."""
        for alien in self.aliens:
            alien.y -= 20 


class SpaceApp(App):
    def build(self):
        return SpaceGame()
    
class Alien(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


if __name__ == '__main__':
    SpaceApp().run()

    
# import time
# from turtle import Screen


# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)