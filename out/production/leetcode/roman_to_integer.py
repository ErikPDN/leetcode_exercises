def roman_to_integer(string):
    dc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_in_int = 0

    i = 0
    while i < len(string):
        if i + 1 < len(string) and dc[string[i]] < dc[string[i + 1]]:
            rom_in_int -= dc[string[i]]
        else:
            rom_in_int += dc[string[i]]
        i += 1

    return rom_in_int


print(roman_to_integer('MCMXCIV'))
opcoes = input('Comandos: ').lower()

