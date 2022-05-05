from pytube import YouTube
from pytube.exceptions import RegexMatchError

from logic.notify import notbar
from logic.exceptions import LinkNotFound, StringEmpty


class Order(object):
    vid: YouTube
    tumb: str
    title: str
    opts = {
        '720p/30fps': (22, '.mp4'),
        '360p/30fps': (18, '.mp4'),
        '144p/7fps': (17, '.mp4'),
        'mp3/128kbps': (140, '.mp4')
    }

    def __init__(self, url: str):
        try:
            self.vid = YouTube(str(url), on_progress_callback=self.verify)
        except RegexMatchError:
            raise LinkNotFound
        else:
            self.tumb = str(self.vid.thumbnail_url)
            self.title = str(self.vid.title)

    def verify(self, stream, chunk, bytes_remaining):
        def porcent(te, tot):
            per = (float(te) / float(tot)) * float(100)
            return per

        size = stream.filesize
        p = porcent(bytes_remaining, size)
        notbar(str(self.title), abs(p - 100))

    def alter_title(self):
        try:
            text = self.text_replace(self.title)
        except StringEmpty:
            text = str(self.vid.title)
        self.title = text

    def down_this(self, path: str, op: str):
        self.alter_title()
        name = self.title
        st = self.vid.streams.get_by_itag(self.opts[op][0])
        st.download(path, name+self.opts[op][1])

    @staticmethod
    def text_replace(text: str):
        par = '/\\:*?\"<>|'
        for c in par:
            while c in text:
                text = text.replace(c, ' ')
        res = text.strip()
        if res == '':
            raise StringEmpty
        else:
            return res
