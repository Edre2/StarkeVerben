import csv
import random as rando

# The prompt the user gets when he has to answer
PROMPT = "> "
# The numbers of forms of the verbs in franch and german
NUMBER_OF_FORMS_DE = 5
NUMBER_OF_FORMS_FR = 1

# Gets the verbs from verbs.csv
def get_defs():
   verbs = []
   with open('/home/erik/StarkeVerben/verbs.csv', 'r') as verbs_file:
      reader = csv.reader(verbs_file)
      for row in reader:
         verbs.append(row)
   return verbs

# returns a a tuple of the numbers from 1 to n in a random order
def rand(n :int):
   # Creating a tuplu with all the integers from 1 to n :
   n_tabl = []
   for i in range(1, n + 1):
      n_tabl.append(i)
   # creating the tuple who will store the final numbers
   randn = []
   # n times, we pick a random number in the list and add it to the final list, then, in order to not have duplicates, we remove it from the original tuple
   for i in range(n):
      # Make sure there's no mistqke because iff len(n_tabl) = 1, we do % 0 wich is impossible 
      if len(n_tabl) > 1:
         num = int(rando.random() * 1000 ) % (len(n_tabl) - 1)
      else:
         num = 0
      randn.append(n_tabl[num])
      n_tabl.pop(num)
   
   # we return the final tuple
   return randn

def ask_n(lang :bool, n :int, verbs):
   # to know wether the given answer is correct
   correct = False

   # if lang = True, we test from DE to FR else, we test from FR to DE, in both cases, we get what we have to print and what the user has to answer
   DE_FORMS = verbs[n][0]
   for i in range(1, NUMBER_OF_FORMS_DE):
      DE_FORMS += ", " + verbs[n][i]
   FR_FORMS = verbs[n][NUMBER_OF_FORMS_DE]
   for i in range(NUMBER_OF_FORMS_DE + 1, NUMBER_OF_FORMS_DE + NUMBER_OF_FORMS_FR):
      FR_FORMS += ", " + verbs[n][i]

   if lang:
      to_print = DE_FORMS
      ans = FR_FORMS
   else:
      to_print = FR_FORMS
      ans = DE_FORMS

   # Printing what's to print & getting the user's answer
   print(to_print)
   rep = input(PROMPT)

   # testing if the user's answer is correct and returning True
   if rep == ans:
      print("Bien")
      return True
   # If it isn't, making him type it to remeber and returning False
   else:
      while rep != ans:
         print("Recopiez ", ans, " : ")
         rep = input(PROMPT)
      return False
      
def learn():
   # Letting the user to choos wich way he wants to learne 
   print("Que voulez-vous faire ?\n1 - Apprendre FR => DE\n2 - Apprendre DE => FR")
   choice = int(input(PROMPT))
   if choice == 2:
      choice = True
   else:
      choice = False

   # Getting the verbs to learn
   verbs = get_defs()

   # Geeting the order to ask the questions
   questions_n = rand(len(verbs))

   # Asking the questions
   for i in questions_n:
      ask_n(choice, i, verbs)

if __name__ == '__main__':
   learn()
