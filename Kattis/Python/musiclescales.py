import sys

def getScales():
    tone, semitone = 2, 1
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    major = [0, tone, tone, semitone, tone, tone, tone, semitone]

    scales = []

    for i in range(len(notes)):
        sigma = i
        scale = []
        for j in major:
            sigma = (sigma + j) % len(notes)
            scale.append(notes[sigma])
        scales.append(scale)
    return scales

def read():
    return list(set(list(sys.stdin)[-1].split()))

def write(l):
    print('none' if len(l) == 0 else ' '.join(l))

def do():
    song = read()
    scales = getScales()

    solution = []

    for scale in scales:
        candidate = True
        for note in song:
            if note not in scale:
                candidate = False
                break
        if candidate:
            solution.append(scale[0])

    write(solution)

do()