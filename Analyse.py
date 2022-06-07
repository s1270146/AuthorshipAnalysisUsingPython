from ngram import doNGram ,doNGrams
from tqdm import tqdm
import ngram as ng

UNIGRAM = 1
BIGRAM = 2
TRIGRAM = 3

def analyse(all , known , questioned , ngram) -> float:
    questioned = doNGrams(questioned, ngram)
    weight = 0.0
    for i in range(len(questioned)):
        weight += all.getWeight(ngram , questioned[i]) * known.getWeight(ngram , questioned[i])
    return weight

def putScore(all , known , questioned , n) -> float:
    questionedList = []
    # doNGrams(questioned, ngram)
    for tweet in questioned:
        questionedList.append(doNGram(tweet,n))
    scoreList = []
    for tweet in questionedList:
        if len(tweet)<n:
            scoreList.append(0)
            continue
        weight = 0.0
        for i in range(len(tweet)-n+1):
            weight += all.getWeight(n , tweet[i]) * known.getWeight(n , tweet[i])
        scoreList.append(weight)
    return scoreList

class UserAnalyse:
    def __init__(self, tweetList, authorName) -> None:
        self.name = authorName
        self.tweetList = tweetList
        self.length = len(tweetList)
        self.lengthMiddle = self.length * 9 // 10

    def doNGram(self, N):
        self.questionedDict = []
        self.knownDict = []
        self.questionedList = []
        self.knownList = []
        for i in range(self.lengthMiddle):
            self.knownList.append(self.tweetList[i])
            self.knownDict.append(ng.doNGram(self.tweetList[i],N))
        for i in range(self.length - self.lengthMiddle):
            self.questionedList.append(self.tweetList[i+self.lengthMiddle])
            self.questionedDict.append(ng.doNGram(self.tweetList[i+self.lengthMiddle],N))

    def execute(self,target) -> str:
        cnt = 0
        leng2 = 0
        for i in range(len(target)):
            leng2 = len(target[i])
            for j in range(leng2):
                for k in range(len(self.knownDict)):
                    if (target[i][j] in self.knownDict[k]):
                        cnt += 1
        return str(cnt)

