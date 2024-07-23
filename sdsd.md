### Problem Explanation
You have two banks, A and B. There is a list of transfers between these two banks. Each transfer has:

A recipient bank (either 'A' or 'B').
A value that indicates how much money is transferred.
The goal is to find out the minimum initial balance each bank needs to ensure that their balance never goes negative during any of the transfers.

Example
Suppose we have the following transfers:

Transfers = "BAABA"
Values = [2, 4, 1, 1, 2]
This means:

Transfer 2 units to B
Transfer 4 units to A
Transfer 1 unit to A
Transfer 1 unit to B
Transfer 2 units to A
We need to determine the starting balance for both banks A and B so that at no point does either bank's balance go negative.

```def solution(R, V):
    # Initialize the balances and minimum balances
    balance_A = 0
    balance_B = 0
    min_balance_A = 0
    min_balance_B = 0
    
    # Iterate through each transfer
    for i in range(len(R)):
        if R[i] == 'A':
            # If the transfer is to bank A, deduct from bank B and add to bank A
            balance_B -= V[i]
            balance_A += V[i]
        else:  # R[i] == 'B'
            # If the transfer is to bank B, deduct from bank A and add to bank B
            balance_A -= V[i]
            balance_B += V[i]
        
        # Track the minimum balance seen for both banks
        min_balance_A = min(min_balance_A, balance_A)
        min_balance_B = min(min_balance_B, balance_B)
    
    # Determine the necessary initial balance for each bank to avoid negative balances
    initial_balance_A = abs(min_balance_A) if min_balance_A < 0 else 0
    initial_balance_B = abs(min_balance_B) if min_balance_B < 0 else 0
    
    # Return the initial balances for bank A and bank B
    return [initial_balance_A, initial_balance_B]
    ```
