from word2number import w2n
import pyttsx3
#from datetime import date, time
import pickle
import os
import pyaudio
import speech_recognition as sr

text_speech = pyttsx3.init()
data = {}
r = sr.Recognizer()
m = sr.Microphone()

def say(message):
    print("spoken output: " + message)

def listen():
    with m as source:
        audio = r.listen(source).lower()

# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
#
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

def listen_for_number(lower=1, upper=4):
    while True:
        words = listen()
        if words.isdigit():
            if int(words) >= lower and int(words) <= upper:
                return int(words)
        elif w2n.word_to_num(words) >= lower and w2n.word_to_num(words) <= upper:
            return int(w2n.word_to_num(words))
        text_speech.say("please say a number between " + str(lower) + " and " + str(upper))
        text_speech.runAndWait()

def listen_for_boolean():
    while True:
        words = listen()
        if words == "yes":
            return True
        elif words == "no":
            return False
        else:
            text_speech.say("please answer with a yes or a no")
            text_speech.runAndWait()

def greet(data):
    if "name" in data:
        text_speech.say("Hello " + data["name"])
        text_speech.runAndWait()
    else:
        try:
            #text_speech.say("Hello, would you like to participate in the quiz?")
            #text_speech.runAndWait()
            text_speech.say("Before we get started, i'll need some basic information")
            text_speech.runAndWait()
            text_speech.say("what is your first name?")
            text_speech.runAndWait()
            with m as source: data["name"] = r.listen(source)
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(data)

                print("You said {}".format(value))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            text_speech.say("nice to meet you, " + data["name"])
            text_speech.runAndWait()
        except KeyboardInterrupt:
            pass

class questionClass:
    pass


question1 = questionClass()
question1.question = "What day did Franklin D. Roosevelt Die?" #April 12, 1945
question1.answer1 = "1. April 12, 1945"
question1.answer2 = "2. April 15, 1945"
question1.answer3 = "3. March 30, 1945"
question1.answer4 = "4. April 10, 1945"
question1.correctAnswer = 1

question2 = questionClass()
question2.question = "In what year did child labor laws start in the United States?" #1938
question2.answer1 = "1. 1952"
question2.answer2 = "2. 1938"
question2.answer3 = "3. 1945"
question2.answer4 = "4. 1923"
question2.correctAnswer = 2

# question3 = questionClass()
# question3.question = "When was the Battle of Gettysburg fought during the Civil War?" #July 1 through July 3, 1863
# question3.answer1 = "1. July 5 through July 7, 1863"
# question3.answer2 = "2. June 1 through June 3, 1863"
# question3.answer3 = "3. July 4 through July 8, 1863"
# question3.answer4 = "4. July 1 through July 3, 1863"
# question3.correctAnswer = 4
#
# question4 = questionClass()
# question4.question = "Who was the first ruler of the Mongol Empire?" #Genghis Khan
# question4.answer1 = "1. Tolui Khan"
# question4.answer2 = "2. Genghis Khan"
# question4.answer3 = "3. Güyük Khan"
# question4.answer4 = "4. Möngke Khan"
# question4.correctAnswer = 2
#
# question5 = questionClass()
# question5.question = "What year did the North American Free Trade Agreement (NAFTA) go into effect?" #1994
# question5.answer1 = "1. 1994"
# question5.answer2 = "2. 1995"
# question5.answer3 = "3. 1993"
# question5.answer4 = "4. 1990"
# question5.correctAnswer = 1
#
# question6 = questionClass()
# question6.question = "In what year is the Bubonic Plague believed to have started in Europe and Asia?" #1346
# question6.answer1 = "1. 1358"
# question6.answer2 = "2. 1337"
# question6.answer3 = "3. 1346"
# question6.answer4 = "4. 1325"
# question6.correctAnswer = 3
#
# question7 = questionClass()
# question7.question = "What was the name of the Ukrainian nuclear power plant that was the site of a nuclear disaster in April 1986?" #Chernobyl
# question7.answer1 = "1. Bezhetsk"
# question7.answer2 = "2. Chernobyl"
# question7.answer3 = "3. Gusinoozyorsk"
# question7.answer4 = "4. Chernogolovka"
# question7.correctAnswer = 2
#
# question8 = questionClass()
# question8.question = "Who was the first Emperor of Rome?" #Augustus
# question8.answer1 = "1. Julius Caesar"
# question8.answer2 = "2. Arcadius"
# question8.answer3 = "3. Maximinus I"
# question8.answer4 = "4. Augustus"
# question8.correctAnswer = 4
#
# question9 = questionClass()
# question9.question = "What year was Nelson Mandela freed from prison?" #1990
# question9.answer1 = "1. 1991"
# question9.answer2 = "2. 1992"
# question9.answer3 = "3. 1990"
# question9.answer4 = "4. 1989"
# question9.correctAnswer = 3
#
# question10 = questionClass()
# question10.question = "How many years did the 100 years war last?" #116 years
# question10.answer1 = "1. 116 years"
# question10.answer2 = "2. 100 years"
# question10.answer3 = "3. 101 years"
# question10.answer4 = "4. 103 years"
# question10.correctAnswer = 1

#Game Start
greet(data)
#time.sleep(5)

userScore = 0

#question 1
text_speech.say(question1.question)
text_speech.runAndWait()
text_speech.say(question1.answer1)
text_speech.runAndWait()
text_speech.say(question1.answer2)
text_speech.runAndWait()
text_speech.say(question1.answer3)
text_speech.runAndWait()
text_speech.say(question1.answer4)
text_speech.runAndWait()
text_speech.say("Say your answer as a number ")
text_speech.runAndWait()

