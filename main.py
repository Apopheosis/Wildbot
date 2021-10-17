import markovify
import spacy
import random

nlp = spacy.load("en_core_web_trf")

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


def wildbowify():
    print('Generating...')

    with open('kabinka.txt', 'r') as f:
        text = f.read()
        f.close()
    text_model = POSifiedText(text, retain_original=False)

    with open('result.txt', 'w') as f:
        for j in range(random.randint(5, 25)):
            n = random.randint(1, 7)
            for i in range(n):
                sentence = text_model.make_sentence()
                sentence = sentence[:-2] + '.'
                f.write(sentence + ' ')
            f.write('\n')
            f.write('\n')
        f.close()