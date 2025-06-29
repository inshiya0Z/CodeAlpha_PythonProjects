# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 140,
    "NFLX": 450
}

portfolio = {}
total_value = 0

print("📊 Welcome to Stock Portfolio Tracker!")
print("Available stocks: AAPL, TSLA, GOOGL, AMZN, NFLX")
print("Enter 'done' to finish input.\n")

# User input loop
while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available. Please try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_value += stock_prices[stock] * quantity

# Display results
print("\n🧾 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment: ${total_value}")

# Optional: Save to text file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_value}\n")
    print("✅ Portfolio saved to 'portfolio_summary.txt'")