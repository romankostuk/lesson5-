immutable_var = 'телефон', 'микроволновка', 'холодильник', 1, 2, 3
print(immutable_var)
immutable_var[4] = 25
print(immutable_var)
# четвертый элемент нельзя изменить на число 25,
# так как у нас в переменной задан картеж, а не список.
# Если бы мы хотели сделать изменения, переменную бы взяли в квадратные скобки.