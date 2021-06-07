from math import *
import logging

######### A lot of this code, isn't mine##############

logging.basicConfig(level=logging.DEBUG)


def getFactors(number):
    factors = []
    for potentialFactor in range(1, int(sqrt(number) + 1)):
        if number % potentialFactor == 0:
            factors.append(potentialFactor)
            factors.append(number // potentialFactor)
    return factors


logging.debug(getFactors(17))


def prime(number):
    return len(getFactors(number)) == 2


logging.debug('prime(24) = %s' % (prime(24)))
logging.debug('prime(17) = %s' % (prime(17)))


allFactors = getFactors(698346759856)
largestPrimeFactor = 0
for factor in allFactors:
    if prime(factor) and factor > largestPrimeFactor:
        largestPrimeFactor = factor


print(largestPrimeFactor)
