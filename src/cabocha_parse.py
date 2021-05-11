import CaboCha

class CabochaParser:
    def __init__(self):
        self.cabocha = CaboCha.Parser('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        self.cabocha.parse('')

    def make_chunks(self,text):
        tree = self.cabocha.parse(text)
        token_size = tree.token_size()
        chunks = []
        toChunkId = -1
        for i in range(token_size):
            token = tree.token(i) # cabocha にかけた文章を形態素ごとに取得
            text = token.surface if token.chunk else (text + token.surface) #  上記の出力結果のchunk(文節)ごとにtextが更新されていく
            toChunkId = token.chunk.link if token.chunk else toChunkId
            # 文末かchunk内の最後の要素のタイミングで出力
            if i == token_size - 1 or tree.token(i+1).chunk:
                chunks.append({'index': len(chunks), 'c': text, 'to': toChunkId})
        return chunks