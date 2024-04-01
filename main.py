from random import choice
suit = ["Club", "Diamond", "Heart","Spade"]
rank = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
wallet = 100
def main(wallet):
    def deposit():
        print("You are player 1")
        print(f"You're having {wallet}$")
        while wallet > 0:
            money_bet = input(f"Enter your amount of money you want to bet? $ ")
            if money_bet.isdigit():
                money_bet = int(money_bet)
                if money_bet > 0 and money_bet <= wallet:
                    break
                else:
                    print("You can only bet what inside your wallet")
                    print(f"Your wallet is {wallet}$")
            else:
                print("Please enter a number")
                money_bet = input("Enter your amount of money you want to bet? $ ")
        return money_bet
    money_bet = deposit()
    def generate_deck():
        deck_of_card = []
        for i in suit:
            for j in rank:
                deck_of_card.append(f"{j} of {i}")
        return deck_of_card
    deck = generate_deck()
    def generate_bet_cards(deck):
        deck_of_all_player_combine = []
        while True:
            players = input("Enter the number of player (2 to 5 players) ")
            if players.isdigit():
                players = int(players)
                if players >= 2 and players <= 5:
                    break
                else:
                    print("Re-enter your number of player: ")
            else:
                print("Enter a number: ")
                players = input("Enter the number of player (2 to 5 players) ")
        for i in range(players):
            deck_of_all_player_combine.append([])
        player_position = -1
        for i in range(players):
            player_position += 1 
            for card in range(0,3):
                random_card = choice(deck)
                deck_of_all_player_combine[player_position].append(random_card)
                deck.remove(random_card)
        return deck_of_all_player_combine,players
    bet_cards,players = generate_bet_cards(deck)
    def calculate_point(bet_cards):
        list_of_point = []
        for i in bet_cards:
            list_of_point.append(0)
        for player_card in range(len(bet_cards)):
            for component_card in bet_cards[player_card]:
                component_list = component_card.split()
                first_component = component_list[0]
                if rank[0] in first_component:
                    list_of_point[player_card] +=1
                elif rank[1] in first_component:
                    list_of_point[player_card] +=2
                elif rank[2] in first_component:
                    list_of_point[player_card] +=3
                elif rank[3] in first_component:
                    list_of_point[player_card] +=4
                elif rank[4] in first_component:
                    list_of_point[player_card] +=5
                elif rank[5] in first_component:
                    list_of_point[player_card] +=6
                elif rank[6] in first_component:
                    list_of_point[player_card] +=7
                elif rank[7] in first_component:
                    list_of_point[player_card] +=8
                elif rank[8] in first_component:
                    list_of_point[player_card] +=9
                elif rank[9] in first_component:
                    list_of_point[player_card] +=10
                elif rank[10] in first_component:
                    list_of_point[player_card] +=11
                elif rank[11] in first_component:
                    list_of_point[player_card] +=12
                elif rank[12] in first_component:
                    list_of_point[player_card] +=13
            if list_of_point[player_card] % 10 ==0:
                print(f'The player {player_card + 1} got 10 points')
                list_of_point[player_card] = 10
            else:
                print(f"The player {player_card + 1} got {list_of_point[player_card]% 10} points")
                list_of_point[player_card] = list_of_point[player_card]% 10
        
        return list_of_point
    list_of_point = calculate_point(bet_cards)
    def determine_winner(list_of_point):
        highest_point = max(list_of_point)
        player = 1
        for i in list_of_point:
            player +=1
        point_of_me = list_of_point[0]
        for i in list_of_point[1:]:
            if point_of_me == highest_point and point_of_me ==i:
                result = "draw"
                print(f"The match is {result}. No winner determined")
                break
            if list_of_point[0] == highest_point:
                result = "win"
                print(f"You win with {list_of_point[0]} points")
                break
            else:
                result = "lose"
                print(f"You {result}")
                break
        return result
    result = determine_winner(list_of_point)
    def calculate_wallet_money(wallet,money_bet, players,result):
        if result == "draw":
            pass
        if result == "win":
            wallet += money_bet * (players - 1)
        if result == "lose" :
            if wallet - money_bet > 0:
                wallet -= money_bet
            else:
                print("You are broke")
                return

        
        print(f"You now have {wallet}$")
        decision = "abc"
        while decision != "yes" and decision != "no":
            decision = input(f"Do you want to continue? (yes/no): ")
            match decision:
                case "yes":
                    main(wallet)
                case "no":
                    break
                case _:
                    print("Enter the right decision")
                    continue
    calculate_wallet_money(wallet,money_bet, players,result)    
main(wallet)
