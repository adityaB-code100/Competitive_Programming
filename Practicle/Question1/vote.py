def australian_voting(candidates, ballots):
    n = len(candidates)
    eliminated = [False] * n

    while True:
        votes = [0] * n

        # Count votes
        for ballot in ballots:
            for choice in ballot:
                if not eliminated[choice]:
                    votes[choice] += 1
                    break

        total_votes = sum(votes)

        # Check winner (>50%)
        for i in range(n):
            if not eliminated[i] and votes[i] > total_votes / 2:
                return [candidates[i]]

        # Find minimum votes among non-eliminated
        min_votes = float('inf')
        for i in range(n):
            if not eliminated[i]:
                min_votes = min(min_votes, votes[i])

        # Check tie
        tied = []
        for i in range(n):
            if not eliminated[i] and votes[i] == min_votes:
                tied.append(i)

        # If all remaining candidates are tied
        remaining = [i for i in range(n) if not eliminated[i]]
        if len(tied) == len(remaining):
            return [candidates[i] for i in remaining]

        # Eliminate candidates with min votes
        for i in tied:
            eliminated[i] = True

candidates = [
    "John Doe",
    "Jane Smith",
    "Jane Austen"
]

ballots = [
    [0,1,2],  
    [1,0,2],  
    [1,2,0],  
    [0,1,2],  
    [2,0,1]   
]

result = australian_voting(candidates, ballots)

for name in result:
    print(name)



# OUTPUT
# John Doe