# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

a = 6336
tmp = a
b = 0

while tmp > 0:
    digit = tmp % 10
    tmp = tmp // 10
    b = b * 10
    b = b + digit

del(tmp)


print("Данное четырёхзначное число читается одинаково слева направо и справо налево: ", True if a == b else False)
