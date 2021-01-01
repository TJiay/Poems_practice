import os
import random as rd

DatePath = "./poems.txt"
Random = 0.1 #10%

class Poems(object):
    def __init__(self, thePoems: str):
        self.thePoems = thePoems.rstrip('\n')
        self.poemsArray = thePoems.rstrip('\n').split(' ,')
        self.poemsLens = len(self.poemsArray)
        self.poemsLenArray = [len(i) for i in self.poemsArray]
        self.chooseNumber = rd.randint(0, self.poemsLens - 1)

    def Println(self):
        def str_patten(num: int): return '\033[4m' + '　'*num + '\033[0m'
        for i in range(self.poemsLens):
            if i == self.chooseNumber:
                print('\033[1m', self.poemsArray[i], '\033[0m', end='')
            if i < self.chooseNumber:
                print(str_patten(self.poemsLenArray[i]), end=',')
            if i > self.chooseNumber:
                print(',', str_patten(self.poemsLenArray[i]), end='')
        print("\n")
        self.Answer()
        self.Tonext()

    def Answer(self):
        answers_input = input("Your answers['dk' to see the answers]: ")
        if answers_input == 'dk': print('\nThe Answers: ', self.thePoems)

    def Tonext(self):
        continue_or_exit = input("\nDo you want to continue or exit?['k' to exit]: ")
        if continue_or_exit == 'k': exit(0)


with open(DatePath, 'r') as poems:
    num = int(input("[Input number of poem]: "))
    count = 0
    for i in poems.readlines():
        if count == num: break
        os.system('clear')
        random_number = rd.randint(1, (int(1/Random) - 1))
        if random_number == 1:
            count += 1
            ob = Poems(i)
            ob.Println()
    print('\033[1;32m', 'You are great!You passed!😎', '\033[0m')
