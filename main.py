import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel

class ViewScreenManager(ScreenManager):
    pass

class MainMenu(Screen):
    config = ObjectProperty(None)

    def clicou(self):
        print("Voce clicou no botao " + self.config.text)



class NewGame(Screen):
    pass


class MenuButton(ButtonBehavior, Label):
    cor = ListProperty(get_color_from_hex('#D0D0D0'))
    cor_press = ListProperty(get_color_from_hex('#6d6b71'))

    def __init__(self, **kwargs):
        super(MenuButton, self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def on_press(self, *args):
        self.cor, self.cor_press = self.cor_press, self.cor

    def on_release(self, *args):
        self.cor, self.cor_press = self.cor_press, self.cor

    def on_cor(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height, self.height),
                    pos=self.pos)
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width-self.height, self.y))
            Rectangle(size=(self.width-self.height, self.height),
                      pos=(self.x+self.height/2.0, self.y))

class ViewApp(App):
    def build(self):
        return ViewScreenManager()

if __name__ == '__main__':
    ViewApp().run()



