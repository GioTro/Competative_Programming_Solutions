# solution to gerrymandering
import sys

def f(v_a, v_b):
	toWin = int((v_a + v_b)/2) + 1
	return ('A', (v_a - toWin), v_b) if v_a > v_b else ('B', v_a, (v_b - toWin))

E = lambda V, w_a, w_b : abs(w_a - w_b)/V

args = [[int(num) for num in line.split()] for line in sys.stdin]
p, d = args[0]
args = args[1:]

votes = {}

for i in args:
	try:
		votes[int(i[0])][0] += int(i[1])
		votes[int(i[0])][1] += int(i[2])
	except:
		votes[int(i[0])] = [int(i[1]), int(i[2])]

total_votes = w_a = w_b = 0

for i in range(d):
	s = f(*votes[i + 1])
	print('%s %d %d' % s)

	total_votes += sum(votes[i + 1])
	w_a += s[1]
	w_b += s[2]

# Last but not least
print(E(total_votes, w_a, w_b))



