from tqdm import tqdm
class Analyse:
    N=2
    questionedDict = []
    knownDict = []
    questionedList = []
    knownList = []   

    def __init__(self, tweetList) -> None:
        for i in range(len(tweetList)):
            if i < len(tweetList)*0.9:
                self.knownList.append(tweetList[i])
            else:
                self.questionedList.append(tweetList[i])

        for k in range(len(self.knownList)):
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
                self.questionedDict.append(tmp)

    def analyse(self,terget) -> str:
        cnt = 0
        for i in tqdm(range(len(self.knownDict))):
            for j in range(len(terget)):
                if (self.knownDict[j][0] == terget[j][0]) & (self.knownDict[j][1] == terget[j][1]):
                    cnt += 1
                    print(cnt)
        return str(cnt)
