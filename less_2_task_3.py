"""Сформировать из введенного числа обратное по порядку входящих в него цифр
 и вывести на экран. Например, если введено число 3486, надо вывести 6843."""
def digit_reverse(digit, res=0):
    if digit == 0:
        return res
    if digit < 10:
        return digit_reverse(digit // 10, res + (digit % 10))
    else:
        return digit_reverse(digit // 10, (res + (digit % 10)) * 10)


z = digit_reverse(1241)
print(z)
