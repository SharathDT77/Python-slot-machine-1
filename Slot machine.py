#Python slot machine
import random
def spin_row():
    symbols= ["🍒","🍉","🍋","🔔","⭐"]

    return[random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("***********************")
    print(" | ".join(row))
    print("***********************")

def get_payout(row,bet):
    if row[0]== row[1]==row[2]:
        if row[0]=="🍒":
            return bet*3
        elif row[0]=="🍉":
            return bet*2
        elif row[0]=="🍋":
            return bet*4
        elif row[0]=="🔔":
            return bet*8
        elif row[0]=="⭐":
            return bet*10

    return 0

def main():
    balance = 100
    print("*******************************")
    print("Welcome to shadow slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*******************************")
    while balance>0:

        print(f"Current balance is {balance} ")


        bet = int(input("Enter your bet amount: "))
        if bet > balance:
            print("Insufficient balance")
            continue

        if bet<=0:
            print("The bet amount should be greater than 0")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning----\n")
        print_row(row)
        payout = get_payout(row,bet)

        if payout>0:

            print(f"You won ${payout}")
        else:
            print("Sorry you have lost")
        balance += payout
if __name__ == '__main__':
    main()