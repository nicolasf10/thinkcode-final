import pyttsx3
import speech_recognition as sr
import datetime
import random
import speedtest
import re
import webbrowser
import wikipedia
import json
# installing PyAudio is also necessary with 'pip install pyaudio'

from mathOperations import math_speech
from quizMaker import Quiz

class AI:
    def __init__(self):
        self.name = "AI"
        self.user_name = None

        # reading the content from repliesdata.json into a python dictionary
        f = open('repliesdata.json')
        self.data = json.load(f)

    def speak(self, audio):
        # getting a reference to a pyttsx3.Engine instance.
        engine = pyttsx3.init()
        # retrieving  the current value of engine property
        voices = engine.getProperty('voices')

        # setting voice to male
        engine.setProperty('voice', voices[0].id)

        # Method speaks the audio
        engine.say(audio)

        # Blocks while processing queued commands, necessary for hearing audio
        engine.runAndWait()

    def take_query(self, type):
        # Running forever until user says goodbye (or similar)
        while (True):
            # This class is responsible for converting audio into text
            r = sr.Recognizer()

            # using the Microphone module from sr that will listen for a query
            with sr.Microphone() as source:
                # Energy threshold of 300 is recommended by SpeechRecognition's documentation (loudness of the file)
                r.energy_threshold = 300

                # How long it will wait after the user stops talking to consider the end of a sentence
                r.pause_threshold = 0.7
                audio = r.listen(source)

                # Now trying to use Google Recognizer function that uses Google’s free web search API
                # This try except block will check if the words are recognized, else an exception will be handled
                try:
                    print("Processing...")

                    instruction = r.recognize_google(audio, language="en-in")

                    print("You said: ", instruction)

                    if type == 'normal':
                        if self.user_name == None:
                            try:
                                self.user_name = re.search("my name is (.*)", instruction)[1]
                            except:
                                pass
                        else:
                            try:
                                self.user_name = re.search("my name is (\d*)", instruction)[1]
                            except:
                                pass


                        # Looking for trigger words
                        if "bye" in instruction or "see you later" in instruction or "need to run" in instruction or "got to run" in instruction or "got to go" in instruction or "catch you later" in instruction:
                            goodbye_call = self.data["goodbyes"][str(random.randint(0, len(self.data["goodbyes"]) - 1))]
                            print(goodbye_call)
                            self.speak(goodbye_call)
                            exit()
                        elif "my name is" in instruction:
                            print("Greetings, {}".format(self.user_name))
                            self.speak("Greetings, {}".format(self.user_name))
                        elif "how are you" in instruction or "how's it going" in instruction or "what's up" in instruction:
                            if self.user_name == None:
                                print("I am doing great, and you?")
                                self.speak("I am doing great, and you?")
                            else:
                                print("I am doing great, and you {}?".format(self.user_name))
                                self.speak("I am doing great, and you {}?".format(self.user_name))
                        elif "time" in instruction:
                            self.tell_time()
                        elif "date" in instruction or " day" in instruction:
                            self.tell_date()
                        elif "who are you" in instruction or "what is your" in instruction:
                            print("I'm Cole, your virtual assistant for programming.")
                            self.speak("I'm Cole, your virtual assistant for programming.")
                        elif "don't" in instruction or "do not" in instruction:
                            print("Okay, I will not do so.")
                            self.speak("Okay, I will not do so.")
                        elif "marry me" in instruction and 'sudo' not in instruction:
                            self.speak("I'm sorry, I can only accept such requests from the super user.")
                        elif "sudo" in instruction and "marry me" in instruction:
                            self.speak("Of course super user! I'll be glad to spend my life with you!")
                        elif "joke" in instruction:
                            self.tell_joke()
                        elif "Wi-Fi" in instruction or "internet" in instruction or "ping" in instruction:
                            self.tell_wifi_speed()
                        elif "how old are you" in instruction:
                            self.speak("I may be just a few weeks old, but I certainly do a lot more than others of my age.")
                        elif "documentation for" in instruction:
                            try:
                                technology_doc = re.search("documentation for (.*)", instruction)[1]
                                self.open_documentation(technology_doc)
                            except:
                                print("Please specify which documentation you need.")
                                self.speak("Please specify which documentation you need.")
                        elif "hey" in instruction or "hello" in instruction or "hi" in instruction:
                            hello_call = self.data["hellos"][str(random.randint(0, len(self.data["hellos"]) - 1))]
                            print(hello_call)
                            self.speak(hello_call)
                        elif "prime number" in instruction or "cosine" in instruction or "tangent" in instruction or "sine" in instruction or "√" in instruction or "square root" in instruction or "+" in instruction or "/" in instruction or "*" in instruction or "-" in instruction:
                            try:
                                math_operation = re.search("(what is )?(the )?(.*)", instruction.lower())[3]
                                math_results = math_speech(math_operation)
                                print(str(math_results))
                                self.speak(str(math_results))
                            except:
                                print("Please tell me what mathematical equation you want to perform.")
                                self.speak("Please tell me what mathematical equation you want to perform.")
                        elif "git cheat" in instruction:
                            print("Opening git cheat-sheet")
                            self.speak("Opening git cheat-sheet")
                            webbrowser.open_new_tab("https://training.github.com/downloads/github-git-cheat-sheet.pdf")
                        elif "search stack overflow for" in instruction.lower() or "search stackoverflow for" in instruction.lower():
                            try:
                                search_words = re.search("search stack overflow for (.*)", instruction.lower())[1]
                                print("Searching stackoverflow for ", search_words)
                                self.speak("Searching stackoverflow for {}".format(search_words))
                                webbrowser.open_new_tab(
                                    "https://stackoverflow.com/search?q={}".format(search_words.replace(' ', '+')))
                            except:
                                try:
                                    search_words = re.search("search stackoverflow for (.*)", instruction.lower())[1]
                                    print("Searching stackoverflow for ", search_words)
                                    self.speak("Searching stackoverflow for {}".format(search_words))
                                    webbrowser.open_new_tab(
                                        "https://stackoverflow.com/search?q={}".format(search_words.replace(' ', '+')))
                                except:
                                    print("Please tell me what you want to search for.")
                                    self.speak("Please tell me what you want to search for.")
                        elif "search stack overflow" in instruction.lower() or "search stackoverflow" in instruction.lower():
                            try:
                                search_words = re.search("search stack overflow (.*)", instruction.lower())[1]
                                print("Searching Stackoverflow for ", search_words)
                                self.speak("Searching Stackoverflow for {}".format(search_words))
                                webbrowser.open_new_tab(
                                    "https://stackoverflow.com/search?q={}".format(search_words.replace(' ', '+')))
                            except:
                                try:
                                    search_words = re.search("search stackoverflow (.*)", instruction.lower())[1]
                                    print("Searching Stackoverflow for ", search_words)
                                    self.speak("Searching Stackoverflow for {}".format(search_words))
                                    webbrowser.open_new_tab(
                                        "https://stackoverflow.com/search?q={}".format(search_words.replace(' ', '+')))
                                except:
                                    print("Please tell me what you want to search for.")
                                    self.speak("Please tell me what you want to search for.")
                        elif "search youtube for" in instruction.lower():
                            try:
                                search_words = re.search("search youtube for (.*)", instruction.lower())[1]
                                print("Searching YouTube for ", search_words)
                                self.speak("Searching YouTube for {}".format(search_words))
                                webbrowser.open_new_tab(
                                    "https://www.youtube.com/results?search_query={}".format(search_words.replace(' ', '+')))
                            except:
                                print("Please tell me what you want to search for.")
                                self.speak("Please tell me what you want to search for.")
                        elif "search youtube" in instruction.lower():
                            try:
                                search_words = re.search("search youtube (.*)", instruction.lower())[1]
                                print("Searching YouTube for ", search_words)
                                self.speak("Searching YouTube for {}".format(search_words))
                                webbrowser.open_new_tab(
                                    "https://www.youtube.com/results?search_query={}".format(search_words.replace(' ', '+')))
                            except:
                                print("Please tell me what you want to search for.")
                                self.speak("Please tell me what you want to search for.")
                        elif "search for" in instruction:
                            try:
                                search_words = re.search("search for (.*)", instruction)[1].lower()
                                print("Searching for ", search_words)
                                self.speak("Searching for {}".format(search_words))
                                webbrowser.open_new_tab(
                                    "http://www.google.com/search?q={}".format(search_words.replace(' ', '+')))
                            except:
                                print("Please tell me what you want to search for.")
                                self.speak("Please tell me what you want to search for.")
                        elif "I'm great" in instruction or "I'm okay" in instruction or "I'm good" in instruction:
                            print("Glad to hear!")
                            self.speak("Glad to hear!")
                        elif "I'm not great" in instruction or "I'm not okay" in instruction or "I'm not good" in instruction:
                            print("I'm sorry to hear.")
                            self.speak("I'm sorry to hear.")
                        elif "open" in instruction:
                            page = re.search("open (.*)", instruction)[1]
                            self.open_page(page.lower())
                        elif "what is" in instruction:
                            try:
                                search_query = re.search("what is (.*)", instruction)[1]
                                self.wikipedia_search(search_query)
                            except:
                                print("Please specify what you want to know about.")
                                self.speak("Please specify what you want to know about.")
                        elif "who is" in instruction:
                            try:
                                search_query = re.search("who is (.*)", instruction)[1]
                                self.wikipedia_search(search_query)
                            except:
                                print("Please specify who you want to know about.")
                                self.speak("Please specify who you want to know about.")
                        elif "quiz me on" in instruction:
                            try:
                                quiz_topic = re.search("quiz me on (.*)", instruction)[1]
                                print(f"Now quizzing you on {quiz_topic}")
                                self.speak(f"Now quizzing you on {quiz_topic}")
                                self.quiz(quiz_topic)
                            except:
                                print("Please provide the topic of the quiz.")
                                self.speak("Please provide the topic of the quiz.")
                        elif "new note" in instruction:
                            try:
                                self.takeNote()
                            except:
                                print("Unfortunately I was unable to create a new note.")
                                self.speak("Unfortunately I was unable to create a new note.")
                        else:
                            print("I'm sorry, I don't understand. Maybe reference my commands reference for help or speak more clearly.")
                            self.speak("I'm sorry, I don't understand. Maybe reference my commands reference for help or speak more clearly.")

                    elif type == 'joke' or type == 'quiz' or 'note':
                        return instruction

                except Exception as error:
                    print(error)
                    print("Please repeat.")
                    self.speak("Please repeat")
                    return "None"

                return instruction

    # Tasks
    def tell_time(self):
        # Return will be as such: 2021-01-05 14:26:17.705949
        time = str(datetime.datetime.now())
        hour = time[11:13]
        min = time[14:16]
        print(time)
        self.speak("The time is " + hour + "Hours and" + min + "Minutes")

    def tell_date(self):
        # Return will be as such: 2021-01-05 14:26:17.705949
        date = str(datetime.datetime.now())

        month_number = int(date[5:7].lstrip('0'))
        day_number = int(date[8:10].lstrip('0'))
        year = date[:4]


        date_speech = "Today is the {} of {} of {}.".format(self.data["days"][str(day_number)], self.data["months"][str(month_number)], year)
        print(date_speech)
        self.speak(date_speech)

    def tell_joke(self):
        jokes = self.data["jokes"]
        joke = jokes[str(random.randint(0, len(self.data["jokes"]) - 1))]

        if type(joke) is dict:
            joke_question = joke['question']
            joke_answer = joke['answer']

            print(joke_question)
            self.speak(joke_question)

            print("Listening...")
            user_answer = self.take_query('joke').lower()

            if user_answer.replace('.', '').replace(',', '').replace("'", "") == joke_answer.lower().replace('.', '').replace(',', '').replace("'", ""):
                print("Exactly. Hehe, that's a good one!")
                self.speak("Exactly. Hehe, that's a good one!")
            else:
                print("Not quite. {}".format(joke_answer))
                self.speak("Not quite. {}".format(joke_answer))
        else:
            print(joke)
            self.speak(joke)

    def tell_wifi_speed(self):
        print("Testing speed...")

        st = speedtest.Speedtest()

        # Dividing by 1e+6 to convert to megabytes
        download_speed = int(st.download() / 1000000)
        upload_speed = int(st.upload() / 1000000)

        servers = []
        st.get_servers(servers)
        ping = st.results.ping

        print("Download speed: ", download_speed)
        print("Upload speed: ", upload_speed)
        print("Ping: ", ping)

        self.speak("Your download speed is about {} megabytes. Upload speed is about {} megabytes. Ping is {}".format(download_speed, upload_speed, ping))

    def open_documentation(self, tech):
        print("Opening documentation for {}".format(tech))
        self.speak("Opening documentation for {}".format(tech))
        webbrowser.open_new_tab("https://devdocs.io/{}/".format(tech.lower()))

    def open_page(self, page):
        try:
            print("Opening {}".format(page))
            self.speak("Opening {}".format(page))
            webbrowser.open_new_tab(self.data.pages[page])
        except:
            print("Unfortunately I can't open {} yet. Open command references for available options.".format(page))
            self.speak("Unfortunately I can't open {} yet. Open command references for available options.".format(page))

    def wikipedia_search(self, query):
        try:
            summary_result = wikipedia.summary(query, sentences=1)
            print(summary_result)
            self.speak(summary_result)
        except:
            print("Unfortunately I wasn't able to retrieve this information.")
            self.speak("Unfortunately I wasn't able to retrieve this information.")

    def quiz(self, quiz_topic):
        try:
            print("Preparing the quiz.")
            self.speak("Preparing the quiz.")
            # Creating an instance of the class Quiz
            quiz_maker = Quiz(quiz_topic)

            # Storing the quiz (in Dict format) in the variable quiz_questions
            quiz_questions = quiz_maker.produce_questions()

            # If quizMaker was unable to produce a quiz
            if quiz_questions == None: raise ValueError

            # Player score
            player_score = 0

            print(f"Fill in the blank for the following {len(quiz_questions)} questions. If you wish to leave the quiz, just say 'leave quiz'")
            self.speak(f"Fill in the blank for the following {len(quiz_questions)} questions. If you wish to leave the quiz, just say 'leave quiz'")

            # looping over all questions and asking the player for the answer
            for q in quiz_questions.values():
                print(q["question"])
                self.speak(q["question"])
                print("Listening...")


                # asking the user for the correct fill in the blank word
                user_answer = ai.take_query('quiz')

                # checking to see if the player wishes to leave the quiz
                if user_answer == 'leave quiz':
                    return None

                if user_answer.lower() == q["answer"].lower():
                    player_score += 1
                    quiz_praise = self.data["quiz_praise"][str(random.randint(0, len(self.data["quiz_praise"]) - 1))]
                    print(quiz_praise)
                    self.speak(quiz_praise)
                else:
                    quiz_mistake = self.data["quiz_mistake"][str(random.randint(0, len(self.data["quiz_mistake"]) - 1))]
                    print(f"{quiz_mistake}. The answer was {q['answer']}")
                    self.speak(f"{quiz_mistake}. The answer was {q['answer']}")
            
            if player_score / len(quiz_questions) > 0.5:
                print(f"Great job! Your score was {player_score} out of {len(quiz_questions)}")
                self.speak(f"Great job! Your score was {player_score} out of {len(quiz_questions)}")
            elif player_score / len(quiz_questions) == 0.5:
                print(f"Good, but you can do better. Your score was {player_score} out of {len(quiz_questions)}")
                self.speak(f"Good, but you can do better. Your score was {player_score} out of {len(quiz_questions)}")
            else:
                print(f"Not perfect, keep working on it. Your score was {player_score} out of {len(quiz_questions)}")
                self.speak(f"Not perfect, keep working on it. Your score was {player_score} out of {len(quiz_questions)}")

            print("Would you like to learn more about this topic?")
            self.speak("Would you like to learn more about this topic?")

            learn_more = self.take_query('quiz')

            if 'yes' in learn_more or 'sure' in learn_more or 'of course' in learn_more or 'yeah' in learn_more:
                webbrowser.open_new_tab(wikipedia.page(quiz_topic).url)

        except:
            print(f"Unfortunately I was unable to quiz you on {quiz_topic}")
            self.speak(f"Unfortunately I was unable to quiz you on {quiz_topic}")

    def takeNote(self):
        try:
            print("What is the title?")
            self.speak("What is the title?")
            text = self.take_query('note')
            heading = text
            f = open(""+heading+'.md', "w")

            print("What is topic 1?")
            self.speak("What is topic 1?")
            text = self.take_query('note')

            topic = text

            f.write("\n")
            f.write("# " + heading)
            f.write("\n")

            f.write("- "+topic)
            f.write("\n")

            continueNoteTaking = True
            
            while continueNoteTaking:
                print("Do you want to add another topic, another subtopic, or end note?")
                self.speak("Do you want to add another topic, another subtopic, or end note?")
                response = ai.take_query('note')

                if 'subtopic' in response:
                    print("What is the content of this subtopic?")
                    self.speak("What is the content of this subtopic?")

                    subtopic = ai.take_query('note')

                    f.write("\t- "+subtopic)
                    f.write("\n")
                elif 'topic' in response:
                    print("What is the content of this topic?")
                    self.speak("What is the content of this topic?")

                    topic = ai.take_query('note')

                    f.write("- "+topic)
                    f.write("\n")
                elif 'end' in response:
                    continueNoteTaking = False
                
            else:
                f.close()
        except:
            print("Please try again.")
            self.speak("Please try again.")

    def readNote(self, note):
        pass

"""
Example:

ai = AI()
while True:
    print("Listening...")
    ai.take_query('normal')
"""