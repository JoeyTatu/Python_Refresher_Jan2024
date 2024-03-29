# print("Welcome to the Quiz Game!")

# playing = input("Would you like to play?\n> ").lower()
# if playing != "yes":
#     quit()

# print("OK! Let\'s play! :)")

# score = 0

# answer1 = input("What does CPU stand for\n> ").lower
# if answer1 == "central processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect!")

# answer2 = input("What does CPU stand for\n> ").lower
# if answer2 == "central processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect!")

# answer3 = input("What does CPU stand for\n> ").lower
# if answer3 == "central processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect!")

# answer4 = input("What does CPU stand for\n> ").lower
# if answer4 == "central processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect!")

# answer5 = input("What does CPU stand for\n> ").lower
# if answer5 == "central processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect!")

# print("Game Over!")
# print(f"Your score: {score}/5")

# Made code more structured and advanced: 
print("Welcome to the IT Quiz Game!")

playing = input("Would you like to play?\n> ").lower()
if playing != "yes":
    quit()

print("OK! Let\'s play! :)")

score = 0

questions = [
    # Questions and answers generated by AI
    "What does CPU stand for?",
    "What is the primary function of RAM in a computer?",
    "Which programming language is known for its readability and simplicity?",
    "What does HTML stand for?",
    "What is the purpose of the 'if' statement in programming?",
    "In networking, what does 'LAN' stand for?",
    "What is the function of an IP address?",
    "What is the difference between 'HTTP' and 'HTTPS'?",
    "What is the command to list files in a directory in Unix/Linux?",
    "What does the acronym 'URL' stand for?",
    "What is the purpose of the 'git' version control system?",
    "What is the difference between 'Python 2' and 'Python 3'?",
    "What does DNS stand for in the context of networking?",
    "What is the purpose of a firewall in computer security?",
    "What is the significance of the term 'open source' in software development?",
    "What is a 'boolean' data type in programming?",
    "What is the role of a 'router' in a computer network?",
    "What does SQL stand for in database management?",
    "Explain the concept of 'cloud computing.'",
    "What is the significance of the term 'API' in software development?",
]

def get_correct_answer(question_number):
    correct_answers = [
        # Questions and answers generated by AI
        "central processing unit",
        "temporary storage of data for quick access by the CPU",
        "python",
        "hypertext markup language",
        "conditional execution",
        "local area network",
        "to uniquely identify a device on a network",
        "secure communication over a computer network",
        "ls",
        "uniform resource locator",
        "version tracking and collaboration on software projects",
        "syntax and feature differences, Python 3 being the latest version",
        "domain name system",
        "monitoring and controlling incoming and outgoing network traffic",
        "source code is freely available for modification and redistribution",
        "logical data type representing true or false",
        "directing data packets between computer networks",
        "structured query language",
        "on-demand delivery of computing services over the internet",
        "application programming interface",
    ]
    return correct_answers[question_number - 1]

for i, question in enumerate(questions, 1):
    user_answer = input(f"{i}. {question}\n> ").lower()
    if user_answer == get_correct_answer(i):
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is: {get_correct_answer(i)}")

print("Game Over!")
print(f"Your score: {score}/{len(questions)}")

