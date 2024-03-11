from dados import calcular_tempo


@calcular_tempo
def length_last_word(s):
    return len(s.strip().split(' ')[-1])


string = "   fly me   to   the moon  "
print(length_last_word(string))
