
import json ,urllib.request
import json
import time
import datetime





"""""
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
dateTime = datetime.date(2019,1,25)
unixtime = str(int(time.mktime(dateTime.timetuple())))
"""""






def downloadStockData(array, minIndex):
    counterStockSymbols = minIndex
    strStockSymbols = ""
    indexRange = 500
    if minIndex == 5500:
        indexRange = 372

    while counterStockSymbols < minIndex + indexRange:
        strStockSymbols = strStockSymbols + array[counterStockSymbols]
        counterStockSymbols = counterStockSymbols + 1
    

    data = urllib.request.urlopen("https://query1.finance.yahoo.com/v7/finance/quote?symbols="+strStockSymbols).read()
    output = json.loads(data.decode('utf-8'))
    
    dateToday = str(datetime.datetime.now())

    counterStockSymbols = 0
    while counterStockSymbols < indexRange:

        isLegalLine = 1

        title1 = "Stock #" + str(minIndex + counterStockSymbols)
        title11 = "------------"
        try:

            symbol =  str(output['quoteResponse']['result'][counterStockSymbols]['symbol'])
        except Exception:
            symbol = ""
            isLegalLine = 0

        try:
            DaysRange = str(output['quoteResponse']['result'][counterStockSymbols]['regularMarketDayRange'])
        except Exception:
            DaysRange = 0
        try:
            bid =  str(output['quoteResponse']['result'][counterStockSymbols]['bid'])
        except Exception:
            bid = 0
        try:
            earningsTimestampStart =  str( output['quoteResponse']['result'][counterStockSymbols]['earningsTimestampStart'])
        except Exception:
            earningsTimestampStart = 0
        try:
            earningsTimestampEnd =  str \
                (output['quoteResponse']['result'][counterStockSymbols]['earningsTimestampEnd'])
        except Exception:
            earningsTimestampEnd = 0

        try:
            marketCap =  str(output['quoteResponse']['result'][counterStockSymbols]['marketCap'])
        except Exception:
            marketCap = 0

        try:
            averageDailyVolume10Day =  str \
                (output['quoteResponse']['result'][counterStockSymbols]['averageDailyVolume10Day'])
        except Exception:
            averageDailyVolume10Day = 0

        try:
            epsTrailingTwelveMonths = str(output['quoteResponse']['result'][counterStockSymbols]['epsTrailingTwelveMonths'])
        except Exception:
            epsTrailingTwelveMonths = 0
        try:
            regularMarketPreviousClose = str(output['quoteResponse']['result'][counterStockSymbols]['regularMarketPreviousClose'])
        except Exception:
            regularMarketPreviousClose = 0
        try:
            ask =  str(output['quoteResponse']['result'][counterStockSymbols]['ask'])
        except Exception:
            ask = 0

        try:
            fiftyTwoWeekLowChange =  str (output['quoteResponse']['result'][counterStockSymbols]['fiftyTwoWeekLowChange'])
        except Exception:
            fiftyTwoWeekLowChange = 0
        try:
            fiftyTwoWeekLow =  str(output['quoteResponse']['result'][counterStockSymbols]['fiftyTwoWeekLow'])
        except Exception:
            fiftyTwoWeekLow = 0
        try:
            regularMarketPrice = str( output['quoteResponse']['result'][counterStockSymbols]['regularMarketPrice'])
        except Exception:
            regularMarketPrice = 0
        try:
            regularMarketTime = str \
                (output['quoteResponse']['result'][counterStockSymbols]['regularMarketTime'])
        except Exception:
            regularMarketTime = 0
        try:
            regularMarketChange = str(output['quoteResponse']['result'][counterStockSymbols]['regularMarketChange'])
        except Exception:
            regularMarketChange = 0
        try:
            regularMarketOpen =  str(output['quoteResponse']['result'][counterStockSymbols]['regularMarketOpen'])
        except Exception:
            regularMarketOpen = 0
        try:
            regularMarketDayHigh =  str(output['quoteResponse']['result'][counterStockSymbols]['regularMarketDayHigh'])
        except Exception:
            regularMarketDayHigh = 0
        try:
            regularMarketDayLow = str( output['quoteResponse']['result'][counterStockSymbols]['regularMarketDayLow'])
        except Exception:
            regularMarketDayLow = 0
        try:
            regularMarketVolume = str(output['quoteResponse']['result'][counterStockSymbols]['regularMarketVolume'])
        except Exception:
            regularMarketVolume = 0
        try:
            fiftyTwoWeekRange = str(output['quoteResponse']['result'][counterStockSymbols]['fiftyTwoWeekRange'])
        except Exception:
            fiftyTwoWeekRange = 0

        try:
            earningsTimestampStart = output['quoteResponse']['result'][counterStockSymbols]['earningsTimestampStart']
            earningTimestampStartDate =   datetime.datetime.utcfromtimestamp(earningsTimestampStart).strftime('%m-%d-%Y')

        except Exception:
            earningTimestampStartDate = 0
        try:
            earningsTimestampEnd = output['quoteResponse']['result'][counterStockSymbols]['earningsTimestampEnd']
            earningsTimestampEndDate = datetime.datetime.utcfromtimestamp(earningsTimestampEnd).strftime('%m-%d-%Y')
        except Exception:
            earningsTimestampEndDate = 0
        try:
            trailingAnnualDividend = output['quoteResponse']['result'][counterStockSymbols]['trailingAnnualDividend']
        except Exception:
            trailingAnnualDividend = 0
        try:
            trailingAnnualDividendRate =  output['quoteResponse']['result'][counterStockSymbols]['trailingAnnualDividendRate']
        except Exception:
            trailingAnnualDividendRate = 0

        try:
            regularMarketChangePercent = str(
                output['quoteResponse']['result'][counterStockSymbols]['regularMarketChangePercent'])
        except Exception:
            regularMarketChangePercent = 0

        message = symbol + '\t' + str(regularMarketChangePercent) + '\t' + str(regularMarketChange) + '\t' + 'NA' + '\t' + str(regularMarketPrice) + '\t' + \
                  str(regularMarketDayLow) + '\t' + 'NA' + '\t' + str(regularMarketDayHigh) + '\t' + \
                  str(regularMarketPreviousClose) + '\t' + str(regularMarketOpen) + '\t' + str(bid) + '\t' + \
                  str(ask) + '\t' + str(DaysRange) + '\t' + str(fiftyTwoWeekRange) + \
                  '\t' + str(regularMarketVolume) + '\t' + str(averageDailyVolume10Day) + '\t' + str(marketCap) + '\t' + 'NA' + '\t' + 'NA' + \
                  '\t' + str(epsTrailingTwelveMonths) + '\t' + str(earningTimestampStartDate) + ' - ' + str(earningsTimestampEndDate) + \
                  '\t' + str(trailingAnnualDividend) + '\t' + str(trailingAnnualDividendRate) + '\t' + 'NA' + '\n'



        if isLegalLine == 1:
            with open('stockout.txt', 'a') as the_file:
                the_file.write(message)

        counterStockSymbols = counterStockSymbols + 1







with open("stockin.txt", "r") as ins:
    array = []
    for line in ins:
        ext = ","
        fileNameOnly = line[:line.find(ext) + len(ext)]
        array.append(fileNameOnly)

countQueries = 0
minIndex = 0

while countQueries < 12:
    downloadStockData(array, minIndex)
    minIndex = minIndex + 500
    countQueries = countQueries + 1
    time.sleep(30)

