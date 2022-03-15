from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from pytube import *
from os.path import join, dirname


class Download(object):
    def __init__(self, link):
        self.vid = YouTube(link)
        self.title = self.vid.title
        self.st = self.vid.streams.first()
        self.PATH = join(dirname(str(App.user_data_dir)), 'Download')

    def baixar(self):
        self.st.download(self.PATH, self.title)


class Adm(ScreenManager):
    pass


class First(Screen):
    def test(self, url):
        self.ids.text.text = ''
        try:
            at = Download(str(url))
        except Exception as ero:
            self.ids.demo.text = str(ero)
        else:
            self.ids.demo.text = at.title
            try:
                at.baixar()
            except Exception as erro:
                self.ids.demo.text = str(erro)


class Main(App):
    def build(self):
        return Adm()


Main().run()
