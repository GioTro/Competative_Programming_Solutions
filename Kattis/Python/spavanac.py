# Solution for kattis problem source: https://open.kattis.com/problems/spavanac
# modulus a la not modulus

def modulus(hours, minutes):
    for i in range(1, 46):
        minutes -= 1
        if minutes < 0:
            minutes += 60
            hours -= 1
            if hours < 0:
                hours += 24
    return hours, minutes


hours, minutes = map(int, raw_input().split())
hours, minutes = modulus(hours, minutes)
print hours, minutes
