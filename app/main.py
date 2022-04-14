from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton

from os import environ

from certifi import where

from threading import Thread

from logic import *

environ['SSL_CERT_FILE'] = where()
pamg = './data/image.png'
path = down_path()
colors = {
    'DeepOrange': {
        '50': 'FBE9E7',
        '100': 'FFCCBC',
        '200': 'FFAB91',
        '300': 'FF8A65',
        '400': 'FF7043',
        '500': 'FF5722',
        '600': 'F4511E',
        '700': 'E64A19',
        '800': 'D84315',
        '900': 'BF360C',
        'A100': 'FF9E80',
        'A200': 'FF6E40',
        'A400': 'FF3D00',
        'A700': 'DD2C00'
    },
    'Amber': {
        '50': 'FFF8E1',
        '100': 'FFECB3',
        '200': 'FFE082',
        '300': 'FFD54F',
        '400': 'FFCA28',
        '500': 'FFC107',
        '600': 'FFB300',
        '700': 'FFA000',
        '800': 'FF8F00',
        '900': 'FF6F00',
        'A100': 'FFE57F',
        'A200': 'FFD740',
        'A400': 'FFC400',
        'A700': 'FFAB00'
    },
    'Red': {
        '50': 'FFEBEE',
        '100': 'FFCDD2',
        '200': 'EF9A9A',
        '300': 'E57373',
        '400': 'EF5350',
        '500': 'F44336',
        '600': 'E53935',
        '700': 'D32F2F',
        '800': 'C62828',
        '900': 'B71C1C',
        'A100': 'FF8A80',
        'A200': 'FF5252',
        'A400': 'FF1744',
        'A700': 'D50000'
    },
    'Light': {
        'StatusBar': '000000',
        'AppBar': '212121',
        'Background': '303030',
        'CardsDialogs': '424242'
    },
    'Dark': {
        'StatusBar': '000000',
        'AppBar': '212121',
        'Background': '303030',
        'CardsDialogs': '424242'
    }
}


class TabVid(FloatLayout, MDTabsBase):
    pass


class TabAud(FloatLayout, MDTabsBase):
    pass


class Check(MDRectangleFlatIconButton, MDToggleButton):
    back1 = 'radiobox-blank'
    back2 = 'radiobox-marked'

    def __init__(self, **kwargs):
        super(Check, self).__init__(**kwargs)
        self.line_color = (0, 0, 0, 0)
        self.pos_hint = {'center_x': .5, 'center_y': .5}
        self.icon = self.back1
        self.font_color_normal = (1, 1, 1, 1)

    def on_state(self, widget, value):
        if value == 'down':
            self.icon = self.back2
        else:
            self.icon = self.back1


class Prince(Screen):
    obvid: any
    op: str

    def reset(self):
        self.ids.direct.text = ''
        self.ids.direct.reset_undo()
        self.ids.tumb.source = pamg
        self.ids.vitle.text = 'Video title'
        del self.obvid
        del self.op

    def get(self, url):
        try:
            self.obvid = Order(url)
        except LinkNotFound:
            self.ids.direct.text = ''
            self.ids.tumb.source = pamg
            self.ids.vitle.text = 'Vídeo não encontrado'
        except Exception as erro:
            print(erro)
        else:
            try:
                self.ids.tumb.source = str(self.obvid.tumb)
            except Exception as erro:
                print(erro)
            else:
                self.ids.vitle.text = self.obvid.title

    def select(self, opt: str):
        self.op = opt

    def down_this(self):
        try:
            Thread(target=self.obvid.down_this, args=(path, self.op)).start()
        except AttributeError:
            pass
        except Exception as erro:
            print(erro)
        else:
            self.reset()


class Main(MDApp):
    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.accent_palette = 'DeepOrange'
        self.theme_cls.theme_style = 'Dark'
        return Prince()


Main().run()
