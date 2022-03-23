from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.utils import platform
from kivy.metrics import sp
from pytube import *
from pytube.exceptions import RegexMatchError
from os.path import dirname, join
from os import remove
from PIL import Image
import requests
from io import BytesIO

if platform == 'android':
    path = join(dirname(str(App.user_data_dir)), 'DownTube')
else:
    path = 'E:\\TestsDownTube'


class ADM(ScreenManager):
    pass


class Prince(Screen):
    def start(self, url):
        try:
            vid = YouTube(str(url))
        except RegexMatchError:
            self.ids.direct.text = ''
        except Exception as erro:
            self.ids.direct.text = str(erro)
        else:
            response = requests.get(vid.thumbnail_url)
            img = Image.open(BytesIO(response.content))
            img.save('./data/tumb.png')
            self.ids.tumb.source = './data/tumb.png'
            self.ids.tumb.reload()
            remove('./data/tumb.png')
            self.ids.vitle.text = vid.title


class Latitle(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = sp(20)

    def on_size(self, *args):
        self.text_size = (self.width - sp(10), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)


class Main(App):
    def build(self):
        return ADM()


Main().run()
