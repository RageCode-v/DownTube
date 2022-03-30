from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.utils import platform
from kivy.metrics import sp
from pytube import *
from pytube.exceptions import RegexMatchError
from os.path import join
from os import remove, environ
from certifi import where
from PIL import Image
import requests
from io import BytesIO

environ['SSL_CERT_FILE'] = where()
pamg = './data/image.png'
tumb = './data/tumb.png'

if platform == 'android':
    from android.permissions import request_permissions, Permission
    from android.storage import primary_external_storage_path
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    path = join(primary_external_storage_path(), 'Download')
else:
    path = 'E:\\TestsDownTube'


class ADM(ScreenManager):
    pass


class Prince(Screen):
    obvid = None
    op = {}

    def reset(self):
        self.ids.direct.text = ''
        self.ids.tumb.source = pamg
        self.ids.vitle.text = 'Video title'
        self.obvid = None
        self.op = {}

    def start(self, url):
        try:
            vid = YouTube(str(url))
        except RegexMatchError:
            self.ids.direct.text = ''
            self.ids.tumb.source = pamg
            self.ids.vitle.text = 'Vídeo não encontrado'
        except Exception as erro:
            self.ids.direct.text = str(erro)
        else:
            try:
                response = requests.get(vid.thumbnail_url)
            except Exception as erro:
                self.ids.direct.text = str(erro)
            else:
                try:
                    img = Image.open(BytesIO(response.content))
                    img.save(tumb)
                except Exception as erro:
                    self.ids.direct.text = str(erro)
                else:
                    self.ids.tumb.source = tumb
                    remove(tumb)
                self.ids.vitle.text = vid.title
            finally:
                self.obvid = vid

    def select(self, opt):
        self.op = opt

    def down_this(self):
        if self.op == {}:
            pass
        else:
            try:
                st = self.obvid.streams.get_by_itag(self.op['itag'])
            except KeyError:
                pass
            except Exception as erro:
                self.ids.direct.text = str(erro)
            else:
                try:
                    st.download(path, ((self.obvid.title.replace('/', ' ').replace('\\', ' '))+self.op['ext']))
                    self.reset()
                except Exception as erro:
                    self.ids.direct.text = str(erro)


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