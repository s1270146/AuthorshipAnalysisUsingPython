import math
from getTweets import getAllTweets
import processData as pd
from ngram import doNGrams
from collections import Counter

UNIGRAM = 1
BIGRAM = 2
TRIGRAM = 3

class IDF:
    def __init__(self) -> None:
        self.allTweetsList = getAllTweets()
        self.allTweetsList = pd.processDatasets(self.allTweetsList)
        length = len(self.allTweetsList)

        self.allTweets1List = doNGrams(self.allTweetsList, UNIGRAM)
        self.allTweets1Dict = Counter()
        for i in range(len(self.allTweets1List)):
            self.allTweets1Dict[self.allTweets1List[i][0]] +=1
        for kw, count in self.allTweets1Dict.most_common():
            self.allTweets1Dict[kw] = math.log(length / count)

        self.allTweets2List = doNGrams(self.allTweetsList, BIGRAM)
        self.allTweets2Dict = Counter()
        for i in range(len(self.allTweets2List)):
            self.allTweets2Dict[self.allTweets2List[i][0]+" "+self.allTweets2List[i][1]] +=1
        for kw, count in self.allTweets2Dict.most_common():
            self.allTweets2Dict[kw] = math.log(length / count)

        self.allTweets3List = doNGrams(self.allTweetsList, TRIGRAM)
        self.allTweets3Dict = Counter()
        for i in range(len(self.allTweets3List)):
            self.allTweets3Dict[self.allTweets3List[i][0]+" "+self.allTweets3List[i][1]+" "+self.allTweets3List[i][2]] +=1
        for kw, count in self.allTweets3Dict.most_common():
            self.allTweets3Dict[kw] = math.log(length / count)

    def getWeight(self , num , sample) -> float:
        if num == UNIGRAM:
            tmp = sample[0]
            return self.allTweets1Dict[tmp]
        elif num == BIGRAM:
            tmp = sample[0]+" "+sample[1]
            return self.allTweets2Dict[tmp] 
        elif num == TRIGRAM:
            tmp = sample[0]+" "+sample[1]+" "+sample[2]
            return self.allTweets3Dict[tmp] 
        else:
            return 0


class TF:
    def __init__(self , target , amount) -> None:
        self.tweets1List = doNGrams(target, UNIGRAM)
        self.tweets1Dict = Counter()
        for i in range(len(self.tweets1List)):
            self.tweets1Dict[self.tweets1List[i][0]] +=1
        for kw, count in self.tweets1Dict.most_common():
            self.tweets1Dict[kw] = count / amount

        self.tweets2List = doNGrams(target, BIGRAM)
        self.tweets2Dict = Counter()
        for i in range(len(self.tweets2List)):
            self.tweets2Dict[self.tweets2List[i][0]+" "+self.tweets2List[i][1]] +=1
        for kw, count in self.tweets2Dict.most_common():
            self.tweets2Dict[kw] = count / amount

        self.tweets3List = doNGrams(target, TRIGRAM)
        self.tweets3Dict = Counter()
        for i in range(len(self.tweets3List)):
            self.tweets3Dict[self.tweets3List[i][0]+" "+self.tweets3List[i][1]+" "+self.tweets3List[i][2]] +=1
        for kw, count in self.tweets3Dict.most_common():
            self.tweets3Dict[kw] = count / amount

    def getWeight(self , num , sample) -> float:
        if num == UNIGRAM:
            tmp = sample[0]
            return self.tweets1Dict[tmp]
        elif num == BIGRAM:
            tmp = sample[0]+" "+sample[1]
            return self.tweets2Dict[tmp] 
        elif num == TRIGRAM:
            tmp = sample[0]+" "+sample[1]+" "+sample[2]
            return self.tweets3Dict[tmp]
        else:
            return 0

if __name__ == '__main__':
    test = IDF()