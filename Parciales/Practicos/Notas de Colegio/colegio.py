""" Program have to
 1 -> Read File
 2 -> For each: Average Note, and if approved or reproved
 3 -> For all:
        => Porcentage of female aproved
        => Average reproved students
        => Name of the highest note
 """

file_name = "colegio.txt"

file = open(file_name)

count_female = count_aproved_female = 0
reproved_students = average_reproved_note = 0
greatest_note = 0
greatest_note_name = ""

average = 0
state = ""

print("Nombre          Nota Final     Estatus")
for line in file:
    data = line.split(",")
    # Name, Gender, N1, N2, N3
    name, gender = data[0], data[1]
    n1, n2, n3 = int(data[2]), int(data[3]), int(data[4])
    average = (n1 + n2 + n3) / 3
    if average < 9.5:
        state = "REPROBO"
        reproved_students += 1
        average_reproved_note += average
    else:
        state = "APROBO"

    if gender == "F" or gender == "f":
        count_female += 1
        if average > 9.4:
            count_aproved_female += 1

    if greatest_note < average:
        greatest_note = average
        greatest_note_name = name

    print("{0:12}       {1:2.2f}        {2:12}".format(name, average, state))
