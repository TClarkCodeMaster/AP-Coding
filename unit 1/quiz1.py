# Create a new document called quiz1.py copy/ paste the following questions
# on your document and answer the following questions.

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

'note: all written responses should be written/ formatted as strings.'

# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.

answer1 = "A linear search would start at the end and a binary would start at the center."
print (answer1)
# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.

answer2 = "It would take five steps, using If, In, Mylist, Print, and else."
print (answer2)
listA = [10,24,34,35,67,98,101]

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.
answer3 = "It would take twelve steps."
print(answer3)

listB = [1,40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244]

# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.
answer4 = "Algorithm is a set of data and codes, stored and use to change or remember someones deeds."
print(answer4)
# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.
answer5 = "The route they take as well as the speed they take it could describe the steps because it shows a complexity of what it takes to get there."
print(answer5)
# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.
answer6 = "You could use the time you've washed clothes and your memmory of what you wore on that day."
print(answer6)
# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.
class Console():
    def __init__ (self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0

class Console():
    def printDetails(self):
        print('Here are the datails of your console:Its black.')
        print('name: BlackiStation '+ self.name)
        print('model: round '+ str(self.model))
        print('year: '+ str(self.year))
# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.. 
def __init__ (self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0

class ConsoleGame():
    def printDetails(self):
        print('Here are the datails of your consoleGame:')
        print('name: Kekekeke'+ self.name)
        print('Wakado: '+ str(self.model))
        print('year: 2937'+ str(self.year))