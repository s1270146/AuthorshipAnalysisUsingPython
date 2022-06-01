from tqdm import tqdm
import ngram as ng

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
        print(len(self.knownList))
        for i in range(self.length - self.lengthMiddle):
            self.questionedList.append(self.tweetList[i+self.lengthMiddle])
            self.questionedDict.append(ng.doNGram(self.tweetList[i+self.lengthMiddle],N))

    def execute(self,target) -> str:
        cnt = 0
        leng2 = 0
        for i in range(len(target)):
            leng2 = len(target[i])
            for j in range(leng2):
                if (target[i][j] in self.knownDict[i]):
                    cnt += 1
        return str(cnt)
