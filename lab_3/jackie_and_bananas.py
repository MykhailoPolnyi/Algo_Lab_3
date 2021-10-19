from math import ceil


def count_eating_speed(piles, time):
    piles_num = len(piles)
    if piles_num > time:
        raise ValueError("Given time must be greater than piles amount!")
    if piles_num == time:
        return max(piles)
    all_bananas = sum(piles)
    if all_bananas <= time:
        return 1

    min_eating_speed = ceil(all_bananas/time)
    k = min_eating_speed

    while True:
        time_for_pile = []
        required_time = 0
        for i in range(piles_num):
            time_for_pile.append(ceil(piles[i]/k))
            required_time += time_for_pile[i]
        if required_time <= time:
            return k
        new_coefs = []
        for i in range(piles_num):
            if time_for_pile[i] > 1:
                new_coefs.append(ceil(piles[i] / (time_for_pile[i] - 1)))
        k = min(new_coefs)
