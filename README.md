Exact Change Calculator

Welcome to the Exact Change Calculator! This simple yet powerful application allows users to input any amount of money and receive the optimal combination of US currency units as change. Whether you're dealing with dollars and cents in your pocket or need to make change at a cash register, this program has got you covered. 

Getting Started
Prerequisites
Before you begin, make sure you have Python installed on your machine.

Usage
Input any amount of money (with up to two decimal places).
The application will respond with the minimum combination of US currency units as change.
Example
Input: $19.99

Output:
- 1 - $10 bill
- 1 - $5 bill
- 4 - $1 bill
- 3 - quarters
- 2 - dimes
- 4 - pennies
Conditions
Programming Language:

Python
Integrated Development Environment (IDE):

PyCharm
User Input Collection:

User input can be collected through any means - UI, file, terminal, etc.

I also like this program because you ask the user to enter any amount of change
The output will have the CORRECT change back in the form of Bills and Coins. 

This simple Python program calculates the minimum number of bills and coins needed to represent a given amount of money.

## How It Works

The program runs in a loop, allowing the user to input an amount, calculate the change, and display the minimum number of bills and coins required. The user can choose to try again or exit the program.

## Getting Started

### Prerequisites

- Python installed on your machine.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/showcase-exact-change.git
    cd showcase-exact-change
    ```

2. Run the program:

    ```bash
    python exact_change.py
    ```


// PROGRAMMING LANGUAGE */
# I attached my PY file to the link and this will give you access to dive into my program and it will state for the user to enter any amount of money
# I used Py charm community to do this program. 

****// In addition, My program used a list, for currency units. I previously had only 10, 5, 1 dollar bills. Then, as I was thinking, if someone buys groceries over $100.00,
and the user enters any amount, I had to change the ammount to fit the correct change back. ***///

I noticed that whenever I entered an amount like $45.61. It would output the correct total change in bills which would be 
4- $10 bills
1- $5 bills
However, when I got to the 61 cents, it was only printing out just 60 cents, instead of adding the extra penny. So I ended up actually creating an accumulator so that the 1 cent or in this case 1 penny would look like this
        (amount += 0.001)
So I initialized that prior to using the for loop. 
# Now to continue that entry of $45.61
2 - $20 bill
1 - $5 bill
2 - 25 cents
1 - 10 cents
1 - 1 cent
-------------------------------------------------
Above here I did add 100, 50, 20 inside the array list, so I wouldn't have like 6 to 7 $10.00 dollar bills if the User enters $125.30.
So instead of the 4 $10.00 dollar bills, the money count made sure to take 2 - $20 bill instead of having more bills than you needed. 

I found that really helpful to add inside the array. 
-----------------------------------------------------------------------

## Setup
To set up and run the Exact Change Showcase app, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/exact-change-showcase.git
   https://github.com/A-TrainStation/ShowcaseLeanTechniques

Navigate to the project directory:
    cd exact-change-showcase
    
2. Install dependencies:
       npm install

3. Run the application:
       npm start
4. Open your web browser and go to http://localhost: to access the application.

Testing
We have included some testing scenarios to ensure the proper functioning of the Exact Change Showcase app. To run the tests, use the following command:
    
    npm test
Below this will be my steps 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 1

I looked over the technical showcase assessment. I started generating ideas and comming up with which program I wanted to use.
I chose Python because that was the language I am comfortable in. 
**//As a side note I am currently studying Cobol, Java, Cloud Foundations, and Intro Database concept.
I started to generate ideas and thougts on playing with the data by entering a random number and taking the different kinds of Dollar Bills,
and different cents to make out exact change of what the user enters. 

I also was tinkering with the idea on what happens if the user enters a number and it doesn't print out the correct data,
oddly enough when I was configuring out the program in python, I had a scenario that I would enter a number and it would not 
print out the correct change back. 

# Step 2.

**// I decided to def the main 
	def main()
		While True:
			input()
			calcs()
			output()
		try_again = input("Do you want to try again? (yes/no): ").lower() 
        if try_again != 'yes':
            break
			
		This is essentially stating while this program is running true, then enter a number
		Then it will ask the user do you want to try again? 
		
	With the Input data, I wanted to make sure the user could not enter just anything, for instance a string saying "HELLO".
	When that happens, the program won't work unless the user enters any amount with 2 decimals. 
	
	**// BELOW here in the def main is basically saying if the users (input) is not equal to yes
		Then it breaks and falls out of the loop. **//.
		The if try_again != 'yes':
			break 
		

# Step 3

**// def input()
In the input we have is While True, I setup a try and except, Simply saying we ask the user to enter the amount of money up to 2 decimal places
break except any Value error as e: and print enter a valid number. We can't have the user entering just anything like a string word, 
so with the except value error, it forces the user to enter a valid number. The program will not work if you don't enter an amount with 2 decimal.
	While True:
		try:
            amount = float(input("Enter the amount of money(with up to two decimal places: $ "))
            break
        except ValueError as e:
            print("Please enter a valid number.")
	return amount


# Step 4 

//** The calculations. Here I decided to use an array list with each of the forms of dollar Bills and different cents.
Like I previously, mentioned I was playing around with entering a number and writing out how the change should look like,
as if the user enters any amount with 2 decimals. 

Another way I previously had setup was doing a case structure, but when looking at the case structure, It was giving me grief and errors.
Arrays made this program run not only functionally, but effieciently. 

**// Inside the brackets are 
100 bills
50  bills
20  bills
10  bills
5   bills

0.25 cents   Quarters
0.1  cents   Dimes
0.05 cents   Nickles
0.01 cents   Pennies

I did numerous variations of entering numbers to get the program to have an error
Sure enough it did and, Here I'll explain it. 


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

Next we move to the for loop, which is for units in currency_units
	I made up an variable called count and set it equal to (amount // unit)
	  /** This line calculates how many times the current currency unit can fit into the remaining amount. *

	The if count> 0:
		change[unit] = count
		amount -= count * count
	// ** The function iterates through the items in the change dictionary.
If the currency unit is greater than or equal to 1 (implying it's a bill), it prints the count and the unit as a bill with a dollar sign.
If the currency unit is less than 1 (implying it's a coin), it converts the unit to cents, 
prints the count, and handles the pluralization of "cent" based on whether there's more than one cent.


# Step 5

We have the output function which will print out the correct change when the user enters any amount with up to 2 decimals.
def output(change):
    for unit, count in change.items():
        if unit >= 1:
            print(f"{count} - ${unit:.0f} bill")
        else:
            cents = int(unit * 100)
            print(f"{count} - {cents} cent{'s' if cents > 1 else ''}")

// ** The function iterates over the items in the change dictionary.
For each unit, it checks whether it's a bill (with a value greater than or equal to 1) or a coin (with a value less than 1).
If it's a bill, it prints the count and unit as a bill with a dollar sign and without any decimal places.
If it's a coin, it converts the unit to cents, prints the count, and handles pluralization based on whether there's more than one cent.


Happy exact changing!



