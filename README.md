# ATM Controller Project

This project is a simple ATM controller system that simulates the flow of an ATM machine. The functionalities include inserting a card, entering a PIN, selecting an account, and performing transactions like checking balance, depositing money, and withdrawing money. The code is structured to be modular and testable, with support for future integration with real banking systems.

## Features

- Insert Card
- Enter PIN
- Select Account (support for multiple accounts)
- Check Balance
- Deposit Money
- Withdraw Money (with validation for insufficient funds)

## Prerequisites

- Python 3.x
- `unittest` (built-in Python module for testing)

## Setup Instructions

### 1. Clone the Repository

To get started with the project, clone the repository:

```bash
git clone https://github.com/lilble/atm-controller.git
cd atm-controller
```

### 2. Running the Tests

The tests are written using Python's `unittest` framework. You can run the tests from the root directory using:

```bash
python -m unittest discover -s test
```
