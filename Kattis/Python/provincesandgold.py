a = list(map(int, raw_input().split()))
bp = a[0]*3+a[1]*2+a[2]
res = ""

if bp >= 8:
	res = "Province or "
elif bp >= 5:
	res = "Duchy or "
elif bp >= 2:
	res = "Estate or "

if bp >= 6:
	res += "Gold"
elif bp >= 3:
	res += "Silver"
else:
	res += "Copper"

print (res)