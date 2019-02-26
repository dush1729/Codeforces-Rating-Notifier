import json
import urllib.request
import pymsgbox
import time
import playsound

handle = 'div24ever'
URL = 'https://codeforces.com/api/user.rating?handle=' + handle

data = json.load(urllib.request.urlopen(URL))
contestList = data["result"]
initialContestCount = len(contestList)

def displayMesage(message):
	pymsgbox.alert(message)

def playSound(filename):
	playsound.playsound(filename)

def alertUser(oldRating, newRating):
	message,filename = "", ""
	if oldRating < newRating:
		message = "Rating incresed by " + str(newRating - oldRating)
		filename = 'assets/win.mp3'
	elif oldRating == newRating:
		message = "No rating change"
	else:
		message = "Rating decreased by " + str(oldRating - newRating)
		filename = 'assets/lose.mp3'
	p1 = Process(target = displayMesage(message))
	p1.start()
	p2 = Process(target = playSound(filename))
	p2.start()
	p1.join()
	p2.join()	

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