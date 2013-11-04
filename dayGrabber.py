
##############################################
###### stuyDayGrabber by Andrew Fischer ######
##############################################
######     (c)Andrew Fischer, 2013      ######

import urllib
import csv
import time, datetime
import string

downloaded_data  = urllib.urlopen('http://stuy.enschool.org/apps/events/show_event.jsp?REC_ID=927665&id=1')
web_data = downloaded_data.readlines()

web_data = " ".join(web_data) #Turns web_data list into readable html

#print web_data

### getWeekday grabs the int given by datetime and converts it to
### the day of the week as used on stuy's website
def getWeekday():
    dayInt = datetime.datetime.today().weekday()
    if dayInt == 0:
        return 'MONDAY'
    if dayInt == 1:
        return 'TUESDAY'
    if dayInt == 2:
        return 'WEDNESDAY'
    if dayInt == 3:
        return 'THURSDAY'
    if dayInt == 4:
        return 'FRIDAY'
    if dayInt == 5:
        return 'SATURDAY'
    if dayInt == 6:
        return 'SUNDAY'


weekday = getWeekday()


def getDay():

#    if weekday == "SATURDAY" or "SUNDAY":
 #       return "It's the weekend!"
#    else:
### NOTE:  IF TESTING ON A WEEKEND, COMMENT OUT ABOVE AND CHANGE weekday BELOW
###        TO A DAY OF THE WEEK!! OTHERWISE THIS WILL NOT TEST PROPERLY!!!!
        beg = web_data.rfind('WEDNESDAY')
        #print beg
        end = beg + 65
        #print end
        searchArea = web_data[beg:end]
        dailyInfo = searchArea.split('<br>')
        dailyInfo = cleanList(dailyInfo) #removes things like \r, null, '' from list
        print dailyInfo


        bell = str(dailyInfo[1])
        bellBeg = bell.find(':')
        bell = bell[bellBeg + 2:] #removes "Bell:" to get raw bell schedule name
        print bell


        lab = str(dailyInfo[2])
        labBeg = lab.find(':')
        lab = lab[labBeg + 2:] #removes "'PhysEd/Sci:" to get raw rotation
        print lab

        

### cleanList removes weird html formatting left over from find
def cleanList(L):
    cleanedList = []

    for x in L: 
        x = [x[:x.find('\r')]] #removes '\r' from string items
        cleanedList = cleanedList + x
    while '' in cleanedList: #removes '' from string items
        cleanedList.remove('')
    return cleanedList






getDay()
                        
