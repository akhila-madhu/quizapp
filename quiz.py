import time

score = 0

name = str(input("What's your name? "))
print("Welcome to the Python quiz!"+name)
print(name +"for you knowldge every correct answer you will get 1 mark")
def q1():
    global score
    print("\n1.In python, print type(type(int))")
    time.sleep(0.5)
    print("a) type 'type' ")
    print("b) Error")
    print("c)0 \n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
        
    else:
        print("Sorry, that was the wrong answer!")
    

    q2()
    
def q2():
    global score
    time.sleep(0.5)
    print("\n2.Is Python case sensitive when dealing with identifiers?")
    print("a) Yes")
    print("b) No")
    print("c) machine dependent\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
    
    q3()
def q3():
    global score
    time.sleep(0.5)
    print("\n3.What is the maximum possible length of an identifier")
    print("a) 31 characters")
    print("b) 20 characters")
    print("c) none of the mentioned\n")

    answer = str(input("What's the right answer: "))

    if answer == "c":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")

    q4()
def q4():
    global score
    time.sleep(0.5)
    print("\n4.All keywords in Python are in _________?")
    print("a) Lowercase")
    print("b) Uppercase")
    print("c) none of the mentioned\n")

    answer = str(input("What's the right answer: "))

    if answer == "c":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
       
    q5()
def q5():
    global score
    time.sleep(0.5)
    print("\n5.What will be the output of the following Python expression?print(4.00/(2.0+2.0))")
    print("a) Error")
    print("b) 1.0")
    print("c) 1.00\n")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
        
    q6()
def q6():
    global score
    time.sleep(0.5)
    print("\n6. What is the output when we execute list(“hello”)? ")
    print("a) [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]")
    print("b) ['hello']")
    print("c) 'hello'\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
       
    q7()
def q7():
    global score
    time.sleep(0.5)
    print("\n7.Which of the following commands will create a list?")
    print("a) list1 = list()")
    print("b)list1 = [] ")
    print("c) all of the above mentioned \n")

    answer = str(input("What's the right answer: "))

    if answer == "c":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
        
    q8()
def q8():
    global score
    time.sleep(0.5)
    print("\n8. Which of the following statements create a dictionary?")
    print("a)d = {} ")
    print("b) d = {“john”:40, “peter”:45}")
    print("c)all of the above ")

    answer = str(input("What's the right answer: "))

    if answer == "c":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
       
    q9()
def q9():
    global score
    time.sleep(0.5)
    print("\n9.Suppose d = {“john”:40, “peter”:45}. To obtain the number of entries in dictionary which command do we use?")
    print("a) d.size()")
    print("b)  len(d)")
    print("c)size(d) \n")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
       

    q10()

def q10():
    global score
    time.sleep(0.5)
    print("\n10.Which of the following is not a declaration of the dictionary?")
    print("a) {1,”A”,2”B”}")
    print("b) {1: ‘A’, 2: ‘B’}")
    print("c) dict([[1,”A”],[2,”B”]])\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
       
    

q1()
if(score>=7):
    print("Excellent!!!  "+name)
    print("Your scored: ",score)
elif(3<score<7):
    print("Good ! "+name)
    print("Your scored: ",score)
else:
    print("better luck next time ! "+name)
    print("Your scored: ",score)

