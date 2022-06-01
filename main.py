#Ask the user what Kia Ora means
def qtest():
  print("What does Kia Ora mean? ")
  print("1: Hello 2: Goodbye 3: Mr Earl 4: Hair Cut")
  q1_ans = input("")
  q1_ans = q1_ans.lower()

  if q1_ans == "1" or q1_ans == "hello":
    print("Correct")
    q1()
  else:
    print("Incorrect")
    qtest()
#Ask the user what ka pai means. If they say the correct answer then write correct. But if they say the incorrect answer then write incorrect and make them do the question again
def q1():
  print("What does ka pai mean?")
  print("1: Well done 2: Go eat 3: Navie 4: Go home")
  q1_ans = input("")
  q1_ans = q1_ans.lower()

  if q1_ans == "1" or q1_ans == "well done": 
    print("correct")
    q2()
  else:
    print("incorrect")
    q1()
#Ask the user How do you say good morning in Te Reo. If they give the correct answer then write correct. If they give the incorrect answer then write incorrect and make them do the question again
def q2():
  print("How do you say good morning in Te Reo?") 
  print(" 1: Tena koe 2: buenos dias 3: John-eun achim 4: Morena")
  q2_ans = input("")
  q2_ans = q2_ans.lower()

  if q2_ans == "4" or q2_ans == "hello":
    print("correct")
    q3()
  else:
    print("incorrect")
    q2()
#Ask the user what color is kikorangi. If they type blue or 1 then write correct. If they type anything else. Then write incorrect and make them do the question again
def q3():
  print("What color is kikorangi?")
  print("1: Blue 2: green 3: Gold 4: Emerald")
  q3_ans = input("")
  q3_ans = q3_ans.lower()

  if q3_ans == "1" or q3_ans == "blue": 
    print("correct")
    q4()
  else:
    print("incorrect")
    q3()
#Ask the user what the color green is in Te Reo. If they say 1 or kakariki. Then write correct. If they type anything else... then write incorrect or 
def q4():
  print("what is green in te reo?")
  print("1:Kakariki 2:Kowhai 3: Kikorangi 4: Mangu")
  q4_ans = input("")
  q4_ans = q4_ans.lower() 
  
  if q4_ans == "1" or "blue":
    print("correct")
    q5()
  else:
    print("incorrect")
    q4()
# Ask the user what does Nau Mai mean in Te reo. If they say  1 or welcome. Then write correct. But if they type anything else... then write incorrect. 
def q5():
  print("what does the Te Reo phrase Nau Mai Haere Mai mean?")
  print("1: Welcome 2: What is your name? 3: Hi my name is 4: Do you know how to do this?")
  q5_ans = input("")
  q5_ans = q5_ans.lower()
  if q5_ans == "1" or "welcome":
    print("correct")
    q6()
  else: 
    print("incorrect")
    q5()

def q6():
  print("How do you say how are you in Te Reo?")
  print("1: Kei te pehea koe 2: Haere ra 3: Kia makona 4: Ka kite Ano")
  q6_ans = input("")
  q6_ans = q6_ans.lower()

  if q6_ans == "1" or q6_ans == "kei te pehea koe":
    print("correct")
    q7()
  else:
    print("incorrect")
    q6()

def q7():
  print("How do you say New Zealand in te reo?")
  print("1: Aotearoa 2: Nueva zelandia 3: zealandia 4: New Aotearoa")
  q7_ans = input("")
  q7_ans = q7_ans.lower()

  if q7_ans == "1" or q7_ans == "Aotearoa":
    print("correct")
    q8()
  else:
    print("incorrect")
    q9()

def q8():
  print("What is the most famous greeting in te reo that is widely used across new zealand?")
  print(" 1: Kia Ora 2: Tena Koe 3: Tena koutou katoa 4: Kia ora tena koutou koe")
  q8_ans = input("")
  q8_ans = q8_ans.lower()

  if q8_ans == "1" or q8_ans == "Kia Ora":
    print("correct")
    q9()
  else:
    print("incorrect")
    q8()

def q9():
  print("What does ata marie mean?")
  print("1: Kia Ora 2: Tena Koe 3: Tena koutou katoa 4: Kia ora tena koutou koe")
  q9_ans = input("")
  q9_ans = q9_ans.lower()
  
  if q9_ans == "1" or "kia ora":
    print("correct")
    q10()
  else:
    print("incorrect")
    q9()

def q10():
  print("What does Nga mihi mean?")
  print("1: Congratulations 2: Good work 3: Good job 4: well done")
  q10_ans = input("")
  q10_ans = q10_ans.lower()
  
  if q10_ans == "1" or "congratulations":
    print("correct")
    q10()
  else:
    print("incorrect")
    q10()
    

qtest()