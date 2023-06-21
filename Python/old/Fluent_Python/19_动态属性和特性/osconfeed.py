from urllib.request import urlopen
import warnings
import os
import json


URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def load():
    make_dir('data')
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)

        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


if __name__ == "__main__":
    load()