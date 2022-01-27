import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
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
    # config = ObjectProperty(None)
    # def clicou(self):
    #     print("Voce clicou no botao " + self.config.text)
    pass

class NewGame(Screen):
    pass

# class ToolBar(BoxLayout,AnchorLayout,RelativeLayout):
#     def __init__(self,**Kwargs):
#         super(ToolBar, self).__init__(**Kwargs)
#         anc_layout = AnchorLayout(
#             anchor_x='right', anchor_y='top', size_hint_y= None, size= (600,40))
#         btn = Label(text='Hello World')
#         anc_layout.add_widget(btn)


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



