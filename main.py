from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from pytube import YouTube

Window.softinput_mode = 'below_target'


class Adm(ScreenManager):
    pass


class Tel1(Screen):
    path = '/storage/emulated/0/Ydown'

    def get_video(self, url):
        vid = YouTube(str(url))
        self.ids.url.text = ''
        down = vid.streams.get_by_itag(22)
        down.download(self.path)


class Main(App):
    def build(self):
        return Adm()


Main().run()
