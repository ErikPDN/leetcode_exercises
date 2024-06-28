from collections import Counter


def findCenter(edges):
    dictionary = {}

    for elements in edges:
        for element in elements:
            if element not in dictionary:
                dictionary[element] = 1
            else:
                dictionary[element] += 1

    most_value = max(dictionary, key=dictionary.get)

    return most_value


bordas = [[1,2],
          [2,3],
          [4,2]]
print(findCenter(bordas))
