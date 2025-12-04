const inputLine = "96952600-96977512,6599102-6745632,32748217-32835067,561562-594935,3434310838-3434398545,150-257,864469-909426,677627997-677711085,85-120,2-19,3081-5416,34-77,35837999-36004545,598895-706186,491462157-491543875,5568703-5723454,6262530705-6262670240,8849400-8930122,385535-477512,730193-852501,577-1317,69628781-69809331,2271285646-2271342060,282-487,1716-2824,967913879-967997665,22-33,5722-11418,162057-325173,6666660033-6666677850,67640049-67720478,355185-381658,101543-146174,24562-55394,59942-93946,967864-1031782";

function parseRanges(line) {
    return line
        .split(",")
        .map(p => p.trim())
        .filter(p => p.length > 0)
        .map(p => {
            const [a, b] = p.split("-").map(Number);
            return [a, b];
        });
}

function sumInvalidIds(ranges) {
    const maxb = Math.max(...ranges.map(r => r[1]));
    const maxDigits = String(maxb).length;
    let total = 0;

    for (let L = 1; L <= Math.floor(maxDigits / 2); L++) {
        const mult = 10 ** L + 1;
        const nMinGlobal = 10 ** (L - 1);
        const nMaxGlobal = 10 ** L - 1;

        for (const [a, b] of ranges) {
            let nmin = Math.ceil(a / mult);
            let nmax = Math.floor(b / mult);

            if (nmin < nMinGlobal) nmin = nMinGlobal;
            if (nmax > nMaxGlobal) nmax = nMaxGlobal;

            if (nmin <= nmax) {
                const cnt = nmax - nmin + 1;
                const sumn = ((nmin + nmax) * cnt) / 2;
                total += mult * sumn;
            }
        }
    }

    return total;
}

const ranges = parseRanges(inputLine);
console.log(sumInvalidIds(ranges));