from ngram import doNGram

UNIGRAM = 1
BIGRAM = 2
TRIGRAM = 3

def analise(all , known , questioned , ngram) -> float:
    questioned = doNGram(questioned, ngram)
    weight = 0.0
    for i in range(len(questioned)):
        weight += all.getWeight(ngram , questioned[i]) * known.getWeight(ngram , questioned[i])
    return weight

