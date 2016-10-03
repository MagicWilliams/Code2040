import json
import requests
import datetime
from datetime import timedelta

# resp = requests.post('http://challenge.code2040.org/api/register', json={'token': "b445cce28b1d51745774db40e999c4ea", 'github': "https://github.com/MagicWilliams/Code2040"})
# if resp.status_code == 200:
#    #SOMETHING WENT WRONG
#    print("We out!")


#Part Two

# resp = requests.post('http://challenge.code2040.org/api/reverse', json={'token': 'b445cce28b1d51745774db40e999c4ea'})
# word = resp.content
# print("This is the word I'm about to reverse: " + word)
# reversedWord = word[::-1]
# print("This is the word I've reversed: " + reversedWord)

# requests.post('http://challenge.code2040.org/api/reverse/validate', json={'token': "b445cce28b1d51745774db40e999c4ea", 'string': reversedWord})


#Step 3
# resp = requests.post('http://challenge.code2040.org/api/haystack', json={'token': 'b445cce28b1d51745774db40e999c4ea'})

# print(resp.content)
# haystack = resp.content
# d = json.loads(haystack)
# needle = d["needle"]
# print("the needle is: " + needle)
# counter = 0
# finalCount = 0

# for key in d["haystack"]:
#     if key == needle:
#         finalCount = counter
#     else:
#         counter = counter + 1

# print(finalCount)

# resp = requests.post('http://challenge.code2040.org/api/haystack/validate', json={'token': 'b445cce28b1d51745774db40e999c4ea', 'needle': finalCount})

#Step Four
# returnList = []
# resp = requests.post('http://challenge.code2040.org/api/prefix', json={'token': 'b445cce28b1d51745774db40e999c4ea'})
# data = json.loads(resp.content)

# prefix = data["prefix"]
# print("the prefix is: " + prefix)
# lengthPrefix = len(prefix)
# print("the words are: ")
# print(data["array"])
# print("")
# print("my list")

# for key in data["array"]:
#     if key[:lengthPrefix] != prefix:
#         returnList.append(key)

# print(returnList)

# resp = requests.post('http://challenge.code2040.org/api/prefix/validate', json={'token': 'b445cce28b1d51745774db40e999c4ea', 'array': returnList})


#Step Five
resp = requests.post('http://challenge.code2040.org/api/dating', json={'token': 'b445cce28b1d51745774db40e999c4ea'})
print resp.content

def convertToDates(numSeconds):
    months = numSeconds / (7*24*60*60)
    weeks = numSeconds / (7*24*60*60)
    days = numSeconds / (24*60*60) - 7*weeks
    hours = numSeconds / (60*60) - 7*24*weeks - 24*days
    minutes = numSeconds / 60 - 7*24*60*weeks - 24*60*days - 60*hours
    seconds = numSeconds - 7*24*60*60*weeks - 24*60*60*days - 60*60*hours - 60*minutes
    print("Number of weeks: " + str(weeks))
    print("Number of days: " + str(days))
    print("Number of hours: " + str(hours))
    print("Number of minutes: " + str(minutes))
    print("Number of seconds: " + str(seconds))

convertToDates(82070)
