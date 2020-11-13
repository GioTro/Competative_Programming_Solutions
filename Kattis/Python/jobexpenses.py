# Solution to jobexpenses
input() # throw
print(sum( [ -int(num) if int(num) < 0 else 0 for num in input().split() ] ) )