import Weight
import Analyse
import getTweets as gt
import processData as pd
from tqdm import tqdm

# 1人目
# 選択されたアカウントのツイートを抽出
FirstAuthorTweets = gt.getAllTweetsBy2Authors(1)
# 抽出したツイートを単語ごとに区切る(Uni-gram)
FirstAuthorList = pd.processDatasets(FirstAuthorTweets['content'])

# 2人目
# 選択されたアカウントのツイートを抽出
SecondAuthorTweets = gt.getAllTweetsBy2Authors(2)
# 抽出したツイートを単語ごとに区切る(Uni-gram)
SecondAuthorList = pd.processDatasets(SecondAuthorTweets['content'])

# ツイートの重さを作成
AllTweetsWeight = Weight.IDF()

firstMiddle = int(len(FirstAuthorList)*0.9)
FirstAuthorWeight = Weight.TF(FirstAuthorList[0 : firstMiddle] , firstMiddle)

secondMiddle = int(len(SecondAuthorList)*0.9)
SecondAuthorWeight = Weight.TF(SecondAuthorList[0 : secondMiddle] , secondMiddle)

# 著者のオブジェクトを作成
FirstAuthor = Analyse.UserAnalyse(FirstAuthorList, FirstAuthorTweets['authorName'])
SecondAuthor = Analyse.UserAnalyse(SecondAuthorList, SecondAuthorTweets['authorName'])

def getN(N) :
    if N == 1: return 'Uni'
    elif N == 2 : return 'Bi'
    elif N == 3 : return 'Tri'

for N in range(1,4) : 
    
    print("======================= {}-Gram ==========================".format(getN(N)))
    FF = Analyse.putScore(AllTweetsWeight , FirstAuthorWeight , FirstAuthorList[firstMiddle : len(FirstAuthorList)] , N)
    FS = Analyse.putScore(AllTweetsWeight , FirstAuthorWeight , SecondAuthorList[secondMiddle : len(SecondAuthorList)] , N)
    SS = Analyse.putScore(AllTweetsWeight , SecondAuthorWeight , SecondAuthorList[secondMiddle : len(SecondAuthorList)] , N)
    SF = Analyse.putScore(AllTweetsWeight , SecondAuthorWeight , FirstAuthorList[firstMiddle : len(FirstAuthorList)] , N)
    

    sumFF = sum(x>0 for x in FF)
    sumFS = sum(x>0 for x in FS)
    sumSS = sum(x>0 for x in SS)
    sumSF = sum(x>0 for x in SF)

    aveFF = sum(FF)/len(FF)
    aveFS = sum(FS)/len(FS)
    aveSS = sum(SS)/len(SS)
    aveSF = sum(SF)/len(SF)

    print("======= SUM =======")
    print(str(sumFF) + " out of " + str(len(FF)))
    print(str(sumFS) + " out of " + str(len(FS)))
    print(str(sumSS) + " out of " + str(len(SS)))
    print(str(sumSF) + " out of " + str(len(SF)))

    print("======= AVE =======")
    print(aveFF)
    print(aveFS)
    print(aveSS)
    print(aveSF)