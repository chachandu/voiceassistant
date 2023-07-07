import pyttsx3
import datetime
import speech_recognition as sr
import smtplib 
# from secrets_1 import senderemail, epwd, to  
import pyautogui
import webbrowser as web
from time import sleep 
import wikipedia 
import pywhatkit
import requests
# from newsapi import NewsApiClient
import clipboard
import os
import time as tt
from nltk.tokenize import word_tokenize
import openai
from time import sleep

from newvoices import speak

openai.api_key = "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"


engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

def time():
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        speak("The current time is :")
        speak(Time)

def date():
      year = int(datetime.datetime.now().year)
      month = int(datetime.datetime.now().month)
      date = int(datetime.datetime.now().day)
      speak(date)
      speak(month)
      speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning sir!")
    elif hour >= 12 and hour <18:
        speak("good afternoonn sir!")
    elif hour >= 18 and hour <24:
        speak("good evening sir!")
    else:
        speak("good night sir!")

def wishme():
    speak("Alexa Here")

def takeCommandCMD():
     query = input("please tell me how can i help you\n")
     return query

def takeCommandMIC():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening.....")
          r.pause_threshold = 1
          audio = r.listen(source)
     try :
          print("recognising..")
          query = r.recognize_google(audio, language="en-IN")
          print("User said : "+query)     
     except Exception as e:
        print(e)
        speak("Say that again please....")
        return "none"
        
     return query

def screenshot():
     name_img = tt.time()
     name_img = f'C:\\Users\\user\\Videos\\voice assistant{name_img}.png'.format(name_img)
     img = pyautogui.screenshot(name_img)
     img.show()


# def sendEmail():
#      server = smtplib.SMTP('smtp.gmail.com', 587)
#      server.starttls()
#      server.login(senderemail, epwd,) 
#      server.sendemail(senderemail, to, 'hello this is a test email by jarvis')
#      server.close()  

def sendwhatsmsg(phone_no, message):
     Message = message
     web.open('http://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
     sleep(10)
     pyautogui.press('enter')

def searchgoogle():
     speak('what should I search for:')
     search = takeCommandMIC()
     web.open('https://www.google.com/search?q='+search)

def text2speech():
     text = clipboard.paste()
     speak(text) 


# def news():
#      newsapi = NewsApiClient(api_key='cd759cad7e3b4125a750fbb361e9917b')
#      data = newsapi.get_top_headlines(q='facebook',
#                                       language='en',
#                                       page_size=5)
     
#      newsdata = data['articles']
#      for x,y in enumerate(newsdata):
#           print(f'{x}{y["description"]}')
#           speak((f'{x}{y["description"]}'))
          
#      speak("thats it for now i'll update you in some time")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ", 

def gpt_output(prompt):
   response = openai.Completion.create(
   model="text-davinci-003",
   prompt=prompt,
   temperature=0.9,
   max_tokens=150,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0.6,
   stop=[" Human:", " AI:"]
   )
   data = response.choices[0].text
   print(data)
   speak(data)
   

if  __name__ == "__main__":
     wishme()
     wakeword = "Alexa"
     while True:
          query = takeCommandMIC().lower()
          query1 = query
          query = word_tokenize(query)
          # print(query)
          if wakeword in query:
               if 'time' in query:
                    time()
               elif 'date' in query:
                    date()
               elif 'message' in query:
                    user_name = {
                         'Abu': '+91 92070 90976'
                    }
                    try:
                         speak("to whom you want to send the whatsapp message?")
                         name = takeCommandMIC()
                         phone_no = user_name[name]
                         speak("what is the message?")
                         message = takeCommandMIC()
                         sendwhatsmsg(phone_no,message)
                         speak("message has been send")
                    except Exception as e:
                         print(e)
                         speak("unable to send the message")

               elif 'wikipedia' in query:
                    speak('searching...on wikipedia..')
                    query = query.replace("wikipedia", "")
                    result = wikipedia.summary(query, sentences = 2)
                    # print(result)
                    speak(result)

               elif 'google' in query:
                    searchgoogle()

               elif 'youtube' in query:
                    speak("what should i search in youtube?")
                    topic = takeCommandMIC()
                    pywhatkit.playonyt(topic)
                    quit()
               
               elif 'thank you' in query:
                    speak("your welcome sir")
               

               # elif 'news' in query:
               #      news()
               elif 'Alexa do you remember anything' in query:
                    remember = open('data.txt','r')
                    speak("you told me to remember that"+remember.read())

               elif 'open file explorer' in query:
                    # speak("which file to open")
                    # file17 = takeCommandMIC()
                    os.system('explorer C://{}'.format(query.replace('open','')))

               elif 'screenshot' in query:
                    screenshot()

               elif 'remember' in query:
                    speak("what should i remember sir?")
                    data = takeCommandMIC()
                    speak("you said me to remember that"+data)
                    remember = open('data.txt','w')
                    remember.write(data)
                    remember.close()

               # elif 'weather' in query:
               #      url = 'http://api.openweathermap.org/data/2.5/weather?>q={Kollam, IN}&units=imperial&appid={7aa8d0ff1452373d76faa528edab148d}'
                    
               #      res = requests.get(url)
               #      data = res.json()

               #      weather = data['weather'] [0] ['main']
               #      temp = data['main']['temp']
               #      desp = data['weather'] [0] ['description']
               #      print(weather)
               #      print(temp)
               #      print(desp)

               elif 'read' in query:
                    text2speech()

               elif 'offline' in query:
                    quit()

               else:
                    gpt_output(query1)

