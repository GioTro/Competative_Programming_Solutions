# solution to pieceofcake2
max_volume = lambda n, h, v : max(max(v*h, (n-h)*v), max((n-v)*h, (n-v)*(n-h)))*4
print( max_volume(* (int(i) for i in input().split()) ) )