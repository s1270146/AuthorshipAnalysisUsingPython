from tqdm import tqdm
from ngram import doNGram

class Analyse:
    UNIGRAM = 1
    BIGRAM = 2
    TRIGRAM = 3
    def __init__(self, tweetList) -> None:
        self.questioned2Dict = []
        self.known2Dict = []
        self.known1Dict = []
        self.featureList = []

        #ユニグラム：重み生成
        self.known1Dict = doNGram(tweetList[0 : int(len(tweetList)*0.9)], self.UNIGRAM)
        for i in tqdm(range(len(self.known1Dict))):
            flag = True
            for j in range(len(self.featureList)):
                if self.featureList[j].word == self.known1Dict[i]:
                    self.featureList[j].weight +=1
                    flag = False
                    break
            if flag : self.featureList.append(Feature(self.known1Dict[i]))
        for i in range(len(self.featureList)):
            self.featureList[i].weight = round(1 / self.featureList[i].weight , 5)

        #バイグラム、トリグラム：データを加工
        self.known2Dict = doNGram(tweetList[0 : int(len(tweetList)*0.9)], self.BIGRAM)
        self.questioned2Dict = doNGram(tweetList[int(len(tweetList)*0.9) : len(tweetList)], self.BIGRAM)

        self.known3Dict = doNGram(tweetList[0 : int(len(tweetList)*0.9)], self.TRIGRAM)
        self.questioned3Dict = doNGram(tweetList[int(len(tweetList)*0.9) : len(tweetList)], self.TRIGRAM)

    #バイグラム用分析関数
    def bigramAnalyse(self,target) -> float:
        weight = 0
        for i in tqdm(range(len(self.known2Dict))):
            for j in range(len(target)):
                if self.known2Dict[i] == target[j]:
                    #重み適用
                    for k in range(len(self.featureList)):
                        if self.known2Dict[i][0] == self.featureList[k].word[0]:
                            weight += self.featureList[k].weight
                        if self.known2Dict[i][1] == self.featureList[k].word[0]:
                            weight += self.featureList[k].weight
        return weight / (len(self.known2Dict[i]) * len(target))

    #トリグラム用分析関数
    def trigramAnalyse(self,target) -> float:
        weight = 0
        for i in tqdm(range(len(self.known3Dict))):
            for j in range(len(target)):
                if self.known3Dict[i] == target[j]:
                    #重み適用（トリグラムは重み倍）
                    for k in range(len(self.featureList)):
                        if self.known3Dict[i][0] == self.featureList[k].word[0]:
                            weight += self.featureList[k].weight * 5
                        if self.known3Dict[i][1] == self.featureList[k].word[0]:
                            weight += self.featureList[k].weight * 5
                        if self.known3Dict[i][2] == self.featureList[k].word[0]:
                            weight += self.featureList[k].weight * 5
        return weight / (len(self.known3Dict[i]) * len(target))

class Feature:
        def __init__(self, word):
            self.word = word #単語
            self.weight = 1  #重みの比率（１〜０）
            