def minMovesToSeat(seats, students):
    count_moves = 0
    seats.sort()
    students.sort()

    for i in range(len(students)):
        diff = abs(students[i] - seats[i])
        count_moves += diff

    return count_moves


seat = [3,1,5]
student = [2,7,4]
print(minMovesToSeat(seat, student))








