####Refurnished code for problem 48
###Reduced code by 11 lines
##Could reduce further by skipping def

def main(n):
    return str(sum(list(i**i for i in range(1, n+1))))[-10:]

print(main(input("\nPrints the last ten digits of the sum of the series, \n1^1 + 2^2 + ... + n^n\nEnter n: ")))
