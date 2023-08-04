def check_if_only_dots_in_one_column_on_plate(plansza):
    lines = plansza.split("\n")
    counter = 0
    for i in range(len(lines[0])):
        column = [line[i] for line in lines]
        if all(char == "." for char in column):
            counter += 1
    return counter

def checking(some):
    plansz = ""
    for line in some:
        if not line.isspace():
            plansz += line
    return plansz

amount_of_plates_with_empty_columns = 0
max_empty_columns = 0

with open("Dane_2203/szachy_przyklad.txt", "r") as bierka:
    chessboards = bierka.read().strip().split("\n\n")

for chessboard in chessboards:
    empty_columns = check_if_only_dots_in_one_column_on_plate(chessboard)
    if empty_columns >= 1:
        amount_of_plates_with_empty_columns += 1
    if empty_columns > max_empty_columns:
        max_empty_columns = empty_columns

print(amount_of_plates_with_empty_columns, max_empty_columns)

input  = open("ifHaveOnlyDotsInOneColumnONplate.txt" , "w")

input.write(str(amount_of_plates_with_empty_columns)  + " " +  str(max_empty_columns))