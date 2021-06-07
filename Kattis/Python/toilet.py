# Problem : https://open.kattis.com/problems/toilet
import re
s = str(input())
ref = s
initial = s[0] + s[1]
s = s[2:]
# First policy
d = re.findall('D', s)
if initial == 'DU' or initial == 'DD':
    print(len(d) * 2 + 1)
elif initial == 'UD':
    print(len(d) * 2 + 2)
else:
    print(len(d) * 2)
# Second policy
d = re.findall('U', s)
if initial == 'UD' or initial == 'UU':
    print(2 * len(d) + 1)
elif initial == 'DU':
    print(2 * len(d) + 2)
else:
    print(2 * len(d))
# Third policy
d = re.findall('DU', s) + re.findall('UD', s)
if initial == 'DU' or initial == 'UD':
    print(len(d) + 1)
else:
    print(len(d))
