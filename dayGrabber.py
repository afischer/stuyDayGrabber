
                ##############################################
                #####                                   #####
                #####  stuyDayGrabber by Andrew Fischer  #####
                #####                                   #####
                ##############################################
                ####       (c) Andrew Fischer, 2013       ####
                ####         Under the MIT Licence        ####
                ####     http://andrew.mit-license.org    ####
                ##############################################
                ####  A quick and dirty python script to  ####
                ####  grab the lab and bell schedule from ####
                ####  stuyvesant's awful website. Enjoy!  ####
                ##############################################


# Module Imports
import urllib               #to get website data
import csv                  #to parse and edit website data
import time, datetime       #to get current days of week
import string

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Data Grabbing

stuyedu = 'http://stuy.enschool.org/'
stuy_data = urllib.urlopen(stuyedu)
stuy_data = stuy_data.readlines()
stuy_data = " ".join(stuy_data)
#print stuy_data


## Now we need to get this week's WEEKLY SCHEDULE URL from that data.
def getWeeklyURL():
    end = stuy_data.rfind('WEEKLY SCHEDULE')
    #The links are laid out in the most idiotic table I have ever seen.
    #This is NOT going to be easy or pretty.
    beg = end - 100
    searchArea = stuy_data[beg:end]
    link = searchArea.split('\t')
    link = 'http://stuy.enschool.org' + link[-1][9:][:-2]
    return link


thisWeeksURL = getWeeklyURL()
downloaded_data  = urllib.urlopen(thisWeeksURL)
web_data = downloaded_data.readlines()
web_data = " ".join(web_data) #Turns web_data list into readable html
#print web_data

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Function Creation
### getWeekday grabs the int given by datetime and converts it to the day of the week as used on stuy's website
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



weekday = getWeekday() #Sets weekday to current day of the week



## This is the main function that gets the current bell schedule and lab/PE rotation
def getSchedules():
#    if weekday == "SATURDAY" or "SUNDAY":
#        print "It's the weekend!"
#
#    else:
        
### NOTE:  IF TESTING ON A WEEKEND, COMMENT OUT ABOVE AND CHANGE weekday BELOW
###        TO A DAY OF THE WEEK!! OTHERWISE THIS WILL NOT TEST PROPERLY!!!!

        beg = web_data.rfind('THURSDAY')
        #print beg
        end = beg + 65
        #print end
        searchArea = web_data[beg:end]
        dailyInfo = searchArea.split('<br>')
        dailyInfo = cleanList(dailyInfo) #removes things like \r, null, '' from list
        #print dailyInfo


        bell = str(dailyInfo[1])
        bellBeg = bell.find(':')
        bell = bell[bellBeg + 2:] #removes "Bell:" to get raw bell schedule name
        #print bell


        lab = str(dailyInfo[2])
        labBeg = lab.find(':')
        lab = lab[labBeg + 2:] #removes "'PhysEd/Sci:" to get raw rotation
        #print lab

        if bellCheck(bell) == True and labCheck(lab) == True:
            print bell
            print lab
        else:
            print "ERROR"

### cleanList removes weird html formatting left over from find
def cleanList(L):
    cleanedList = []

    for x in L: 
        x = [x[:x.find('\r')]] #removes '\r' from string items
        cleanedList = cleanedList + x
    while '' in cleanedList: #removes '' from string items
        cleanedList.remove('')
    return cleanedList


### bellCheck checks to make sure the result is an actual schedule, and not a day off notice
def bellCheck(bell):
    if bell == 'Regular' or bell == 'Special' or bell == 'Conference' or bell == "Homeroom":
        return True
    else:
        return False

### labCheck makes sure the given rotation is valid.
def labCheck(lab):
    if lab == 'A' or lab == 'B' or lab == 'A1' or lab == 'B1' or lab == 'A2' or lab == 'B2':
        return True
    else:
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Function Calls:

#print getWeeklyURL()
getSchedules()
                        
