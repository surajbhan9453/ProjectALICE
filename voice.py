import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import dirs 
from selenium import webdriver #chrome external window
import time
import requests  #for weather 
import subprocess   #all internal exe file
from datetime import date
import calendar

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import cv2
import face_recognition 
from simple_facerec import SimpleFacerec




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1269, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-80, -40, 1351, 751))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/wp2757874.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.pui= QLabel
        self.pui.movie = QtGui.QMovie("./UI/wp2757874.gif")
        self.label.setMovie(self.pui.movie)
        self.pui.movie.start()
            


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 1051, 191))
        font = QtGui.QFont()
        font.setFamily("Cinzel Black")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 220, 341, 291))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/123.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.pui= QLabel
        self.pui.movie = QtGui.QMovie("./UI/123.gif")
        self.label_3.setMovie(self.pui.movie)
        self.pui.movie.start()


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(950, 410, 341, 251))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/ascd.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.pui= QLabel
        self.pui.movie = QtGui.QMovie("./UI/ascd.gif")
        self.label_5.setMovie(self.pui.movie)
        self.pui.movie.start()


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 630, 1261, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/audio.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.pui= QLabel
        self.pui.movie = QtGui.QMovie("./UI/audio.gif")
        self.label_4.setMovie(self.pui.movie)
        self.pui.movie.start()
        


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ea0004;\">ALICE </span><br/><span style=\" font-size:26pt; color:#ffffff;\">(Artificial Linguistic Internet Computer Entity)</span></p></body></html>"))
import Lucyi


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
cdriver='C:\\Users\\suraj\\Downloads\\chromedriver.exe'


