import spacy
import ginza

class GinzaParser:
    def __init__(self, text):
        nlp = spacy.load("ja_ginza")
        self.doc = nlp(text)
        self.phrases = ginza.bunsetu_spans(self.doc)

    def get_keywors_from_ginza(self):
        tokens = [{'i':token.i, 'orth':token.orth_, 'lemma':token.lemma_, 
                'pos':token.pos_, 'tag':token.tag_, 'dep':token.dep_, 'head.i':token.head.i, 
                'children': list(token.children), 'lefts': list(token.lefts), 'rights': list(token.rights),
                'head.text': token.head.text} 
                for sent in self.doc.sents for token in sent]
        return tokens

    def get_named_entity_text_from_ginza(self):
        ents = [ent.text for ent in self.doc.ents]
        return ents

    def get_phrase_dependency_from_ginza(self):
        dependency = [ (ginza.bunsetu_span(token), phrase) for phrase in self.phrases for token in phrase.lefts]
        return dependency