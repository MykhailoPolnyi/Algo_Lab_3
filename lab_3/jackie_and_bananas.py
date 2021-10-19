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
    required_speed = min_eating_speed

    while True:
        time_for_pile = []
        required_time = 0
        for i in range(piles_num):
            time_for_pile.append(ceil(piles[i]/required_speed))
            required_time += time_for_pile[i]
        if required_time <= time:
            return required_speed
        new_coefs = []
        for i in range(piles_num):
            if time_for_pile[i] > 1:
                new_coefs.append(ceil(piles[i] / (time_for_pile[i] - 1)))
        required_speed = min(new_coefs)
