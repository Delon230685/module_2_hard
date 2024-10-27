while True:
    def gen_pass(n):
        password = ''
        for i in range(1,21):
            for j in range(i + 1,21):
                if i != n and j != n:
                    sum = i + j
                    if n % sum == 0:
                        password += str(i) + str(j)
        return password
    n = int(input('Введите число от 3 до 20: '))
    if 3 <= n <= 20:
        result = gen_pass(n)
        print(f'{result}')
    else:
        print('Число не в заданном диапазоне!')