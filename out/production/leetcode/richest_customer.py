def maximum_wealth(accounts):
    richest = sum(accounts[0])

    for i in range(1, len(accounts)):
        curr_customer = 0
        for j in range(len(accounts[i])):
            curr_customer += accounts[i][j]

        if curr_customer > richest:
            richest = curr_customer

    return richest


accout = [[2,8,7],[7,1,3],[1,9,5]]

print(maximum_wealth(accout))

# other way
# def maximumWealth(self, accounts: List[List[int]]) -> int:
#     m = 0
#     for customer in accounts:
#         s = sum(customer)
#         if s > m:
#             m = s
#     return (m)

