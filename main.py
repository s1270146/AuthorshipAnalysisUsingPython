import Weight
import Analyse
import getTweets as gt
import processData as pd
from tqdm import tqdm

def main (A_NAME , B_NAME):
    #A_NAME = 'BarackObama'
    #B_NAME = 'taylorswift13'

    #print("Read "+A_NAME+"'s Tweets")
    ATweets = gt.getAllTweetsBy2Authors(A_NAME)
    AList = pd.processDatasets(ATweets)
    #print("Read "+B_NAME+"'s Tweets")
    BTweets = gt.getAllTweetsBy2Authors(B_NAME)
    BList = pd.processDatasets(BTweets)

    #print("generate weight of all tweets object")
    ALL = Weight.IDF()

    #print("generate weight of "+A_NAME+" object")
    AsplitIdx = int(len(AList)*0.9)
    A = Weight.TF(AList[0 : AsplitIdx] , AsplitIdx)

    #print("generate weight of "+B_NAME+" object")
    BsplitIdx = int(len(BList)*0.9)
    B = Weight.TF(BList[0 : BsplitIdx] , BsplitIdx)


    #print("'known = "+A_NAME+" , questioned = "+A_NAME+"' un-gram analysing")
    aa = Analyse.analise(ALL , A , AList[AsplitIdx : len(AList)] , 1)
    #print("'known = "+A_NAME+" , questioned = "+B_NAME+"' un-gram analysing")
    ab = Analyse.analise(ALL , A , BList[BsplitIdx : len(BList)] , 1)
    #print("'known = "+B_NAME+" , questioned = "+A_NAME+"' un-gram analysing")
    ba = Analyse.analise(ALL , B , AList[AsplitIdx : len(AList)] , 1)
    #print("'known = "+B_NAME+" , questioned = "+B_NAME+"' bun-gram analysing")
    bb = Analyse.analise(ALL , B , BList[BsplitIdx : len(BList)] , 1)

    print("-----------------------------------UNIGRAM-----------------------------------")
    print("known = "+A_NAME+" , questioned = "+A_NAME+" : " + str(round(aa , 3)))
    print("known = "+A_NAME+" , questioned = "+B_NAME+" : " + str(round(ab , 3)))
    print("known = "+B_NAME+" , questioned = "+A_NAME+" : " + str(round(ba , 3)))
    print("known = "+B_NAME+" , questioned = "+B_NAME+" : " + str(round(bb , 3)))

    #print("'known = "+A_NAME+" , questioned = "+A_NAME+"' bi-gram analysing")
    aa = Analyse.analise(ALL , A , AList[AsplitIdx : len(AList)] , 2)
    #print("'known = "+A_NAME+" , questioned = "+B_NAME+"' bi-gram analysing")
    ab = Analyse.analise(ALL , A , BList[BsplitIdx : len(BList)] , 2)
    #print("'known = "+B_NAME+" , questioned = "+A_NAME+"' bi-gram analysing")
    ba = Analyse.analise(ALL , B , AList[AsplitIdx : len(AList)] , 2)
    #print("'known = "+B_NAME+" , questioned = "+B_NAME+"' bi-gram analysing")
    bb = Analyse.analise(ALL , B , BList[BsplitIdx : len(BList)] , 2)

    print("-----------------------------------BIGRAM-----------------------------------")
    print("known = "+A_NAME+" , questioned = "+A_NAME+" : " + str(round(aa , 3)))
    print("known = "+A_NAME+" , questioned = "+B_NAME+" : " + str(round(ab , 3)))
    print("known = "+B_NAME+" , questioned = "+A_NAME+" : " + str(round(ba , 3)))
    print("known = "+B_NAME+" , questioned = "+B_NAME+" : " + str(round(bb , 3)))

    #print("'known = "+A_NAME+" , questioned = "+A_NAME+"' tri-gram analysing")
    aa = Analyse.analise(ALL , A , AList[AsplitIdx : len(AList)] , 3)
    #print("'known = "+A_NAME+" , questioned = "+B_NAME+"' tri-gram analysing")
    ab = Analyse.analise(ALL , A , BList[BsplitIdx : len(BList)] , 3)
    #print("'known = "+B_NAME+" , questioned = "+A_NAME+"' tri-gram analysing")
    ba = Analyse.analise(ALL , B , AList[AsplitIdx : len(AList)] , 3)
    #print("'known = "+B_NAME+" , questioned = "+B_NAME+"' tri-gram analysing")
    bb = Analyse.analise(ALL , B , BList[BsplitIdx : len(BList)] , 3)

    print("-----------------------------------TRIGRAM-----------------------------------")
    print("known = "+A_NAME+" , questioned = "+A_NAME+" : " + str(round(aa , 3)))
    print("known = "+A_NAME+" , questioned = "+B_NAME+" : " + str(round(ab , 3)))
    print("known = "+B_NAME+" , questioned = "+A_NAME+" : " + str(round(ba , 3)))
    print("known = "+B_NAME+" , questioned = "+B_NAME+" : " + str(round(bb , 3)))


if __name__ == '__main__':
    names = ["katyperry","justinbieber","taylorswift13","BarackObama","rihanna","YouTube","ladygaga","TheEllenShow","Twitter","jtimberlake","KimKardashian","britneyspears","Cristiano","selenagomez","cnnbrk","jimmyfallon","ArianaGrande","shakira","instagram","ddlovato"]
    main('jimmyfallon' , 'Cristiano')

    """
    for i in tqdm(range(len(names))):
        for j in range(i , len(names)):
            main(names[i], names[j])
            """