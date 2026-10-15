import random


def flip_coin() -> dict:
    coin_dict = {}
    for cases in range(0, 10000):
        heads_count = 0
        for flip in range(0, 10):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1
        coin_dict[heads_count] = coin_dict.get(heads_count, 0) + 1
    total = sum(coin_dict.values())
    for key in coin_dict:
        coin_dict[key] = round(coin_dict[key] / total, 2)

    return dict(sorted(coin_dict.items()))
