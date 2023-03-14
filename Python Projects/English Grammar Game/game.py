# Made by Okan Deniz as an English project.
# Requirement: "pip install pyttsx3"

import random
import time
import pyttsx3
import threading

questionamount = 40
narratorEnabled = True
voicetype = 1

# Speaker engine
def engineSpeak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voicetype].id)
    engine.say(audio)
    try:
        engine.runAndWait()
    except RuntimeError:
        pass

def speak(text):
    if narratorEnabled:
        audio_thread = threading.Thread(target=engineSpeak, args=(text,))
        audio_thread.start()

# Color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Settings
settingsyn = input(f"Would you like to use the default settings? (Y/N): ").lower()
if settingsyn == "n":
    try:
        setting1 = int(input(f"[Settings] Amount of questions? (1-40): "))
    except ValueError:
        print(f"{RED}Unexpected value assigned. Exiting the program...{RESET}")
        time.sleep(1)
        exit()
    if setting1 > 0 and setting1 <= 40:
        questionamount = setting1
    else:
        print(f"{RED}The value must be between 1 and 40. Exiting the program...{RESET}")
        time.sleep(1)
        exit()
    setting2 = input(f"[Settings] Enable narrator? (Y/N): ").lower()
    if setting2 == "y":
        setting3 = input(f"[Settings] What should be the gender of narrator voice? (Male/Female): ").lower()
        if setting3 == "male":
            voicetype = 0
        elif setting3 == "female":
            voicetype = 1
        else:
            print(f"{RED}Unexpected value assigned. Exiting the program...{RESET}")
            time.sleep(1)
            exit()
    else:
        narratorEnabled = False

# Ending the game function
def gameOver():
    print("")
    print(f"{MAGENTA}------------------------------------------------------------\nGame is over, fetching the scores and creating a leaderboard...\n------------------------------------------------------------{RESET}")
    speak(f"Game is over, fetching the scores and creating a leaderboard...")
    time.sleep(3)
    print("")
    print("Final Scores:")
    speak("Final scores:")
    participants.sort(key=lambda x: x["score"], reverse=True)
    for participant in participants:
        print(f"{YELLOW}{participant['name']}{RESET}: {participant['score']}")
    print("")
    time.sleep(300)
    exit()

# Define the participants
participants = []

speak("How many participants are there?")

try:
    num_of_participants = int(input(f"{CYAN}How many participants are there?{RESET} "))
except ValueError:
    print(f"{RED}Unexpected value assigned. Exiting the program...{RESET}")
    time.sleep(1)
    exit()

for i in range(num_of_participants):
    print("")
    speak(f"Enter participant {i + 1}'s name")
    name = input(f"Enter participant {i + 1}'s name: ")
    speak(f"Participant {name} has been added to the list")
    print(f"Participant \"{name}\" has been added to the list.")
    participants.append({"name": name, "score": 0})

time.sleep(1)
print("")
speak("Starting the game")
print(f"{CYAN}Starting the game...{RESET}")

