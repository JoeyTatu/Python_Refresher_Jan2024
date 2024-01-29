import random

# Consts
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "7️⃣ ": ROWS, # If less than rows, this will never win
    "👑": 5,
    "💎": 5,
    "🪙 ": 10,
    "🍀": 10,
    "🍌": 15,
    "🍇": 15,
    "🍒": 15,
    "🍊": 15,
    "💸": 20
}

symbol_value = { # Winnings = bet x below, e.g. 7️⃣7️⃣7️⃣ = bet x 10
    "7️⃣ ": 10, 
    "👑": 8,
    "💎": 8,
    "🪙 ": 4,
    "🍀": 4,
    "🍌": 2,
    "🍇": 2,
    "🍒": 2,
    "🍊": 2,
    "💸": 0,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]

        for column in columns:
            symbol_to_check = column[line]

            if symbol != symbol_to_check:
                break

        else:
            winnings += values[symbol] * bet
    
    return winnings

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")

            else:
                print(column[row], end="")
        
        print()

def deposit() -> int:
    while True:
        amount = input("How much to deposit: €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break

            else:
                print("Please enter amount greater than 0.")

        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines() -> int:
    while True:
        lines = input(f"How many lines (1-{str(MAX_LINES)})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid amount of lines.")

        else:
            print("Please enter a number")
    
    return lines

def get_bet() -> int:
    while True:
        bet = input("How much to BET on each line? €")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break

            else:
                print(f"Amount must be between €{MIN_BET} and €{MAX_BET}.")

        else:
            print("Please enter a number.")

    return bet

def main():        
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    
    if total_bet > balance:
        amount_needed = total_bet - balance
        print(f"Insuffient funds!\nBalance: €{balance} - Total bet: €{total_bet} - Amount needed: €{amount_needed}")
        quit()

    print(f"Your bet: €{bet} on {lines} lines. Total bet: €{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings = check_winnings(slots, lines, bet, symbol_value)

    print()
    
    if winnings == 0:
        print("Sorry, you didn't win this time.")
    
    else:
        print(f"You won €{winnings}!")

main()