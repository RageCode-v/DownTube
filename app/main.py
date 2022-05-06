from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.toast import toast

from os import environ
from certifi import where
from threading import Thread

from logic import *

environ['SSL_CERT_FILE'] = where()
pamg = './data/image.png'
path = down_path()
colors = load_colors()


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

    def reset(self):
        self.ids.direct.text = ''
        self.ids.direct.reset_undo()
        self.ids.tumb.source = pamg
        self.ids.vitle.text = 'Video title'
        del self.obvid
        checks = MDToggleButton.get_widgets('downs')
        for w in checks:
            if w.state == 'down':
                w.state = 'normal'
        del checks

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

    def down(self):
        op = None
        checking = MDToggleButton.get_widgets('downs')
        for w in checking:
            if w.state == 'down':
                op = w.text
                break
            else:
                op = None
        del checking
        if op is not None:
            try:
                if self.obvid.title == '':
                    toast('Nome vazio, usando título original')
                else:
                    toast('Download iniciado')
                self.obvid.title = self.ids.vitle.text
                Thread(target=self.obvid.down_this, args=(path, op)).start()
            except AttributeError:
                pass
            except Exception as erro:
                print(erro)
            else:
                self.reset()
        else:
            toast('Selecione uma opção acima!')

    def msgver(self):
        if self.ids.vitle.text.strip() == '':
            self.ids.vitle.error = True
        else:
            self.ids.vitle.error = False


class Main(MDApp):
    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.accent_palette = 'DeepOrange'
        self.theme_cls.theme_style = 'Dark'
        return Prince()


Main().run()
