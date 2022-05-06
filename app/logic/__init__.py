from logic.notify import notbar
from logic.wherepath import down_path
from logic.downloader import Order
from logic.exceptions import *


def load_colors():
    from json import loads

    with open('./data/colors.json', 'r') as f:
        res = loads(f.read())
    return res
