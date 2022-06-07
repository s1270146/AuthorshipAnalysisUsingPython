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
    print()
    for i in range(1,11):
        passingPoint = round(i/(10**N),5)
        print("################# Pass Score = {} #################".format(passingPoint))
        print()

        cntFF = sum(x>passingPoint for x in FF)
        cntFS = sum(x>passingPoint for x in FS)

        cntSS = sum(x>passingPoint for x in SS)
        cntSF = sum(x>passingPoint for x in SF)

        tp = round(cntFF/len(FF)*100, 2)
        fp = round(cntFS/len(FF)*100, 2)
        fn = round(cntSF/len(SS)*100, 2)
        tn = round(cntSS/len(SS)*100, 2)

        print(str(cntFF) + " out of " + str(len(FF)) + " (" + str(tp) + "%)")
        print(str(cntFS) + " out of " + str(len(FF)) + " (" + str(fp) + "%)")
        print(str(cntSS) + " out of " + str(len(SS)) + " (" + str(tn) + "%)")
        print(str(cntSF) + " out of " + str(len(SS)) + " (" + str(fn) + "%)")

        print()

        print("Accurancy(正解率) : " + str(round((tp+tn)/(tp+fp+fn+tn)*100,2)) + "%")
        print("Precision(適合率) : " + str(round(tp/(tp+fp)*100,2)) + "%")
        print("Recall(再現率) : " + str(round(tp/(tp+fn)*100,2)) + "%")
        print("Specificity(特異率) : " + str(round(tn/(tn+fp)*100,2)) + "%")

        print()