# Easy Quiz details.
easyQuestion = ["In HTML we have","___1___", "types of heading tags for writing heading?",
                "In HTML we use","___2___", "tag to get Bold Text?",
                "HTML stands for","___3___","?",
                "___4___"," tag is used to create links."]

easyAnswer = ["6" , "<b> </b>", "Hyper Text Markup Language", "<a>"]

# Medium Quiz details.
medQueestion = ["We use","___1___", "keyword to define function?",
                "If We have to take input we use","___2___", "function?",
                "To show message to user we use","___3___" ,"?",
                "___4___", "and","___5___"," are used to create loop."]

medAnswer = ["def" , "raw_input", "print", "while", "for"]

# Hard Quiz details.
hardQuestion = ["___1___", "is used to kill Activity.",
                "Latest version of API","___2___", "is called Oreo?",
                "The root element of Android Manifest file is","___3___" ,"?",
                "___4___"," is latest version of android."]
hardAnswer = ["finish()" , "26", "manifest", "Oreo"]

# Ask user to select level, it takes nothing as argument and returns question
#and answer for selected level.
def questionTypeChooser() :
    print "easy -> HTML\nmedium -> Python\nhard -> Android"
    level = raw_input("\nChoose Level for the Quiz(easy, medium, hard): ")
    if level.lower() == "easy":
        return easyQuestion, easyAnswer, "easy"
    if level.lower() == "medium":
        return medQueestion, medAnswer, "medium"
    if level.lower() == "hard":
        return hardQuestion, hardAnswer, "hard"
    else:
        print "You selected invalid level!"
        return questionTypeChooser()

# Removes space between punctuation and males new question in new line.
def spaceRemover(str) :
    str = str.replace(".",".\n")
    str = str.replace("?","?\n")
    return str

# Asks user for answer of the blank if answer is correct moves to next blank.
# It takes blank_number, que, answers, answer as arguments and returns
# next blank_number or asks for same blank based on answer.
def answerCheck(blank_number, que, answers, answer) :
    blank = "___" + str(blank_number) + "___"
    guess = raw_input("Please fill in blank #" + str(blank_number) +
                      " (case-sensitive): ")
    if guess == answer:
        que[que.index(blank)] = answer
        print spaceRemover(" ".join(que)) + "\n"
        blank_number += 1
        return blank_number
    else:
        print "Incorrect answer. Please try again.\n"
        return answerCheck(blank_number, que, answers, answer)

# This is main part of Quiz which manages all operations one by one it
# takes nothing and returns nothing.
def startGame():
    que, answers, level = questionTypeChooser()
    print ("\nHere is the fill-in-the-blank for the " + level + " difficulty "
           "level:")
    print spaceRemover(" ".join(que)) + "\n"
    blank_number = 1
    for answer in answers:
        blank_number = answerCheck(blank_number, que, answers, answer)
    print ("Congratulations, You have completed the" + level)
startGame()
