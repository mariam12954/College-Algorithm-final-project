def birthdaycakecandles(candles):
    max_height = candles[0]
    tallest_count = 0

    for candle in candles:
        if candle > max_height:
            max_height = candle

    return max_height

    for candle in candles:
        if candle == max_height:
            tallest_count += 1

    return tallest_count

n = int (input("enter the number of candles:"))
candles = []
for i in range(n):
    height = int(input(f"enter height of candle{i+1}:"))
    candles.append(height)

is_symmetric = True
for i in range(n//2):
    if candles[i] != candles[n-i-1]:
        is_symmetric = False
        break

tallest_count=birthdaycakecandles(candles)
max_height=birthdaycakecandles(candles)
print("max height:" , max_height)
print("number of tallest candles:" , tallest_count)
print("is symmetric:", is_symmetric)
