from __future__ import print_function


LARGE = 10000
NUM_RANKS = 2


def top_ratios():
    vowels = ['a', 'e', 'i', 'o', 'u']
    ranks = {}  # Record the highest two ranks
    with open('twl06.txt') as f:
        for w in f:
            word = w.strip()
            nv = 0
            for c in word:
                if c in vowels:
                    nv += 1
            nc = len(word) - nv
            keys = list(ranks.keys())
            keys.sort(reverse=True)
            if nv == 0:
                rank = LARGE
            else:
                rank = nc / nv  # Python 3, float
            if not keys:
                ranks[rank] = [word]
            else:
                # Insert the rank
                if len(keys) < NUM_RANKS:
                    if rank in keys:
                        ranks[rank].append(word)
                    else:
                        ranks[rank] = [word]
                # Insert the rank or replace an old lower rank
                else:
                    if rank in keys:
                        ranks[rank].append(word)
                    else:
                        for e in keys:
                            if rank > e:
                                ranks[rank] = [word]
                                # Delete the lowest rank in ranks
                                lowest_rank = keys[-1]
                                del ranks[lowest_rank]
                                break
    keys = list(ranks.keys())
    keys.sort(reverse=True)
    res = []
    for key in keys:
        res.append(ranks[key])
    return res


if __name__ == '__main__':
    print(top_ratios())
