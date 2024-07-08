def numWaterBottles(numBottles: int, numExchange: int) -> int:
    total = numBottles

    while numBottles >= numExchange:
        new_full_bottles = numBottles // numExchange  # Novas garrafas cheia na qual posso trocar
        empty_remainder = numBottles % numExchange  # Garrafas vazias que restaram depois que bebi e troquei
        total += new_full_bottles
        numBottles = new_full_bottles + empty_remainder  # A nova quantidade de garrafas

    return total


numB = 15
numE = 8
print(numWaterBottles(numB, numE))