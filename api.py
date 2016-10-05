import json
import requests
import datetime
from datetime import timedelta

# Registration for Step 1!
 resp = requests.post('http://challenge.code2040.org/api/register', json={'token': "b445cce28b1d51745774db40e999c4ea", 'github': "https://github.com/MagicWilliams/Code2040"})
 if resp.status_code == 200:
    print("Let's gooooo!")

# Step Two -  Reversing a string
resp = requests.post('http://challenge.code2040.org/api/reverse', json={'token': 'b445cce28b1d51745774db40e999c4ea'})
word = resp.content
print("This is the word I'm about to reverse: " + word)
reversedWord = word[::-1]
print("This is the word I've reversed: " + reversedWord)
requests.post('http://challenge.code2040.org/api/reverse/validate', json={'token': "b445cce28b1d51745774db40e999c4ea", 'string': reversedWord})


# Step 3 - Needle and the Haystack
resp = requests.post('http://challenge.code2040.org/api/haystack', json={'token': 'b445cce28b1d51745774db40e999c4ea'})
print(resp.content)
haystack = resp.content
d = json.loads(haystack)
needle = d["needle"]
print("the needle is: " + needle)
counter = 0
finalCount = 0

for key in d["haystack"]:
    if key == needle:
         finalCount = counter
    else:
         counter = counter + 1

print(finalCount)
resp = requests.post('http://challenge.code2040.org/api/haystack/validate', json={'token': 'b445cce28b1d51745774db40e999c4ea', 'needle': finalCount})


# Step Four
returnList = []
resp = requests.post('http://challenge.code2040.org/api/prefix', json={'token': 'b445cce28b1d51745774db40e999c4ea'})
data = json.loads(resp.content)

prefix = data["prefix"]
lengthPrefix = len(prefix)

for key in data["array"]:
     if key[:lengthPrefix] != prefix:
         returnList.append(key)

resp = requests.post('http://challenge.code2040.org/api/prefix/validate', json={'token': 'b445cce28b1d51745774db40e999c4ea', 'array': returnList})

#Step Five
resp = requests.post('http://challenge.code2040.org/api/dating', json={'token': 'b445cce28b1d51745774db40e999c4ea'})
date = resp.content
jsonDate = json.loads(date)


# Will convert the number of seconds into their equivalent in weeks, days, hours, minutes, and seconds
# These variable are the amounts of days, hours, etc. that we need to add to the first datestamp given
weeks = 0
days = 0
hours = 0
minutes = 0
seconds = 0

interval = int(jsonDate["interval"])

weeks = interval / (7*24*60*60)
days = interval / (24*60*60) - 7*weeks
hours = interval / (60*60) - 7*24*weeks - 24*days
minutes = interval / 60 - 7*24*60*weeks - 24*60*days - 60*hours
seconds = interval - 7*24*60*60*weeks - 24*60*60*days - 60*60*hours - 60*minutes

# Just a sanity check in the terminal to make sure everything has been correctly calculated
print("number of days to change: " +str(days))
print("number of hours to change: " +str(hours))
print("number of min to change: " +str(minutes))
print("number of seconds to change: " +str(seconds))

currDay = int(date[22:24])
currHour = int(date[25:27])
currMin = int(date[28:30])
currSec = int(date[31:33])

# If we need to add days to the timestamp, then add that number of days to the currentDay given in time stamp. If not, leave it alone!
if days != 0:
    currDay = currDay + days

if hours != 0:
    currHour = currHour + hours
    if currHour >= 24: # This conditional just makes sure that 27 hours converts to 3 hours and adds 1 day to the day count.
        currDay = currDay + 1
        currHour = currHour - 24

if minutes != 0:
    currMin = currMin + minutes
    if currMin >= 60:
            currHour = currHour + 1
            currMin = currMin - 60

if seconds != 0:
    currSec = currSec + seconds
    if currSec >= 60:
            currMin = currMin + 1
            currSec = currSec - 60

# For formatting, all digits less than 10 need to have a 0 in front, and get converted back into strings.
if currDay < 10:
    currDay = "0" +str(currDay)
else:
    currDay = str(currDay)

if currHour < 10:
    currHour = "0" +str(currHour)
else:
    currHour = str(currHour)

if currMin < 10:
    currMin = "0" +str(currMin)
else:
    currMin = str(currMin)

if currSec < 10:
    currSec = "0" +str(currSec)
else:
    currSec = str(currSec)

# Another sanity check
print("new day number: " +currDay)
print("new hour number: " +currHour)
print("new min number: " +currMin)
print("new sec number: " +currSec)

newDate = date[:22] + str(currDay) + "T" + str(currHour) + ":" + str(currMin) + ":" + str(currSec) + date[33:]
newDate = newDate[14:34] # Gets rid of the extra stuff surrounding the datestamp in the original given date.
print date[14:34]
print newDate

resp = requests.post('http://challenge.code2040.org/api/dating/validate', data={'token': 'b445cce28b1d51745774db40e999c4ea', 'datestamp': newDate})
