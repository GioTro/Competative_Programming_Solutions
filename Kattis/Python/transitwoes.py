# Solution transitwoes
import sys


def solve(t_start, t_end, walk, ride, interval):
    # Gives the time we have to wait. Assuming wait is 0 if we arrive at the
    # same time as the bus.
    def wait(x, y): return 0 if x % y == 0 else (x // y + 1) * y - x

    # Run simulation
    t_i = t_start
    while len(ride) > 0:
        t_i += walk.pop(0)
        t_i += wait(t_i, interval.pop(0))
        t_i += ride.pop(0)
    t_i += walk.pop(0)  # Walk to class room

    write(t_i <= t_end)


def write(s):
    if s:
        print('yes')
    else:
        print('no')


def read():
    # A bit messy bessy
    arg = [str(line).strip() for line in sys.stdin]
    t_start, t_end, _ = arg[0].split()
    walk = [int(number) for number in arg[1].split()]
    ride = [int(number) for number in arg[2].split()]
    interval = [int(number) for number in arg[3].split()]

    solve(int(t_start), int(t_end), walk, ride, interval)


read()
