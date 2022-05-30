from tqdm import tqdm
import ngram as ng

class userAnalyse:
    """ N=2
    questionedDict = []
    knownDict = []
    questionedList = []
    knownList = []   
    length = 0
    lengthMiddle = 0 """


    def __init__(self, tweetList) -> None:
        """ for i in range(len(tweetList)):
            if i < len(tweetList)*0.9:
                self.knownList.append(tweetList[i])
            else:
                self.questionedList.append(tweetList[i]) """
        
        """ for k in range(len(self.knownList)):
            for i in range(len(self.knownList[k])- self.N + 1):
                tmp = []
                for j in range(self.N):
                    tmp.append(self.knownList[k][i+j])
                self.knownDict.append(tmp)

        for k in range(len(self.questionedList)):
            for i in range(len(self.questionedList[k])- self.N+ 1):
                tmp = []
                for j in range(self.N):
                    tmp.append(self.questionedList[k][i+j])
                self.questionedDict.append(tmp) """
        self.questionedDict = []
        self.knownDict = []
        self.questionedList = []
        self.knownList = [] 

        self.N = 2
        self.length = len(tweetList)
        self.lengthMiddle = self.length * 9 // 10

        for i in range(self.lengthMiddle):
            self.knownList.append(tweetList[i])
            self.knownDict.append(ng.doNGram(tweetList[i],self.N))
        print(len(self.knownList))
        for i in range(self.length - self.lengthMiddle):
            self.questionedList.append(tweetList[i+self.lengthMiddle])
            self.questionedDict.append(ng.doNGram(tweetList[i+self.lengthMiddle],self.N))

    def execute(self,target) -> str:
        cnt = 0
        leng2 = 0
        """ for i in tqdm(range(len(self.knownDict))): """
        for i in range(len(target)):
            leng2 = len(target[i])
            for j in range(leng2):
                if (target[i][j] in self.knownDict[i]):
                    cnt += 1
                    """ print(cnt) """
                    """ print(target[i][j])
                    print(target[i])
                    print(self.knownDict[i]) """
        return str(cnt)
