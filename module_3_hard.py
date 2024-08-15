
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data, result = 0):
    if isinstance(data, int):
        result += data
    elif isinstance(data, str):
        result += len(data)
    elif iter(data):
        for each in data:
            if isinstance( each, dict): # ЕСЛИ DICT
                for key, val in each.items():
                    result = calculate_structure_sum( key, result) # ключ
                    result = calculate_structure_sum( val , result) # значение
            else:
                result = calculate_structure_sum( each, result)
    #print('Текущий элемент', data, 'Текущий результат', result)
    return result

res = calculate_structure_sum( data_structure)
print('Результат ', res)


