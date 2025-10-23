def test(lst):
    result = {}
    for item in lst:
        result[item[0]]=item[1:]
        return result

students = [[1, 'jean' 'V'] [2, 'lula' 'V'], [3, 'brian' 'VI',], [4, 'lynne', 'VI'], [5, 'zach', 'VII']]
print("\norignal list of lists:")
print(students)
print("\nconverted lists to a dictionary:")
print(test(students))