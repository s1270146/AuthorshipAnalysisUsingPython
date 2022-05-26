def processDatasets(tweets):
    processedList = []
    for tweet in tweets:
        processedList.append(tweet.split())
    return processedList