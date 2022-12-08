def solution6(p):
    with open(p) as inp:
        for line in inp:
            signal = line

    buffer = set()
    for i, ch in enumerate(signal):
        if len(buffer) == 4:
            print(signal[i - 10:i])
            return i
        else:
            if ch in buffer:
                buffer = {ch}
            else:
                buffer.add(ch)


def solution6b(p):
    with open(p) as inp:
        for line in inp:
            signal = line

    buffer = set()
    for i, ch in enumerate(signal):
        if len(buffer) == 14:
            print(signal[i - 14:i], len(signal[i - 14:i]))
            return i
        else:
            if ch in buffer:
                buffer = {ch}
            else:
                buffer.add(ch)