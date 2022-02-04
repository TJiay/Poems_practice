from os import system, listdir
from re import findall
from random import randint, random
from sys import version as python_version
from platform import system as system_name

# TODO: def a _print function to print any style word  
sys_clean_command = {"Windows": "cls", "Linux": "clear"}

# Poems object
class Poems(object):
    def __init__(self, thePoems: str):
        if thePoems != '':
            self.poemsArray = [findall(r"“?(.*?)[，。：]", i) for i in findall(r".*?[。；？！]”?", thePoems)]
            self.poemsLens = [len(i) for i in self.poemsArray]
            self.poemsSentencesLen = len(self.poemsArray)

    def Println(self, thePoems: str, randomRate = 0.4):
        self.__init__(thePoems)

        def underline(num: int):
            return ' ' + '\033[4m' + '　'*num + '\033[0m'

        for i in range(self.poemsSentencesLen):
            if self.poemsLens[i] <= 1: continue
            if random() < randomRate:
                self.chooseNumber = randint(0, self.poemsLens[i] - 1)
                self.poemsLenArray = [len(k) for k in self.poemsArray[i]]

                for j in range(self.poemsLens[i]): # print poems
                    if j == self.chooseNumber:
                        print('\033[1m', self.poemsArray[i][j], '\033[0m', end='')
                    if j < self.chooseNumber:
                        print(underline(self.poemsLenArray[j]), end='，')
                    if j > self.chooseNumber:
                        print(',', underline(self.poemsLenArray[j]), end='')

                # Answer
                self.Answer(i)

                # Next
                next_or_exit = input("\n Do you want to continue or exit?['q' to exit]: ")
                system('clear')

                if next_or_exit == 'q': # exit
                    print('\033[1;32m', 'Goodbye!', '\033[0m')
                    exit(0)

    def Answer(self, n: int):
        def f(i: int):
            return i + 1 if i + 1 > self.chooseNumber else i 
            # => i + 1 > self.chooseNumber ? i + 1 : i

        for i in range(self.poemsLens[n] - 1):
            answers_input = input(f"\n Your answers for {i} ['a' to see the answers]: ")
            if answers_input == 'a': # print answers
                print('\n The Answers: ', self.poemsArray[n][f(i)])
            elif answers_input == self.poemsArray[n][f(i)]: 
                print('\033[1;32m', 'Good job!', '\033[0m')
            else:
                print('\033[1;31m', 'Error!', '\033[0m')
                print(' The Answers: ', self.poemsArray[n][f(i)])

system(sys_clean_command[system_name()])
ob = Poems('')  # Create a poems object
count, grade_arr = 0, []
max_number_of_poems = 50

# Read Date list
listDir = listdir("./Data/")
for filename in listDir:
    # print(filename)
    grade_scr = findall(r"PoemsOfGrade(.*).txt", filename)[0]
    grade_arr.append(int(grade_scr))
grade_arr.sort()

# Begin
Grade = input(f" Chooes grade{grade_arr}: ")

number_of_poems = int(input("\n Input number of poem[Max: 50]: "))
while(number_of_poems >= max_number_of_poems):
    print('\033[1;31m', 'Warning: the number is bigger than 50', '\033[0m')
    number_of_poems = int(input("\n Input number of poem[Max: 50]: "))

DataPath = f"./Data/PoemsOfGrade{Grade}.txt"

# Main interactive
with open(DataPath, 'r') as poems_file:
    if int(python_version[2]) >= 5 and int(python_version[2]) <= 7: # 3.5 <=python_version <= 3.7
        i = 1
        while i and (count != number_of_poems):
            i = poems_file.readline()
            if i[0] == '#':
                # TODO: Get the poem title and poet name
                continue
            system(sys_clean_command[system_name()])
            ob.Println(i.rstrip("\n"))
            count = count + 1
    else: # := need python_version >= 3.8
        while (i := poems_file.readline()) and (count != number_of_poems):
            if i[0] == '#':
                # TODO: Get the poem title and poet name 
                continue
            print(python_version)
            system(sys_clean_command[system_name()])
            ob.Println(i.rstrip("\n"))
            count = count + 1

# End
if number_of_poems == 0:
    print('\033[1;31m', 'What are you doing?', '\033[0m')
else:
    print('\033[1;32m', 'You are great!You passed!😎', '\033[0m')
