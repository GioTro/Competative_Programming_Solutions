#Solution for kattis problem source: https://open.kattis.com/problems/easiest



def sumdigits(number):
    string = str(number)
    summa = 0
    for i in range(0, len(string)):
        summa += int(string[i])
    return summa

def brute(number):
    hold = sumdigits(number)
    count = 11
    while True:
        if sumdigits(number*count) == hold:
            return count
        else:
            count += 1

numbertocheck = [1]
answer = []
count = 0
#Handles input
while numbertocheck[-1] != 0:
    numbertocheck.append(int(input()))

#executes the calculations
for i in range(1, len(numbertocheck)-1):
    answer.append(brute(numbertocheck[i]))

#handleoutput

for i in range(0, len(answer)):
    print(answer[i])


    
