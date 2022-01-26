from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from youtube_dl import YoutubeDL

Window.softinput_mode = 'below_target'


class Adm(ScreenManager):
    pass


class Tel1(Screen):
    def get_video(self, url):
        ydl_opts = {'FORMAT': 'MP4',
                    'outtmpl': '/storage/emulated/0/Ydown/%(title)s.%(ext)s'
                    }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(url)])
        self.ids.url.text = ''


class Main(App):
    def build(self):
        return Adm()


Main().run()
