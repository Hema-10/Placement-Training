'''To solve the problem of determining which customers account for at least 5% of the total number of trades and 
then sorting those customers alphabetically'''
def most_active(customers):
    from collections import Counters 
    trade_counts = Counter(customers)
    total_trades = len(customers)
    threshold = total_trades * 0.0
    active_customers = [customer for customer, count in trade_counts.items() if count >= threshold]
    active_customers.sort()
    return active_customers
n = int(input().strip())
customers = [input().strip() for _ in range(n)]
result = most_active(customers)
for customer in result:
    print(customer)
