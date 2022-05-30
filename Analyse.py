from tqdm import tqdm
class Analyse:
    
    N=2
    questionedDict = [] # 10% of self's tweets
    knownDict = [] # 90% of self's tweet
    questionedList = []
    knownList = []   

    def __init__(self, tweetList) -> None:
        """set initial conditions

        Args:
            self: author 
            tweetList: tweetList of its author 
        """

        # devide into two parts 'known' and 'questioned'
        for i in range(len(tweetList)):
            if i < len(tweetList)*0.9:
                self.knownList.append(tweetList[i])
            else:
                self.questionedList.append(tweetList[i])

        # do bi-gram for knownList
        for k in range(len(self.knownList)):
            for i in range(len(self.knownList[k])- self.N + 1):
                tmp = []
                for j in range(self.N):
                    tmp.append(self.knownList[k][i+j])
                self.knownDict.append(tmp)

        # do bi-gram for questionedList
        for k in range(len(self.questionedList)):
            for i in range(len(self.questionedList[k])- self.N+ 1):
                tmp = []
                for j in range(self.N):
                    tmp.append(self.questionedList[k][i+j])
                self.questionedDict.append(tmp)

    # target -> questionedText : dict 
    def analyse(self,target) -> str:
        cnt = 0
        for i in tqdm(range(len(self.knownDict))):
            for j in range(len(target)):
                if (self.knownDict[j][0] == target[j][0]) & (self.knownDict[j][1] == target[j][1]):
                    cnt += 1
                    print(cnt)
        return str(cnt)
