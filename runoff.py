import sys

MAX_VOTERS = 100
MAX_CANDIDATES = 9
candidates = []
pref = [[None for _ in range(MAX_CANDIDATES)] for _ in range(MAX_VOTERS)]


class Candidate:
    def __init__(self, name, votes, eliminated):
        self.name = name
        self.votes = votes
        self.eliminated = eliminated


def main():
    if len(sys.argv) != 2:
        print("Usage: Please provide Candidate List")
        return 1

    candidate_list = sys.argv[1].split(',')
    candidate_count = len(candidate_list)
    print(candidate_list)
    if candidate_count > MAX_CANDIDATES:
        print(f'Maximum number of candidates is {MAX_CANDIDATES}')
        return 2
    for i in range(candidate_count):
        candidates.append(Candidate(candidate_list[i], 0, False))

    voter_count = int(input("No. of voters: "))
    if voter_count > MAX_VOTERS:
        print(f'Maximum numbers of voters is {MAX_VOTERS}')
        return 3

    for i in range(voter_count):
        for j in range(candidate_count):
            name = input(f'Rank {j+1}: ')
            if not vote(i, j, name, candidate_list):
                print("Invalid vote.")
                return 4
        print()

    while True:
        tabulate(voter_count)
        won = print_winner(voter_count)
        if won:
            break

        min = find_min()
        tie = is_tie(min)
        if tie:
            print('No result')
            for i in range(candidate_count):
                if not candidates[i].eliminated:
                    print(candidates[i].name, end=" ")
            print()
            break

        eliminate(min)
        for i in range(candidate_count):
            candidates[i].votes = 0

    return 0


def vote(voter, rank, name, candidate_list):
    if name not in candidate_list:
        return False
    pref[voter][rank] = candidate_list.index(name)
    return True


def is_eliminated(voter, rank):
    if rank > MAX_CANDIDATES:
        raise Exception("Something went wrong!")
    candidate = pref[voter][rank]
    if candidates[candidate].eliminated:
        return is_eliminated(voter,  rank+1)
    candidates[candidate].votes += 1


def tabulate(voter_count):
    rank = 0
    for voter in range(voter_count):
        is_eliminated(voter, rank)


def print_winner(voter_count):
    for candidate in candidates:
        if candidate.votes > voter_count // 2:
            print(f'{candidate.name} is the winner.')
            return True
    return False


def find_min():
    min = float('inf')
    for candidate in candidates:
        if candidate.votes < min and not candidate.eliminated:
            min = candidate.votes
    return min


def is_tie(min):
    for i in range(len(candidates) - 1):
        if not candidates[i].eliminated and candidates[i].votes > min:
            for j in range(i+1, len(candidates)):
                if not candidates[j].eliminated and candidates[j].votes > min:
                    if candidates[i].votes != candidates[j].votes:
                        return False
            break
    return True


def eliminate(min):
    for candidate in candidates:
        if not candidate.eliminated and candidate.votes <= min:
            candidate.eliminated = True


main()
