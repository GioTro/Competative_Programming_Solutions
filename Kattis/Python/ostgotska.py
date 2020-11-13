# Problem : https://open.kattis.com/problems/ostgotska
import re
line = str(raw_input())
d = re.findall('[a-z]*ae[a-z]*', line)
dp = list(line.split())

if float(len(d))/len(dp) >= 0.4:
	print('dae ae ju traeligt va')
else:
	print('haer talar vi rikssvenska')
