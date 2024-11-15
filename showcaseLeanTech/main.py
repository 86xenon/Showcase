DOLLARS = [100, 50, 20, 10, 5, 1]
COINS = [25, 10, 5, 1]
COINS_NAME = ['Quarter(s)', 'Dime(s)', 'Nickel(s)', 'Penny/pennies']


def compute_change(amount): # Algorithm to compute the least coins/dollars
    # initialize lists for dollars / coins
    final_dollars = [0] * len(DOLLARS)
    final_coins = [0] * len(COINS)

    dollar_amount = int(amount[0])
    for i, money in enumerate(DOLLARS):
        final_dollars[i] = dollar_amount // money
        dollar_amount %= money

    if len(amount) == 2:
        coin_amount = int(amount[1])
        for i, coin in enumerate(COINS):
            final_coins[i] = coin_amount // coin
            coin_amount %= coin

    return final_dollars, final_coins

# Assumption of input: no value of zero or less, max of 2 decimal places, must be integer or float
def receive_input():
    while True:
        try:
            money_amount = input("Please enter the amount: ")
            money_amount = float(money_amount)

            if money_amount <= 0:
                print("Please enter a positive number greater than 0.\n")
                continue

            dollar_coins = str(money_amount).split(".") # Separate dollars from coins

            if len(dollar_coins) == 2: # Ensure two decimal places if given 1, reiterate loop if > 2
                if len(dollar_coins[1]) == 1:
                    dollar_coins[1] += "0"
                if int(dollar_coins[1]) > 99:
                    print("Please enter a number with a decimal value no more than 99.\n")
                    continue

            return dollar_coins
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def print_output(dollar, coin):
    cash_output = ''
    i = 0
    for amount in dollar:
        if amount != 0:
            cash_output += '$' + str(DOLLARS[i]) + ' bills: ' + str(amount) + '\n'
        i += 1
    i = 0
    for amount in coin:
        if amount != 0:
            cash_output += str(COINS_NAME[i]) + ': ' + str(amount) + '\n'
        i += 1
    print(cash_output)

if __name__ == '__main__':
    user_input = receive_input()
    dollars, coins = compute_change(user_input)
    print_output(dollars, coins)


