def excluding_min_and_max(salary):
    ord_salary = sorted(salary)

    ord_salary.pop(-1)
    ord_salary.pop(0)

    return sum(ord_salary) / len(ord_salary)


salario = [1000,9000,2000,3000,4000,6000]
print(excluding_min_and_max(salario))


# best solution
#
# s = set(salary)
# s.remove(min(salary))
# s.remove(max(salary))
# return sum(s) / len(s)
