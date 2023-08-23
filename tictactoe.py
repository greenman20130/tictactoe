pos = {"a1" :"-", "b1" :"-", "c1" :"-", 
       "a2" :"-", "b2" :"-", "c2" :"-",
       "a3" :"-", "b3" :"-", "c3" :"-"}
winner = True
walk = ""
player = ""
count = 9

combinations = [["a1", "a2", "a3"],
                ["b1", "b2", "b3"],
                ["c1", "c2", "c3"],
                ["a1", "b1", "c1"],
                ["a2", "b2", "c2"],
                ["a3", "b3", "c3"],
                ["a1", "b2", "c3"],
                ["c1", "b2", "a3"]]

table = f"""0  A  B  C
1  {pos["a1"]}  {pos["b1"]}  {pos["c1"]}
2  {pos["a2"]}  {pos["b2"]}  {pos["c2"]}
3  {pos["a3"]}  {pos["b3"]}  {pos["c3"]}"""
print(table)
  
def test(player_):
    walk = input(f"Игрок {player_}, введите номер поля, например b2: ")
    walk = walk.lower()
    if walk in pos:
        if pos[walk] == "-":
            pos[walk] = player_
            
            return table
        else:
            print("Эта позиция занята")
            test(player_)
    else:
        print("Неверное значение")
        test(player_)

def test_win(player_):
    global player
    global winner
    global count
    table = f"""0  A  B  C
1  {pos["a1"]}  {pos["b1"]}  {pos["c1"]}
2  {pos["a2"]}  {pos["b2"]}  {pos["c2"]}
3  {pos["a3"]}  {pos["b3"]}  {pos["c3"]}"""
    print(table)
    for i in range(0, 8):
        comb = combinations[i]
        a, b, c = comb[0], comb[1], comb[2]
        if pos[a] == player_:
            if pos[b] == player_:
                if pos[c] == player_:
                    winner = player_ and False
                    return winner
                    
    count -= 1
    if count == 0:
        print("Ничья")
        count = False
        player = ""
        
def x_player():
    global player
    player = "X"
    test(player)
    return test

def o_player():
    global player
    player = "O"
    test(player)
    return test

while winner:
    x_player()
    test_win("X")
    if winner == False:
        break
    elif count == False:
        break
    o_player()
    test_win("O")
    if winner == False:
        break
    elif winner == False:
        break

if player == "X":
    print("""░██╗░░░░░░░██╗██╗███╗░░██╗███╗░░██╗███████╗██████╗░  ██╗░░██╗
░██║░░██╗░░██║██║████╗░██║████╗░██║██╔════╝██╔══██╗  ╚██╗██╔╝
░╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝  ░╚███╔╝░
░░████╔═████║░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗  ░██╔██╗░
░░╚██╔╝░╚██╔╝░██║██║░╚███║██║░╚███║███████╗██║░░██║  ██╔╝╚██╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝""")
elif player == "O":
    print("""░██╗░░░░░░░██╗██╗███╗░░██╗███╗░░██╗███████╗██████╗░  ░█████╗░
░██║░░██╗░░██║██║████╗░██║████╗░██║██╔════╝██╔══██╗  ██╔══██╗
░╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝  ██║░░██║
░░████╔═████║░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗  ██║░░██║
░░╚██╔╝░╚██╔╝░██║██║░╚███║██║░╚███║███████╗██║░░██║  ╚█████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝  ░╚════╝░""")
