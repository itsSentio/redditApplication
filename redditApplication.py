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
	global loginNotFinished, userName, userPass
	loginNotFinished = False
	redditObject.login(userName.get(), userPass.get())

def getLogin():
	global redditObject, root, loginNotFinished, userName, userPass
	loginWindow = tk.Toplevel(root)
	while loginNotFinished:
		tk.Label(loginWindow, text="Username").grid(row=0)
		tk.Label(loginWindow, text="Password").grid(row=1)
		userName = tk.Entry(loginWindow)
		userPass = tk.Entry(loginWindow)
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
	for submission in subreddit.get_hot(limit=5):
		submissionListbox.insert(tk.END, submission.title)

		
root = tk.Tk()
root.title('reddit Standalone')

headerLabel = tk.Label(root, text = "Standalone Reddit Application", font=("Arial", 10), anchor=tk.W)
headerLabel.pack()

submissionListbox = tk.Listbox(root, width=200)
submissionListbox.pack()

buttonFrame = tk.Frame(root, width = 200)
buttonFrame.pack()

try:
	userLabel = tk.Label(buttonFrame, text = "Currently logged: " + userName, font=("Arial", 10), anchor=tk.W)
	userLabel.pack(side = tk.BOTTOM)
except NameError:
	userLabel = tk.Label(buttonFrame, text = "Currently logged: None", font=("Arial", 10), anchor=tk.W)
	userLabel.pack(side = tk.BOTTOM)
else:
	userLabel = tk.Label(buttonFrame, text = "Currently logged: " + userName, font=("Arial", 10), anchor=tk.W)
	userLabel.pack(side = tk.BOTTOM)

loginButton = tk.Button(buttonFrame, text="Login", command = getLogin)
loginButton.pack(side = tk.LEFT)

getFeedButton = tk.Button(buttonFrame, text="Check Feed", command = pullRedditFeed)
getFeedButton.pack(side = tk.LEFT)

root.mainloop()




