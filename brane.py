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
from email.mime.text import MIMEText


os.system('pip install pyttsx3')
os.system('pip install pipwin')
os.system('pipwin install pyaudio')
os.system('pipwin install speechrecognizer')
os.system('pip install wikidedia')
os.system('pip install tkinter')
os.system('pip install smtplib')
os.system('cls')


def datain():
    root = Tk()
    var = IntVar()
    l1 = Label(root,text="Your Name")
    name = Entry(root,width =35 , fg='red',borderwidth = 5)
    l1.grid(row=0,column=0)
    name.grid(row = 0,column = 1)
    l2= Label(root,text="Assistant Voice :")
    l2.grid(row=1,column=0)
    b1 = Radiobutton(root,text='Male',variable=var,value=0)
    b1.grid(row=1,column=1)
    b2 = Radiobutton(root,text='Female',variable=var,value=1)
    b2.grid(row=3,column=1)
    Button(root,text="Submit",fg='red',padx=40,borderwidth=5,command=lambda:getval(root,var,name)).grid(row=4,column=1)
    root.mainloop()


def getval(root,var,name):
    a=var.get()
    b=name.get()
    if b!="":
        open('logs','w+').write(str(a)+"\n"+b)
        root.quit()

try:
	l = open("Logs",'r').readlines()
except Exception as e:
	datain()
	l = open("Logs",'r').readlines()
	username=l[1]
	av=int(l[0])

if len(l)==2:
	username=l[1]
	av=int(l[0])
else:
	datain()
	l = open("Logs",'r').readlines()
	username=l[1]
	av=int(l[0])


engine = pyttsx3.init('sapi5')
engine.setProperty('voice',engine.getProperty('voices')[av].id)


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


class email:
    def __init__(self):
        self.sender=""
        self.receiver=""
        self.password=""

    def val(self,root,sender,receiver,password):
        self.sender = sender.get()
        self.receiver = receiver.get()
        self.password = password.get()
        if  self.sender != "" and self.receiver != "" and self.password != "":
            root.quit()
            self.procedure()

    def procedure(self):
        speak("What message do you want to send")
        body = command_input()
        msg = MIMEText( body )
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Subject'] = "Automatic Mail"
        try:
            server = smtplib.SMTP(smtp.gmail.com,587)
            server.starttls()
            server.login(self.send,self.password)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            speak("Master I was unable to send email")
    
    def display(self):
        root = Tk()
        l1 = Label(root,text="from : ")
        sender = Entry(root,width =35 , fg='red',borderwidth = 5)

        l2 = Label(root,text="to : ")
        receiver = Entry(root,width =35 , fg='red',borderwidth = 5)
        
        l3 = Label(root,text="password : ")
        password = Entry(root,width =35 , fg='red',show='*',borderwidth = 5)
        
        l1.grid(row=0,column=0)
        l2.grid(row=1,column=0)
        l3.grid(row=2,column=0)

        sender.grid(row = 0,column = 1)
        receiver.grid(row = 1,column = 1)
        password.grid(row = 2,column = 1)
    
        b1 = Button(root,text='Send',command = lambda : self.val(root,sender,receiver,password),padx=40)
        b1.grid(row=3,column=1)
        
        root.mainloop()


def makeNote():
	note = open("NOTE.log",'w')
	speak("What do want to note")
	str = command_input()
	note.write(str)
	speak("nOTE SAVED")
		

def viewNote():
	try :
		note = open("NOTE.log",'r')
		speak("The note reads")
		for line in note:
			speak(line)
	except Exception as e:
		speak("No notes found.You have to create some")


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
			email().display()
		elif 'view note' in query:
			viewNote()
		elif ('make' or 'write') and 'note' in query:
			makeNote()


def intro():
	speak("Hello Master "+username)
	speak("I am your Presonal Assistant")
	speak("THE BRANE")
	speak("What can i do for you")
		

if __name__ == "__main__":
	intro()
	check()
