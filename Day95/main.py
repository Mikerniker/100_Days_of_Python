
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window



class Alien(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class Spaceship(Widget):    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        if self._keyboard:
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)
        self.moving_left = False
        self.moving_right = False
      

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard = None


    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.moving_left = True
        elif keycode[1] == 'right':
            self.moving_right = True

    def on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'left':
            self.moving_left = False
        elif keycode[1] == 'right':
            self.moving_right = False

    def update(self):
        if self.moving_left and self.x > 0:
            self.x -= 5
        if self.moving_right and self.right < self.parent.width:
            self.x += 5

    def fire_bullet(self):
        bullet = Bullet()
        bullet.size = (10, 20)  # Set bullet size


class SpaceGame(Widget):
    player = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.aliens = []
        self.alien_velocity_x = -2
        Clock.schedule_once(self.create_aliens)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def create_aliens(self, *args):
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
        self.player.update()

        for alien in self.aliens:
            alien.x += self.alien_velocity_x

        if any(alien.x < 0 for alien in self.aliens):
            self.alien_velocity_x *= -1
            self.lower_aliens()
        elif any(alien.right > self.width for alien in self.aliens):
            self.alien_velocity_x *= -1
            self.lower_aliens()    

   # continue here
    
    def lower_aliens(self):
        """Drops all aliens down when they change horizontal direction."""
        for alien in self.aliens:
            alien.y -= 20 

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        pass
    
    def update_movement(self, dt):
        if self.moving_left:
            self.player.center_x = max(self.player.center_x - 5, self.player.width / 2)
        if self.moving_right:
            self.player.center_x = min(self.player.center_x + 5, self.width - self.player.width / 2)


class Bullet(Widget):
    speed = NumericProperty(5)

    def move(self):
        self.y += self.speed

class SpaceApp(App):
    def build(self):
        return SpaceGame()
    
if __name__ == '__main__':
    SpaceApp().run()

    
# import time
# from turtle import Screen


# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)