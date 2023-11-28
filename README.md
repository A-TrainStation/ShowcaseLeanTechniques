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
        amount += 0.001
So I iniilized that prior to using the for loop. 
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

Happy exact changing!



