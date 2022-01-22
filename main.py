from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from pytube import YouTube


class Adm(ScreenManager):
    pass


class Tel1(Screen):
    def get_video(self, url):
        vid = YouTube(str(url))
        self.ids.url.text = ''
        down = vid.streams.get_by_itag(22)
        down.download('tests')


class Main(App):
    def build(self):
        return Adm()


Main().run()
