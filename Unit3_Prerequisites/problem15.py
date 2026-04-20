def dna_consensus(testcases):
    for m, n, dna in testcases:
        result = ""
        error = 0

        for i in range(n):
            count = {'A':0, 'C':0, 'G':0, 'T':0}

            for seq in dna:
                count[seq[i]] += 1

            # find best character (lexicographically smallest in tie)
            best_char = 'A'
            max_freq = count['A']

            for ch in "CGT":
                if count[ch] > max_freq:
                    max_freq = count[ch]
                    best_char = ch

            result += best_char
            error += (m - max_freq)

        print(result)
        print(error)



testcases = [
    (5, 8, [
        "TATGATAC",
        "TAAGCTAC",
        "AAAGATCC",
        "TGAGATAC",
        "TAAGATGT"
    ]),
    (4, 10, [
        "ACGTACGTAC",
        "CCGTACGTAG",
        "GCGTACGTAT",
        "TCGTACGTAA"
    ]),
    (6, 10, [
        "ATGTTACCAT",
        "AAGTTACGAT",
        "AACAAAGCAA",
        "AAGTTACCTT",
        "AAGTTACCAA",
        "TACTTACCAA"
    ])
]

dna_consensus(testcases)