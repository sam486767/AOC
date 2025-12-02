input_line ="96952600-96977512,6599102-6745632,32748217-32835067,561562-594935,3434310838-3434398545,150-257,864469-909426,677627997-677711085,85-120,2-19,3081-5416,34-77,35837999-36004545,598895-706186,491462157-491543875,5568703-5723454,6262530705-6262670240,8849400-8930122,385535-477512,730193-852501,577-1317,69628781-69809331,2271285646-2271342060,282-487,1716-2824,967913879-967997665,22-33,5722-11418,162057-325173,6666660033-6666677850,67640049-67720478,355185-381658,101543-146174,24562-55394,59942-93946,967864-1031782"

def is_invalid(n):
    s = str(n)
    D = len(s)
    for L in range(1, D):
        if D % L != 0:
            continue
        k = D // L
        if k < 2:
            continue
        block = s[:L]
        if block * k == s:
            return True
    return False

def parse_ranges(line):
    out = []
    for p in line.split(','):
        p = p.strip()
        if not p:
            continue
        a, b = p.split('-')
        out.append((int(a), int(b)))
    return out

def solve(line):
    ranges = parse_ranges(line)
    total = 0
    for a, b in ranges:
        for v in range(a, b + 1):
            if is_invalid(v):
                total += v
    return total


print(solve(input_line))
