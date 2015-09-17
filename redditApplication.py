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
	redditObject.login(userName.get(), userPass.get())

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

		
def subscribeSubreddit():
	global redditObject
	userSubredditInput = input("Enter Subreddit Name: ")
	redditObject.get_subreddit(userSubredditInput).subscribe()

def unsubscribeSubreddit():
	global redditObject
	userSubredditInput = input("Enter Subreddit Name: ")
	redditObject.get_subreddit(userSubredditInput).unsubscribe()

def pullRedditFeed():
	global root, submissionListbox
	subreddit = redditObject.get_subreddit('python')
	for submission in subreddit.get_hot(limit=10):
		submissionListbox.insert(tk.END, submission.title)

def getAbout():
	print ("Insert Text")
		
root = tk.Tk()
root.title('reddit Standalone')

headerLabel = tk.Label(root, text = "Standalone Reddit Application", font=("Arial", 10), anchor=tk.W)
headerLabel.pack()

submissionListbox = tk.Listbox(root, width=200)
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




