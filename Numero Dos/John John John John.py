input_line ="96952600-96977512,6599102-6745632,32748217-32835067,561562-594935,3434310838-3434398545,150-257,864469-909426,677627997-677711085,85-120,2-19,3081-5416,34-77,35837999-36004545,598895-706186,491462157-491543875,5568703-5723454,6262530705-6262670240,8849400-8930122,385535-477512,730193-852501,577-1317,69628781-69809331,2271285646-2271342060,282-487,1716-2824,967913879-967997665,22-33,5722-11418,162057-325173,6666660033-6666677850,67640049-67720478,355185-381658,101543-146174,24562-55394,59942-93946,967864-1031782"

def parse_ranges(line):
 parts = [p.strip() for p in line.split(',') if p.strip()]
 ranges = []
 for p in parts:
     a,b = p.split('-')
     ranges.append((int(a), int(b)))
 return ranges

def sum_invalid_ids(ranges):
 maxb = max(b for _, b in ranges)
 max_digits = len(str(maxb))
 total = 0
 for L in range(1, max_digits // 2 + 1):
     mult = 10**L + 1
     n_min_global = 10**(L-1)
     n_max_global = 10**L - 1
     for a,b in ranges:
         nmin = -(-a // mult)     # rounding up
         nmax = b // mult         # rounding down
         if nmin < n_min_global:
             nmin = n_min_global
         if nmax > n_max_global:
             nmax = n_max_global
         if nmin <= nmax:
             cnt = nmax - nmin + 1
             sumn = (nmin + nmax) * cnt // 2
             total += mult * sumn
 return total

ranges = parse_ranges(input_line)
print(sum_invalid_ids(ranges))
