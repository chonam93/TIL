def sum_digit(num):
    # 코드를 입력하세요.
    total = 0
    for number in str(num):
        number_int = int(number)
        total += number_int

    return total

total_def = 0
for i in range(1, 1000):
    total_def += sum_digit(i)

print(total_def)