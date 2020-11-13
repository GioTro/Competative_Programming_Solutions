# Problem : https://open.kattis.com/problems/humancannonball2
import math

def time(v_0, theta, x):
	return ( x / (math.cos(theta) * v_0) )

def height(v_0, theta, time):
	return ( v_0*time*math.sin(theta) - (9.81/2*(time**2)) )

def solve(n):
	t = time(n[0], n[1], n[2])
	y = height(n[0], n[1], t)
	if y >= (n[3]+1) and y <= (n[4]-1):
		print("Safe")
	else:
		print("Not Safe")

r = int(raw_input())
data = []
# [v_0, theta, x_1, h_1, h_2]
for i in range(r):
	d = list(map(float, raw_input().split()))
	d[1] = math.radians(d[1])
	data.append(d)

for i in data:
	solve(i)