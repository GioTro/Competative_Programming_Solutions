# Problem : https://open.kattis.com/problems/heartrate
for i in range(int(input())):
    b, p = map(float, input().split())
    k = 60 / p
    kp = k * b
    print("%f %f %f" % (kp - k, kp, kp + k))
