import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize


def getProcessedContentsByLineFromFiles(filep, filen):
    with open(filep, encoding="utf-8_sig") as fp:
        linesp = fp.readlines()
        lineContentsp = []
        for line in linesp:
            contentStringp = "".join(line)
            contentStringp.rstrip()
            sentencesp = sent_tokenize(contentStringp)
            sep_sentencesp = []
            for sentence in sentencesp:
                tagged_token = word_tokenize(sentence)
                tagged_words = nltk.pos_tag(tagged_token)
                sep_sentence = " ".join(w for (w, t) in tagged_words if t.startswith('JJ') or t.startswith('NN') or t.startswith('VB') or t.startswith('RB'))
                sep_sentencesp.append(sep_sentence)
            lineContentsp.append(" ".join(sep_sentencesp))

    with open(filen, encoding="utf-8_sig") as fn:
        linesn = fn.readlines()
        lineContentsn = []
        for line in linesn:
            contentStringn = "".join(line)
            contentStringn.rstrip()
            sentencesn = sent_tokenize(contentStringn)
            sep_sentencesn = []
            for sentence in sentencesn:
                tagged_token = word_tokenize(sentence)
                tagged_words = nltk.pos_tag(tagged_token)
                sep_sentence = " ".join(w for (w, t) in tagged_words if t.startswith('JJ') or t.startswith('NN') or t.startswith('VB') or t.startswith('RB'))
                sep_sentencesn.append(sep_sentence)
            lineContentsn.append(" ".join(sep_sentencesn))

    input_documents = lineContentsp + lineContentsn

    return input_documents, lineContentsp, lineContentsn
