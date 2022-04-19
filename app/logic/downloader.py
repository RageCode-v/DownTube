from pytube import YouTube
from pytube.exceptions import RegexMatchError

from logic.notify import notbar
from logic.exceptions import LinkNotFound


class Order(object):
    vid: YouTube
    tumb: str
    title: str
    opts: dict = {
        'VHD': (22, '.mp4'),
        'VSD': (18, '.mp4'),
        'VLS': (17, '.mp4'),
        'AP': (140, '.mp3')
    }
    vez = True

    def __init__(self, url: str):
        try:
            self.vid = YouTube(str(url), on_progress_callback=self.verify, on_complete_callback=self.firstag)
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
        notbar(str(self.title), abs(p - 100), self.vez)
        self.vez = False

    def firstag(self):
        self.vez = True

    def alter_title(self, new_title: str):
        self.title = new_title

    def down_this(self, path: str, op: str):
        name = self.title.replace('/', ' ').replace('\\', ' ').strip()
        st = self.vid.streams.get_by_itag(self.opts[op][0])
        st.download(path, name+self.opts[op][1])
