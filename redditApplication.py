from urllib import *
import praw
from pprint import pprint
import json

# Handles import error in Tkinter.
try:
	# Python2
	import Tkinter as tk
except ImportError:
	# Python3
	import tkinter as tk

# Global Variables
loginNotFinished = True

# Defines Reddit Object
redditObject = praw.Reddit(user_agent="reddit Standalone Application")

def sendLoginRequest():
	global loginNotFinished, userName, userPass, userLabel, buttonFrame
	loginNotFinished = False
	redditObject.login(userName.get(), userPass.get(), disable_warning=True)

	# Makes changes to login label.
	userLabel.destroy()
	userLabel = tk.Label(buttonFrame, text = "Currently logged: " + userName.get(), font=("Arial", 10), anchor=tk.W)
	userLabel.pack(side = tk.BOTTOM)

def getLogin():
	global redditObject, root, loginNotFinished, userName, userPass
	loginWindow = tk.Toplevel(root)
	while loginNotFinished:
		tk.Label(loginWindow, text="Username").grid(row=0)
		tk.Label(loginWindow, text="Password").grid(row=1)
		userName = tk.Entry(loginWindow)
		userPass = tk.Entry(loginWindow, show="*")
		userName.grid(row=0, column=1)
		userPass.grid(row=1, column=1)
		loginFinished = tk.Button(loginWindow, text="Login", command = sendLoginRequest).grid(row=2)
		loginFinished.pack()

def pullRedditFeed():
	global root, submissionListbox, submission, subreddit
	subreddit = redditObject.get_subreddit('python')
	for submission in subreddit.get_hot(limit=10):
		submissionListbox.insert(tk.END, submission.title)
	pullFeedID()

def pullFeedID():
	global subreddit, submissionList
	submissionList = [0]
	for submissionId in subreddit.get_hot(limit=10):
		submissionList.append(submissionId.id)

def openRedditWindow(self):
	global submissionListbox, submissionList
	submissionWindow = tk.Toplevel(root, width=580, height=680)

	# Pulls user input.
	userSelect = submissionListbox.curselection()
	userSelectFinal = submissionList[userSelect[0]]
	submissionData = redditObject.get_submission(submission_id = userSelectFinal)
	pprint (vars(submissionData))

	submissionWindowFrame = tk.Frame(submissionWindow)
	submissionWindowFrame.pack()

	submissionWindowTitle = tk.Label(submissionWindowFrame, text=submissionData.title, font=("Arial", 14), anchor=tk.W, justify=tk.LEFT)
	submissionWindowTitle.pack()

	submissionWindowSelfText = tk.Label(submissionWindowFrame, text=submissionData.selftext, wraplength=1000, font=("Arial", 10), anchor=tk.W, justify=tk.LEFT)
	submissionWindowSelfText.pack()



def getAbout():
	print('Test')

root = tk.Tk()
root.title('reddit Standalone')

headerLabel = tk.Label(root, text = "Standalone Reddit Application", font=("Arial", 10), anchor=tk.W)
headerLabel.pack()

submissionListbox = tk.Listbox(root, width=200)
submissionListbox.bind("<Double-Button-1>", openRedditWindow)
submissionListbox.pack()

buttonFrame = tk.Frame(root, width = 200)
buttonFrame.pack()

userLabel = tk.Label(buttonFrame, text = "Currently logged in: None", font=("Arial", 10), anchor=tk.W)
userLabel.pack(side = tk.BOTTOM)

loginButton = tk.Button(buttonFrame, text="Login", command = getLogin)
loginButton.pack(side = tk.LEFT)

getFeedButton = tk.Button(buttonFrame, text="Check Feed", command = pullRedditFeed)
getFeedButton.pack(side = tk.LEFT)

aboutButton = tk.Button(buttonFrame, text="About", command = getAbout)
aboutButton.pack(side = tk.LEFT)

root.mainloop()