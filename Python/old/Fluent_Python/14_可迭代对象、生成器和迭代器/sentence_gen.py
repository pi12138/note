# 使用生成器代替 sentence_iter.py 中的 SentenceIterator
import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence {}'.format(reprlib.repr(self.text))

    def __iter__(self):
        for i in self.words:
            yield i
        return 

    # # 也可以这样
    # def __iter__(self):
    #     return iter(self.words)