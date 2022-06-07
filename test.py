import Weight
import Analyse
import getTweets as gt
import processData as pd
from tqdm import tqdm
import random

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

anotherAuthorFirst = gt.anotherTweets(FirstAuthor.name, len(FirstAuthorList)-firstMiddle)
anotherAuthorSecond = gt.anotherTweets(SecondAuthor.name, len(SecondAuthorList)-secondMiddle)

def getN(N) :
    if N == 1: return 'Uni'
    elif N == 2 : return 'Bi'
    elif N == 3 : return 'Tri'

for N in range(1,4) : 
    
    print("======================= {}-Gram ==========================".format(getN(N)))
    FF = Analyse.putScore(AllTweetsWeight , FirstAuthorWeight , FirstAuthorList[firstMiddle : len(FirstAuthorList)] , N)
    FA = Analyse.putScore(AllTweetsWeight , FirstAuthorWeight , anotherAuthorFirst , N)

    SS = Analyse.putScore(AllTweetsWeight , SecondAuthorWeight , SecondAuthorList[secondMiddle : len(SecondAuthorList)] , N)
    SA = Analyse.putScore(AllTweetsWeight , SecondAuthorWeight , anotherAuthorSecond , N)
    print()
    for i in range(1,11):

        # 判定する点数
        passingPoint = round(i/(10**N),5)
        
        print("################# Pass Score = {} #################".format(passingPoint))
        print()
        print("--- {} ---".format(FirstAuthor.name))
        cntFF = sum(x>passingPoint for x in FF)
        cntFA = sum(x>passingPoint for x in FA)

        cntSS = sum(x>passingPoint for x in SS)
        cntSA = sum(x>passingPoint for x in SA)

        # 実際:正 予測:正
        tp = cntFF
        # 実際:負 予測:正
        fp = cntFA
        # 実際:正 予測:負
        fn = len(FF)-cntFF
        # 実際:負 予測:負
        tn = len(FA)-cntFA

        print(str(cntFF) + " out of " + str(len(FF)) + " (" + str(round(cntFF/len(FF)*100,2)) + "%)")
        print()
        print("TP = "+ str(tp))
        print("FP = "+ str(fp))
        print("FN = "+ str(fn))
        print("TP = "+ str(tn))
        print()

        print("Accurancy(正解率) : " + str(round((tp+tn)/(tp+fp+fn+tn)*100,2)) + "%")
        print("Precision(適合率) : " + str(round(tp/(tp+fp)*100,2)) + "%")
        print("Recall(再現率) : " + str(round(tp/(tp+fn)*100,2)) + "%")
        print("Specificity(特異率) : " + str(round(tn/(tn+fp)*100,2)) + "%")

        print()
        print("--- {} ---".format(SecondAuthor.name))

        tp = cntSS
        fp = len(FF)-cntSS
        fn = cntSA
        tn = len(SA)-cntSA

        print(str(cntSS) + " out of " + str(len(SS)) + " (" + str(round(cntSS/len(SS)*100,2)) + "%)")
        print()
        print("TP = "+ str(tp))
        print("FP = "+ str(fp))
        print("FN = "+ str(fn))
        print("TP = "+ str(tn))
        print()

        print("Accurancy(正解率) : " + str(round((tp+tn)/(tp+fp+fn+tn)*100,2)) + "%")
        print("Precision(適合率) : " + str(round(tp/(tp+fp)*100,2)) + "%")
        print("Recall(再現率) : " + str(round(tp/(tp+fn)*100,2)) + "%")
        print("Specificity(特異率) : " + str(round(tn/(tn+fp)*100,2)) + "%")

        print()