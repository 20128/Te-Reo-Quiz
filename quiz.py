#Base quiZ learning code 

#importing the random library
import random

#globals and questions lists
score = 0

print("Please answer question by using the letters A,B,C and D. Please do not use the words")
te_reo = ["Kia ora",  "lake", "food", "Test","ngaa mihi","  aotearoa", "kororia", "trip", "hei", "lapid"]
right_answer = ["Hello", "roto", "kai", "test", "Thank you", " New zealand", "glorious", "haerenga", "hei", "whariki"]
option_1 = ["Mr Earl" , "Kai pai" , "morena", "Test","Mahi", "ma", "aniwaniwa", "taea", "karaka", "toi"]
option_2 = ["Haircut" , "Tena koe" , "ngaa mihi" , "Test","Kikorangi", "ika", "kahurangi", "whero", "Ahitereiria", "emerara"]


#  define a function to generate a question
def generate_question(te_reo, right_answer, option_1, option_2):
  global score
  print("what is the correct word for", te_reo, "in maori")
  #generate a random number to determine the sequence of questions 
  random_sequence = random.randint(0,2)
#seperate print statements for readability 
  if(random_sequence == 0):
    print("A", option_1)
    print("B", option_2)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
    else:
      print("incorrect.")
  elif(random_sequence == 1):
    print("A", option_1)
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      score += 1
    else:
      print("incorrect.")
  elif(random_sequence == 2):
    print("A", right_answer)
    print("B", option_2)
    print("C", option_1)
    answer = input().lower()
    if answer == "a":
       score += 1
    else:
      print("incorrect.")

#generate 3 questions pulling possible answers from lists.
for i in range(0, 10):
  generate_question(te_reo[i],right_answer[i],option_1[i],option_2[i])

#print the score at the end  of the quiz
print(score) 