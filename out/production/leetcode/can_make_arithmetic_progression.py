def can_make_progression(arr):
    sorted_arr = sorted(arr)
    diff = sorted_arr[1] - sorted_arr[0]

    sum = 0
    for i in range(1, len(sorted_arr)):
        sum = abs(diff) + sorted_arr[i-1]
        if sum == sorted_arr[i]:
            continue
        else:
            return False

    return True

array = [-509,-19,-439,-264,-404,-369,-299,-89,-229,-54,-194,16,-544,-159,-124,-474,-334]
print(can_make_progression(array))


