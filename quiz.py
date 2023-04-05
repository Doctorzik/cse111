"""
This Program uses a csv file that contains basic science questions 
to generate random questions to user in the form of 
computer based test

"""

import math  # Import the math library to perform specific math operations

import csv   # Import the csv module to read a csv file in the program
import random  # Import the random module to randomly select any number of questions from the list
               # of questions depending on the user choice



def main():
  
  try:   # this begin the program the handle any error exceptions that may occur
     

      print("Welcome To this quiz program \nYou are required to get at least 60% \n of the number of questions you choose" )
       # The above will intruduce the quiz,state any rule associated and guides user on expected input

      start_quiz = input("Do you want to play this quiz game? ") # A choice is given to the user to proceed in the quiz
      while start_quiz.lower() == "yes":  # The quiz will only commence if the user input "yes"
        quest = int(input("How many questions do you want to answer? ")) # The user chooses the number of questions he feels he can answer

        num_correct = 0   # This keep track of the user score
 
        question_answer_list = read_file("questions.csv")  # This line calls the read file function and store the required line in the variable
        
        
 
        if quest > len(question_answer_list):  # This line make sure the user does not request to take more quiz than what is availabe 
          print(f"You cannot choose more questions than what is available. Choose a number less than {len(question_answer_list)}")
        else:
        
          num_of_questions = min(quest, len(question_answer_list)) # this get  the number of questions from the list corresponding with the user choice

          questions = random.sample(list(question_answer_list.items()), k=num_of_questions)
                     #  this randomly picks questions from the list of questions from the user input

          for num, (question, alternatives) in enumerate(questions, start=1):
              print(f"\nQuestion {num}:")
            
              correct_answer = alternatives[0]
            

              answer = input(f"{question}? ")
              if answer.lower() == correct_answer.lower():
                  print("Correct!")
                  num_correct += 1


              else:
                  print(f"You did not get it correctly!")

          print(f"\nYou got {num_correct} correct out of {num} questions")

          print(f"\nYou got  {get_percentage(num_correct, num)} percent")  

          print(get_accolade(get_percentage(num_correct, num)))
        

        break      
      else:
        print("Thank you! See you next time incase you decide to play again")


  except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {question_answer_list} doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")



  except ValueError as val_err:
      # This code will be executed if the user enters
      # an invalid integer for the number of questions.
      print()
      print(type(val_err).__name__, val_err, sep=": ")
      print("You entered an invalid integer for the number of questions.")
      print("Run the program again and enter an integer for" \
              " the number of questions.")



  except Exception as excep:
      # This code will be executed if some
      # other type of exception occurs.
      print()
      print(type(excep).__name__, excep, sep=": ")

def get_question_index():

    question_number = int(input("What question number do you want? "))

    index = question_number 

    return index


def get_accolade(percent_score):
  if percent_score >= 50:
    return "Well done! you did a great Job"
  else:
    return "Please Try Harder Next time"


def get_percentage(got_questions, total_questions): # This function calcuate the percentage of given values 
  percent = (got_questions * 100) / total_questions

  return percent



    


def read_file(filename): # This function reads from a csv file and return a compound list

    question_complist = {}
    
    with open(filename,  mode="rt")  as question_file:

      reader = csv.reader(question_file)

      next(reader)

      for line in reader:
        
          question_id = line[0]
          answer_key = line[3]
          questions = line[9]

          question_complist[questions] = [answer_key]
          # question_complist.append(answer_key)

      return  question_complist


if __name__ == "__main__":
    main()