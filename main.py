import json
import urllib.request
import pymsgbox
import time
import playsound

handle = 'dush1729'
URL = 'https://codeforces.com/api/user.rating?handle=' + handle

data = json.load(urllib.request.urlopen(URL))
contestList = data["result"]
initialContestCount = len(contestList)

while True:
	data = json.load(urllib.request.urlopen(URL))
	contestList = data["result"]
	if initialContestCount != len(contestList):
		oldRating = contestList[-1]["oldRating"]
		newRating = contestList[-1]["newRating"]
		if oldRating < newRating:
			playsound.playsound('assets/win.mp3')
			pymsgbox.alert("Rating incresed by " + str(newRating - oldRating))
		elif oldRating == newRating:
			pymsgbox.alert("No rating change")
		else:
			playsound.playsound('assets/lose.mp3')
			pymsgbox.alert("Rating decreased by " + str(oldRating - newRating))
		break
	else:
		time.sleep(60)