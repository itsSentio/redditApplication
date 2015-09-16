from urllib import *
import praw
from pprint import pprint

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
	redditFeed = redditObject.get_subreddit('python').get_hot(limit=5)
	pprint ([str(x) for x in redditFeed])

root = tk.Tk()

loginButton = tk.Button(root, text="Login", command = getLogin)
loginButton.pack()

getFeedButton = tk.Button(root, text="Check Feed", command = pullRedditFeed)
getFeedButton.pack()


root.mainloop()




