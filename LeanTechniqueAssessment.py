# Input any amount of money (with up to two decimal places)
# Application will respond with the amount in units
# Us currency with the least amount of change given.
#  Ex $19.99
#   1 - $10 bill
#   1 - $5 bill
#   4 - $1 bill
#   3 - quarters
#   2- dimes
#   4 - pennies
# Thorough explanation in your README.md on how to setup and use the app
# Alexander Meiners

def main():
    while True:
        amount = input_Data()
        change = calculate_Change(amount)
        output(change)
        try_again = input("Do you want to try again? (yes/no): ").lower()
        if try_again != 'yes':
            break

def input_Data():
    while True:
        try:
            amount = float(input("Enter the amount of money(with up to two decimal places: $ "))
            break
        except ValueError as e:
            print("Please enter a valid number.")

    return amount
def calculate_Change(amount):
    currency_units = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    change = {}

    amount += 0.001

    for unit in currency_units:
        count = int(amount // unit)
        if count > 0:
            change[unit] = count
            amount -= count * unit
    return change


def output(change):
    for unit, count in change.items():
        if unit >= 1:
            print(f"{count} - ${unit:.0f} bill")
        else:
            cents = int(unit * 100)
            print(f"{count} - {cents} cent{'s' if cents > 1 else ''}")

main()
