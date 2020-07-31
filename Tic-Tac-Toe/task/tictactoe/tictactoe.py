# write your code here
def print_board(loc):
    selection1 = loc[13] + " " + loc[23] + " " + loc[33]
    selection2 = loc[12] + " " + loc[22] + " " + loc[32]
    selection3 = loc[11] + " " + loc[21] + " " + loc[31]
    print("---------")
    print("|", selection1, "|")
    print("|", selection2, "|")
    print("|", selection3, "|")
    print("---------")
locations = {13: " ", 23: " ", 33: " ", 12: " ", 22: " ", 32: " ", 11: " ", 21 : " ", 31: " "}
print_board(locations)
turn = 0
while True:
    coordinate = input("Enter the coordinates: ").split()
    if coordinate[0].isdigit() is False or coordinate[1].isdigit is False:
        print("You should enter numbers!")
        continue
    coordinate = [int(i) for i in coordinate]

    if coordinate[0] < 1 or coordinate[0] > 3 or coordinate[1] > 3 or coordinate[1] < 1 :
        print("Coordinates should be from 1 to 3!")
        continue
    new_coordinate = coordinate[0] * 10 + coordinate[1]
    if locations[new_coordinate] != "_" and locations[new_coordinate] != " ":
        print("This cell is occupied! Choose another one!" )
        continue
    if turn % 2 == 0:
        locations[new_coordinate] = 'X'
    else:
        locations[new_coordinate] = 'O'
    turn += 1

    print_board(locations)

    move = [locations[13] + locations[23] + locations[33]
            , locations[12] + locations[22] + locations[32]
            , locations[11] + locations[21] + locations[31]
            , locations[11] + locations[22] + locations[33]
            , locations[13] + locations[22] + locations[31]
            , locations[13] + locations[12] + locations[11]
            , locations[23] + locations[22] + locations[21]
            , locations[33] + locations[32] + locations[31]]
    count = 0
    if "XXX" in move:
        print("X wins")
        break
    elif "OOO" in move:
        print("O wins")
        break
    else:
        if all([cell != " " for cell in locations.values()]):
            print("Draw")
            break
