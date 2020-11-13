def solve(before, after, n):
    if len(before) == 0:
        print("Deletion succeeded")
        return 0
    if n%2 == 0:
        if before[0] == after[0]:
            solve(before[1:], after[1:], n)
        else:
            print("Deletion failed")
    if n%2 == 1:
        if before[0] != after[0]:
            solve(before[1:], after[1:], n)
        else:
            print("Deletion failed")

r = int(input())
b = str(input())
a = str(input())

solve(b, a, r)