# Questions dictionary
questions = {
    "Which verb completes this sentence correctly?\n  She ____ a new car.\n    a. has\n    b. have\n    c. had": "a",
    "Which verb completes this sentence correctly?\n  They ____ to the park.\n    a. go\n    b. went\n    c. goes": "b",
    "Which verb completes this sentence correctly?\n  He ____ his homework.\n    a. did\n    b. do\n    c. does": "a",
    "Which word is a possessive pronoun?\n  a. his\n  b. him\n  c. he": "a",
    "Which sentence uses a question word?\n  a. The cat is on the mat\n  b. I am happy\n  c. Where is the library": "c",
    "Which sentence uses a preposition?\n  a. The book is green.\n  b. The cat is under the table.\n  c. I am tired.": "b",
    "Which sentence uses the correct form of 'to be' in the past tense?\n  a. She am here yesterday.\n  b. He is happy.\n  c. They were at the party.": "c",
    "Which sentence uses an article?\n  a. Cat is on table.\n  b. A cat is on the table.\n  c. Cat on table.": "b",
    "Which sentence uses an adjective?\n  a. I run fast.\n  b. The cat is on the mat.\n  c. The red car drives quickly.": "c",
    "Which sentence uses a verb in the present continuous tense?\n  a. I eat breakfast every day.\n  b. They are playing soccer.\n  c. He will go to the store.": "b",
    "Which sentence uses a plural noun?\n  a. The cat is on the mat.\n  b. I have a dog.\n  c. They have three cats.": "c",
    "Which sentence uses a comparative adjective?\n  a. I am happy.\n  b. The book is interesting.\n  c. The car is faster than the bike.": "c",
    "Which sentence uses the correct form of 'to be' in the present tense?\n  a. They is at home.\n  b. She are my friend.\n  c. He is eating lunch.": "c",
    "Which sentence uses a conjunction?\n  a. I am hungry.\n  b. The cat is on the mat.\n  c. I want pizza, but I am on a diet.": "c",
    "Which sentence uses a superlative adjective?\n  a. I am happy.\n  b. The book is interesting.\n  c. The car is the fastest on the road.": "c",
    "Which sentence uses an adverb?\n  a. The cat is on the mat.\n  b. I run quickly.\n  c. The red car drives fast.": "b",
    "Which sentence uses a possessive noun?\n  a. I have a dog.\n  b. The dog has a bone.\n  c. My dog has a bone.": "c",
    "Which sentence uses the correct form of 'to be' in the future tense?\n  a. They am going to the store.\n  b. She is going to be happy.\n  c. He will be here tomorrow.": "c",
    "Which word is an adverb in this sentence?\n  He sings ____.\n    a. sings\n    b. he\n    c. beautifully": "c",
    "Which sentence is in the present continuous tense?\n  a. Walter is cooking dinner.\n  b. Walter cooked dinner yesterday.\n  c. Walter will cook dinner tonight.": "a",
    "Which sentence is in the past simple tense?\n  a. I am studying English.\n  b. He will go to the store later.\n  c. She walked to the park yesterday.": "b",
    "Which sentence is in the future simple tense?\n  a. She is cooking dinner right now.\n  b. They went to the movies last night.\n  c. I will meet you at the restaurant at 7 PM.": "c",
    "Which sentence uses the correct form of the verb 'to be' in the present tense?\n  a. They is happy.\n  b. I are tired.\n  c. He is at work.": "c",
    "Which sentence has a subject pronoun?\n  a. Jesse is reading a book.\n  b. Reading a book is fun.\n  c. The book is interesting.": "a",
    "Which sentence has an object pronoun?\n  a. Mary gave him the book.\n  b. Gustavo is reading the book.\n  c. The book is on the table.": "a",
    "Which sentence has a comparative adjective?\n  a. The car is big.\n  b. The car is bigger.\n  c. The car is biggest.": "b",
    "Which sentence has a superlative adjective?\n  a. Hank is tall.\n  b. Sarah is taller than Tom.\n  c. Jerry is the tallest of them all.": "c",
    "Which sentence uses the correct form of the verb 'to have' in the present tense?\n  a. They has a new car.\n  b. I have a headache.\n  c. He had a good day.": "b",
    "Which sentence has a reflexive pronoun?\n  a. He gave the book to her.\n  b. She brushed her hair.\n  c. They played soccer together.": "b",
    "Which sentence is in the present continuous tense?\n  a. She is going to school every day.\n  b. He played soccer yesterday.\n  c. They are watching a movie right now.": "c",
    "Which sentence has a preposition of location?\n  a. She walked to the store.\n  b. He drove his car.\n  c. The cat is under the table.": "c",
    "Which sentence has a past participle?\n  a. She is cooking dinner.\n  b. He has eaten lunch already.\n  c. They will go to the beach later.": "b",
    "Which sentence is in the past perfect tense?\n  a. She is studying for her test.\n  b. He had finished his homework before dinner.\n  c. They will start the project next week.": "b",
    "Which sentence has a modal verb?\n  a. She walked to the store.\n  b. He can swim very well.\n  c. They played soccer together.": "b",
    "Which sentence has an infinitive verb?\n  a. He likes to play the guitar.\n  b. She is studying English.\n  c. They went to the museum yesterday.": "a",
    "Which sentence is in the past continuous tense?\n  a. Saul reads books every day.\n  b. Jesse was sleeping when the phone rang.\n  c. They are watching a movie right now.": "b",
    "Which sentence is in the present perfect tense?\n  a. Chuck has visited France twice.\n  b. She is studying for her test.\n  c. They will start the project next week.": "a",
    "Which sentence has a conditional verb?\n  a. She is studying Turkish.\n  b. If it rains, we will stay inside.\n  c. They went to the museum yesterday.": "b",
}

# Quiz game function
def quiz_game(participants, questions):
    q_number = 0
    # Shuffle the questions
    question_list = list(questions.keys())
    random.shuffle(question_list)

    for question in question_list:
        # Select a random participant
        q_number += 1
        if questionamount + 1 == q_number:
            gameOver()
        current_participant = random.choice(participants)["name"]
        time.sleep(4)
        print("")
        speak(f"Get ready {current_participant}, It's your turn!")
        print(f"{YELLOW}Get ready {current_participant}, It's your turn!{RESET}")
        time.sleep(3)
        # Ask the question
        print(f"#{q_number}: " + question)
        speak(f"Enter your answer")
        answer = input("Enter your answer: ").lower()

        # Check the answer
        if answer == questions[question].lower():
            # Add points to the participant's score
            for participant in participants:
                if participant["name"] == current_participant:
                    participant["score"] += 1
                    print("")
                    print(f"{GREEN}Your answer is correct!{RESET}\n{participant['name']}, you currently have {CYAN}{participant['score']}{RESET} points.")
                    speak(f"Your answer is correct! You currently have {participant['score']} points.")
        else:
            print("")
            print(f"{RED}Incorrect! The answer was: {RESET}" + questions[question])
            speak(f"Incorrect! The answer was {questions[question]}")

    gameOver()

# Run the quiz game
quiz_game(participants, questions)
