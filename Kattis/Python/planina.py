#Solution for kattis problem source: https://open.kattis.com/problems/planina
#
#Obviously the solution is in the square numbered series. I wrote them out and found a pattern,
#but for the squareroots.
#start recursion at a0=2 then an=2*a(n-1)-1   and the series which will be the answer is just a(n)^2


def recursion():
    n = 2
    recursion = [1]
    for i in range(1, 17):
        n=(2*n-1)
        recursion.append(n)
    return recursion

index = int(input())
myList = recursion()
print(myList[index]**2)
