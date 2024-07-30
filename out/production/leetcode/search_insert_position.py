from dados import calcular_tempo


@calcular_tempo
def searc_insert(lst, target):
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low


tamanho_array = 98765432
array_ordenado = list(range(1, tamanho_array + 1))
targt = 12345678
print(searc_insert(array_ordenado, targt))