# ans1 = sr.listen_for_number(1, 4)
try:
    with m as source: data["ans1"] = r.listen(source)
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(data)

        print("You said {}".format(value))
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    text_speech.say("nice to meet you, " + data["name"])
    text_speech.runAndWait()
except KeyboardInterrupt:
    pass


if data["ans1"] == 1:
    userScore += 1
    text_speech.say("Correct!")
    text_speech.runAndWait()
else:
    text_speech.say("Incorrect!")
    text_speech.runAndWait()


text_speech.say("You're score is now: " + userScore)
text_speech.runAndWait()
text_speech.say("Lets move onto the next question")
text_speech.runAndWait()
#time.sleep(3)

#question 2
text_speech.say(question2.question)
text_speech.runAndWait()
text_speech.say(question2.answer1)
text_speech.runAndWait()
text_speech.say(question2.answer2)
text_speech.runAndWait()
text_speech.say(question2.answer3)
text_speech.runAndWait()
text_speech.say(question2.answer4)
text_speech.runAndWait()
text_speech.say("Say your answer as a number ")
text_speech.runAndWait()

# ans2 = sr.listen_for_number(1, 4)
try:
    with m as source: data["ans2"] = r.listen(source)
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(data)

        print("You said {}".format(value))
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    text_speech.say("nice to meet you, " + data["name"])
    text_speech.runAndWait()
except KeyboardInterrupt:
    pass

if data["ans2"] == 2:
    userScore += 1
    text_speech.say("Correct!")
    text_speech.runAndWait()
else:
    text_speech.say("Incorrect!")
    text_speech.runAndWait()


text_speech.say("You're score is now: " + userScore)
text_speech.runAndWait()
text_speech.say("Lets move onto the next question")
text_speech.runAndWait()
#time.sleep(3)

# #question 3
# print(question3.question)
# print()
# print(question3.answer1)
# print(question3.answer2)
# print(question3.answer3)
# print(question3.answer4)
# print()
# print("Enter your answer as a number ")
#
# ans3 = int(input())
#
#
# if ans3 == 4:
#     userScore += 1
#     print("Correct!")
# else:
#     print("Incorrect!")
#
#
# print("You're score is now: ", userScore)
# print("Lets move onto the next question")
# print()
# time.sleep(3)
#
# #question 4
# print(question4.question)
# print()
# print(question4.answer1)
# print(question4.answer2)
# print(question4.answer3)
# print(question4.answer4)
# print()
# print("Enter your answer as a number ")
#
# ans4 = int(input())
#
#
# if ans4 == 2:
#     userScore += 1
#     print("Correct!")
# else:
#     print("Incorrect!")
#
#
# print("You're score is now: ", userScore)
# print("Lets move onto the next question")
# print()
# time.sleep(3)
#
# #question 5
# print(question5.question)
# print()
# print(question5.answer1)
# print(question5.answer2)
# print(question5.answer3)
# print(question5.answer4)
# print()
# print("Enter your answer as a number ")
#
# ans5 = int(input())
#
#
# if ans5 == 1:
#     userScore += 1
#     print("Correct!")
# else:
#     print("Incorrect!")
#
#
# print("You're score is now: ", userScore)
# print("Lets move onto the next question")
# print()
# time.sleep(3)
#
# #question 6
# print(question6.question)
# print()
# print(question6.answer1)
# print(question6.answer2)
# print(question6.answer3)
# print(question6.answer4)
# print()
# print("Enter your answer as a number ")
#
# ans6 = int(input())
#
#
# if ans6 == 3:
#     userScore += 1
#     print("Correct!")
# else:
#     print("Incorrect!")
#
#
# print("You're score is now: ", userScore)
# print("Lets move onto the next question")
# print()
# time.sleep(3)
#
# #question 7
# print(question7.question)
# print()
# print(question7.answer1)
# print(question7.answer2)
# print(question7.answer3)
# print(question7.answer4)
# print()
# print("Enter your answer as a number ")
#
# ans7 = int(input())
#
#
# if ans7 == 2:
#     userScore += 1
#     print("Correct!")
# else:
#     print("Incorrect!")
#
#
# print("You're score is now: ", userScore)
# print("Lets move onto the next question")
# print()
# time.sleep(3)
#
# #question 8
# print(question8.question)
# print()
# print(question8.answer1)
# print(question8.answer2)
# print(question8.answer3)
# print(question8.answer4)
# print()
# print("Enter your answer as a number ")
#
# ans8 = int(input())
#
#
# if ans8 == 4:
#     userScore += 1
#     print("Correct!")
# else:
#     print("Incorrect!")
#
#
# print("You're score is now: ", userScore)
# print("Lets move onto the next question")
# print()
# time.sleep(3)
#
# #question 9
# print(question9.question)
# print()
# print(question9.answer1)
# print(question9.answer2)
# print(question9.answer3)
# print(question9.answer4)
# print()
# print("Enter your answer as a number ")
#
# ans9 = int(input())
#
#
# if ans9 == 3:
#     userScore += 1
#     print("Correct!")
# else:
#     print("Incorrect!")
#
#
# print("You're score is now: ", userScore)
# print("Lets move onto the next question")
# print()
# time.sleep(3)
#
# #question 10
# print(question10.question)
# print()
# print(question10.answer1)
# print(question10.answer2)
# print(question10.answer3)
# print(question10.answer4)
# print()
# print("Enter your answer as a number ")
#
# ans10 = int(input())
#
#
# if ans10 == 1:
#     userScore += 1
#     print("Correct!")
# else:
#     print("Incorrect!")
#
#
# print("That is the final question")
# print("Calculating final score")
# print()
# time.sleep(5)
#
# userScorePercent = userScore * 10


text_speech.say("Thank you for playing")
text_speech.runAndWait()
text_speech.say("you're final score is " + userScore + "/ 10 ")
text_speech.runAndWait()