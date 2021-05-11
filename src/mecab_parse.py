import MeCab

class MecabParser:
    def __init__(self):
        self.mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        self.mecab.parse('')

    def make_keywords(self,text):
        node = self.mecab.parseToNode(text)
        keywords = []
        while node:
            word = node.surface
            pos = node.feature.split(",")[1]
            noun = node.feature.split(",")[0:2]
            if pos == "固有名詞" or (noun[0] == "名詞" and "一般" in noun):
                keywords.append(word)
            node = node.next
        return keywords