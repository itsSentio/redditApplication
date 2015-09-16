from urllib import *
import praw

def getLogin():
	redditObject = praw.Reddit(user_agent="redditApplication")
	userName = input("Enter Username: ")
	userPass = input("Enter Password: ")
	redditObject.login(userName, userPass)

getLogin()
