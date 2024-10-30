coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> dict:
    if amount <= 0:
        return "Amount must be > 0"

    res = {}
    for coin in coins:
        if amount // coin != 0:
            res[coin] = amount // coin
            amount -= res[coin] * coin
    return res


def find_min_coins(amount: int) -> dict:
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0
    coin_count = [{} for _ in range(amount + 1)]

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                coin_count[i][coin] = coin_count[i].get(coin, 0) + 1
        # print(f"coin: {coin}, min_coins: {min_coins}. coin_count{coin_count}")
    return coin_count[amount] if min_coins[amount] != float("inf") else {}


print(find_coins_greedy(int(input("sum: "))))
print(find_min_coins(int(input("sum: "))))