sst=dirs.mains
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        print("Good Morning!, Sir")
        speak("Good Morning!, Sir")

    elif hour>=12 and hour<18:
        print("Good Afternoon!, Sir.. ")   
        speak("Good Afternoon!, Sir.. ")   

    else:
        print("Good Evening!, Sir")  
        speak("Good Evening!, Sir")  

    print("I am Alice, The AI Assistant of Bhanu ... How can i help you...!  ") 
    speak("I am  Alice, The AI Assistant of, Bhaanu... How can i help you...!  ") 
    
    
     
    # print(speak)

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
                                                                                                                                                                                                                                                                                                                                                 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('surajbk@student.iul.ac.in', sst)
    server.sendmail('surajbk@student.iul.ac.in', to, content)
    server.close()

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    
    
    wishMe()
    
    cmd=1
    while cmd:
        
        query = takeCommand().lower()
        

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif (('quit' in query) or ('exit' in query) or('keep quiet' in query)or('good night'in query)):
            if'good night'in query:
                hour = int(datetime.datetime.now().hour)
                if ((hour>=21 and hour<24)or(hour>=0 and hour<=2)):
                    speak("Ok sir, Good Night.. I am always with you sir, bye, Take care..")
                    cmd=0
                else:
                    speak("No sir.. Dont make me a fool... ")
            else:
                speak("Ok sir.. i hope, i did well, bye sir, Take care..")
                cmd=0
        elif (('good morning' in query)or('good afternoon' in query)or('good evening'in query)):
            
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                print("Good Morning! sir...")
                speak("Good Morning! sir...")

            elif hour>=12 and hour<18:
               print("Good Afternoon! sir...")
               speak("Good Afternoon! sir...")
            elif hour>=18 and hour<24:
                print("Good evening sir..")      
                speak("Good evening sir..")      
        elif 'play' in query:
            
            query = query.replace("play","")
            query=query.replace("search","")
            kit.playonyt(query)
            print(f"playing, {query}")
            speak(f"playing, {query}")
            

        elif 'open google' in query:
            print("opening google....")
            speak("opening google....")
            url="http://google.com"
            #chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            webbrowser.open(url)
            
            
        elif 'google' in query:
            query = query.replace("in","")
            query = query.replace("on","")
            query = query.replace("google","")
            query=query.replace("search","")
            tab = "http://google.com/?#q="
            webbrowser.open(tab+query)
            speak("Result on your screen")

        elif 'open gmail'in query:
            speak("ok sir, opening gmail")
            webbrowser.open("www.gmail.com")
            speak("Gmail on your screen, Sir...")
            
        elif 'open facebook'  in query :
            print("opening facebook....")
            speak("opening facebook....")
            url='www.facebook.com'
            speak("Facebook on your screen, Sir...")
            webbrowser.open(url)
        
        elif 'open whatsapp' in query:
            # webbrowser.open("www.whatsappweb.com") 
            print("opening whatsapp....")
            speak("opening whatsapp....")
            url='http://web.whatsapp.com/'
            speak("Whatsapp on your screen, Sir...")
            webbrowser.open(url) 
        elif'show my last'in query:
            file = open("pywhatkit_dbs.txt","r",encoding='utf-8')
            content = file.read()
            file.close()
            if content == "--------------------":
                content = None
            print(content)
            speak(content)
            
            
             

        elif 'open control' in query:
            print("opening Control panel....")
            speak("opening Control panel....")
            subprocess.call('control.exe')
            speak("Control Panel on your screen, Sir...")
        elif 'open file' in query:
            speak("Opening File Explorer")
            subprocess.call('explorer.exe')
            speak("File explorer on your screen, Sir...")

        elif (('music' in query)or('gana'in query)):
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print("Ok Sir, Playing music....")
            speak("ok Sir, Playing music....")
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[5]))
        elif "time" in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"The Time is {strTime}")
            speak(f" the time is {strTime}")

        elif (('open visual studio' in query) or ('open vs code'in query)):
            codePath ="C:\\Users\\SBK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        

        elif 'date'in query:
            today=datetime.datetime.now()
            today1=today.strftime("%d, %B, ")
            rr=str(today.year)
            today1=today1+rr
            print("Today date is.")
            print(today1)
            speak("today date is.")
            
            speak(today1)
            

        elif'today'in query:
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                print("Good Morning! sir...")
                speak("Good Morning! sir...")               
            elif hour>=12 and hour<18:
               print("Good Afternoon! sir...")
               speak("Good Afternoon! sir...")
            elif hour>=18 and hour<24:
                print("Good evening sir..")                
                speak("Good evening sir..")
            today=datetime.datetime.now()
            today1=today.strftime("%d, %B, ")
            rr=str(today.year)
            today1=today1+rr
            print("today date is...",today1)
            speak("today date is..."+today1)             
            date = date.today()
            st=calendar.day_name[date.weekday()]
            print("today is, ",st)
            speak("today is, "+st)
        elif'day'in query:
            date = date.today()
            st=calendar.day_name[date.weekday()]
            speak("today is, "+st)
            print("today is, ",st)                  
        elif 'send email' in query:
            try:
                speak("Give the Name of Reciever.")
                dic={
 
                     "Suraj"   : "surajbk@student.iul.ac.in",
                     "Bhanu" : "bhanupsk2000@gmail.com",
                     "Diwakar" : "ds6228353@gmail.com",
                     "Ayush"  : "aymishra@student.iul.ac.in",
                     "Ajgar"   : "asgarabbas532@gmail.com",
                     "Pankaj"  : "pankajkushwaha58@gmail.com",
                     "sir" :  "surajbk@student.iul.ac.in"

                     }
                
                so=to=takeCommand()
                to=dic[to]
                speak("What should I say?")
                content = takeCommand()               
                sendEmail(to, content)
                speak(f"Email has been sent! to ,{so}, Thankyou....")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif (('who are you' in query) or ('your name' in query)):
            print('I am AI Based Alice,. i am assistant of Bhanu...  ')
            speak('I am AI Based Alice,. i am assistant of, Bhaanu....  ')

        elif 'favourite song' in query:
            speak("my favroit song is, Megenta riddim.. Do you want to play")
            query=takeCommand().lower()
            if (('yes' in query) or('yah' in query)):
              url='https://www.youtube.com/watch?v=op4B9sNGi0k'
              speak("Playing My Favorite song")
              webbrowser.open(url)  
            else:
                speak("ok sir, no problem")  
        elif 'open turbo c' in query:
            speak("opening Turbo C")
            path='C:\\TC\\BIN\\DB.EXE'
            os.startfile(path)
        
        elif 'whatsapp' in query:
            try: 
                print("Give the name of reciever")
                speak("Give the name of reciever")
                di={
                     "Suraj" : "+918707885861",
                     "Diwakar" : "+916392315371",
                     "Ayush" : "+918318363623",
                     "papa"  : "+919453485143",
                     "Ajgar"  :"+916389261613"
                     }
                number=di[takeCommand()]
            
                print("What message you want to send.")
                speak("What message you want to send.")
                whatmsg=takeCommand()
                print("Time in hour.")
                speak("Time in hour.")
                hour=int(takeCommand())
                print(hour)
                print("Time in minute.")
                speak("Time in minute.")
                minu=int(takeCommand())
                print(minu)
                kit.sendwhatmsg(number,whatmsg,hour,minu)
            except Exception as e :
                print(e)
                speak("Sorry Sir. I am not able to send this...     Try again..")
        
        elif 'close music' in query:
            os.system('taskkill /f /im vlc.exe')
        elif 'close file' in query:
            os.system('taskkill /f /im explorer.exe')
        elif 'close chrome' in query:
            os.system('taskkill /f /im chrome.exe')
        
        elif 'turn off' in query:
            speak("When pc will turning off..Give time in second..")
            shut=int(takeCommand())
            shuts=str(shut)
            os.system('shutdown -s -t '+shuts) 
            print("pc will turning off in ",shuts, " second..")
            speak("pc will turning off in "+shuts+ " second..")
            print("If you Want to Cancel Shut down, Say Cancel")
            speak("If you Want to Cancel Shut down, Say Cancel")
            
        elif 'cancel'in query:
            cont = "shutdown /a"
            os.system(cont)
            print("Ok sir,Dont worry I will not shut down your system")
            speak("Ok sir,Dont worry, I will not shut down your system")
        elif 'hello' in query:
            print("Hello sir, What can i do for you..")    
            speak("hello sir, What can i do for you..") 
           
        elif 'weather' in query:
            try:  
                api_address='http://api.openweathermap.org/data/2.5/weather?appid=248932e95581539a55245ccabc4b8e65&q='
                unit='&units=metric'
                speak("Tell me city name.")
                city=takeCommand()
                url= api_address + city+unit
                json_data= requests.get(url)

                data=json_data.json()
                temp=data['main']['temp']
                temp=str(temp)
                hum=data['main']['humidity']
                hum=str(hum)
                wind=data['wind']['speed']
                wind=wind*2
                wind=str(wind)
                vis=data['visibility']
                vis=vis/100
                vis=str(vis)
                discript=data['weather'][0]['main']
                discript=str(discript)
                     
                print("tempreature is ",temp," degree celcius..")
                speak("tempreature is "+temp+" degree celcius..")
            
                print("Humidity is ",hum," percent..")
                speak("Humidity is "+hum+" percent..")
            
                print("Speed of wind is ",wind," miles per hour..")
                speak("Speed of wind is "+wind+" miles per hour..")

                print("Discription of Visibility is ",discript)
                speak("Discription of Visibility is "+discript)
            
                print(" Visibility is ",vis," metre..")
                speak(" Visibility is "+vis+" metre..")
            except Exception as e :
                print("")
                speak("Sorry Sir. I am not able to Give you Report, Try again..")                  
              
        
        elif 'university' in query:
            try:
                speak("Opening I L I login page, Sir")
                username = [dirs.std]
                password = [dirs.mains2]
                url = 'https://ilizone.in/login/index.php'
                speak("Opening chrome...")
                driver = webdriver.Chrome(cdriver)
                driver.get(url)
                
                cd=1
                while cd:

                    speak("What can i do.. Sir")
                    query=takeCommand().lower()
                    if'account' in query:
    
                        driver.find_element_by_id('username').send_keys(username)
                        driver.find_element_by_id('password').send_keys(password)
                        speak("Username and password succesfully enterd")
                        time.sleep(1)
                        driver.find_element_by_id('loginbtn').click()
                        speak("Welcome to Integral university Portal.")
                        time.sleep(1)
                        
                        cm=1
                        while cm:
                            
                            try:
                                driver.find_element_by_xpath("//button[@aria-expanded='false']").click()
                                time.sleep(2)
                            except Exception as e :
                                print("")
                            speak("What can i do next...")
                            diff={
                                'advanced technology'  :  'https://ilizone.in/course/view.php?id=3571',
                                'source lab':  'https://ilizone.in/course/view.php?id=3572',
                                'E commerce':  'https://ilizone.in/course/view.php?id=3400',
                                'VB.net': 'https://ilizone.in/course/view.php?id=3305',
                                'source' : 'https://ilizone.in/course/view.php?id=3310',
                                'cyber law'    : 'https://ilizone.in/course/view.php?id=3315',
                                'project lab'  : 'https://ilizone.in/course/view.php?id=3569',
                                

                             }
                            try:
                                query=takeCommand().lower()
                                query=query.replace("open ","")
                                query=query.replace("Alice ","")
                                query=query.replace("hey ","")
                                query=query.replace("hello ","")
                                st=query
                                query=diff[query]
                                driver.get(query)
                                speak("ok sir, Opening "+st+" section")
                            except Exception as e :
                                if'back'in query:
                                    speak("ok sir, i am going to back")
                                    driver.back()
                                elif 'close'in query:
                                    speak("ok sir, closing window")
                                    driver.close()
                                    break
                                elif'maximize'in query:
                                    speak("ok sir, maximizing window")
                                    driver.maximize_window()
                                elif'announcements'in query:
                                    speak("Ok sir, Opening Announcements section")
                                    driver.find_element_by_xpath("//span[@class='instancename']").click()
                                elif'submit'in query:
                                    time.sleep(1)
                                    try:
                                        driver.find_element_by_link_text('Submit attendance').click()
                                        speak("ok sir,Don't worry, i will sumbit your attendance")
                                        time.sleep(1)
                                        driver.find_element_by_xpath("//input[@class='form-check-input ']").click() #<input class="form-check-input "
                                        time.sleep(1)    
                                        driver.find_element_by_xpath("//span[@data-fieldtype='submit']").click()    #<span data-fieldtype="submit"
                                        speak("Sir, Your attendance was successfully submitted...")
                                    except Exception as e :
                                        speak("Sorry sir, i can't submit your attendance right now..")
                                elif'attendance' in query:
                                    speak("ok sir, Opening Attendance section")
                                    driver.find_element_by_link_text("Attendance").click()
                                    speak("Attendance section opened successfully... ")
                                    time.sleep(2)
                                
                                elif'minimize'in query:
                                    speak("ok sir, minimizing window")
                                    driver.minimize_window()
                                else:
                                    cm=1
                        cd=0            
                    elif 'close' in query:
                        speak("Closing tab from chrome")
                        cd=0
                        driver.close()
                    elif'maximize'in query:
                        driver.maximize_window()
                        speak("Maximizing window Successfully")
                    else:
                       speak("sorry sir, your given command is not valid ")                                         
            except Exception as e :
                print("")
                speak("Sorry Sir. I am not able to Give you Report, Try again..")     

            
               
                
        elif 'face' in query:
          sfr = SimpleFacerec()
          sfr.load_encoding_images("images/")
          cap = cv2.VideoCapture(0)
          while True:
             ret, frame = cap.read()
             face_locations, face_names = sfr.detect_known_faces(frame)
             for face_loc, name in zip(face_locations, face_names):
                 y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                 cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                 cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        
             cv2.imshow("Frame", frame)
             key = cv2.waitKey(1)
             if key == 27:
                break
             try: 
                    if name == 'Bhanu':
                        speak("Hello and welcome Mr. Bhanu")
                        break
        
                    elif name == 'Shivam':
                        speak("Hello and welcome Mr. Shivam")
                        break
        
                    elif name == 'Pawan':
                        speak("Hello and welcome Mr. Pawan}")
                        break
        
                    elif name == 'Unknown':
                        speak("Unauthorised user detected, Thank you")
                        break
                        
        
             except Exception as e:
                              
                    print(e)             
cap.release()
cv2.destroyAllWindows()    #driver.find_element_by_id('span.multiline').click()
    
    
    
            
    
exit()        #speak("successfully logged into your integral learning initiative account")
sys.exit(app.exec_())        

          
