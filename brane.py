import pyttsx3
import speech_recognition as sr
from datetime import *
import requests
import wikipedia
import webbrowser
import os
from tkinter import *
from tkinter import filedialog
import smtplib

engine = pyttsx3.init('sapi5')
engine.setProperty('voice',engine.getProperty('voices')[0].id)

root = Tk()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def check_Internet():
	try :
		_ = requests.get('http://www.google.com/',timeout=5)
		return True
	except requests.ConnectionError:
		speak("Sorry!! No Internet Connection Found")
		return False


def command_input() :
	r = sr.Recognizer()
	with sr.Microphone() as source :
		print('Listening....')
		r.pause_threshold = .5
		audio = r.listen(source)

	try :
		print("Recognizing....")
		query = r.recognize_google(audio,language = 'en-in')
		return str(query)
	
	except Exception as e:
		speak("Please Try Again...")
		return command_input()

def intro():
	speak("Hello Master")
	speak("I am your Presonal Assistant")
	speak("THE BRANE")
	speak("What can i do for you")

def day_today():speak('Today is'+date.today().strftime("%A"))

def time_now():
	datet = datetime.now()
	speak(str(datet.strftime("%I"))+' '+str(datet.strftime("%M"))+datet.strftime("%p"))
	
def search_wiki(query):
	speak("Searching wikipedia")
	query = query.replace("wikipedia","")
	try:
		results = wikipedia.summary(query, sentences=3)
		print('According to Wikipedia '+results)
		speak('According to Wikipedia '+results)

	except Exception as n:
		speak('No data about the topic found')

def open_page(urll):
	if(check_Internet()):
		speak('Opening Web Browser')
		webbrowser.open(urll)
		exit()


def launchr():
	speak("Which website do you want to open?")
	open_page(command_input().lower())
	exit()
	
def launchpro(pathh):
	try : 
		speak("Launching Program")
		os.startfile(pathh)
		exit()
	except Exception as e:
		speak("Unable to open the program")

def playmusic():
	os.startfile(filedialog.askopenfilename(parent=root,title='Select music file',filetypes=[("Audio Files","*.mp3")]))
	root.destroy()
	exit()


def emailSend():
	speak("What is the massage?")
	msg = command_input()
	print("Message : "+msg)
	speak("Please enter the email :")
	to = input()
	try:
		server = smtplib.SMTP(smtp.gmail.com,587)
		server.ehlo()
		server.starttls()
		server.login("youremail@gmail.com","your_password")
		server.sendmail('youremail@gmail.com',to,msg)
		server.close()
	except Exception as e:
		speak("Master I was unable to send email")

def check():
	while(check_Internet()) :
		query = command_input().lower()
		if "quit" in query :
			break
		elif "day today" in query :
			day_today()
		elif "the time" in query :
			time_now()
		elif ('search' or 'in') and "wikipedia" in query:
			search_wiki(query)
		elif ('launch' or 'open') and 'youtube' in query:
			open_page('youtube.com')
		elif ('launch' or 'open') and 'google' in query:
			open_page('google.com')
		elif ('launch' or 'open') and 'github' in query:
			open_page('github.com')
		elif ('launch' or 'open') and 'hackerrank' in query:
			open_page('hackerrank.com')
		elif ('launch' or 'open') and 'website' in query:
			launchr()
		elif ('launch' or 'open') and 'vscode' in query:
			launchpro("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
		elif 'play music' in query:
			playmusic()
		elif 'send email' in query:
			emailSend()


if __name__ == "__main__":
	intro()
	check()