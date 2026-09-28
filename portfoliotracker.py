# Simple stock tracker
# Each stock has a name, number of shares, and price per share

stocks = [
    {"name": "AAPL", "shares": 10, "price": 150.00},
    {"name": "MSFT", "shares": 8, "price": 310.00},
    {"name": "GOOG", "shares": 5, "price": 260.00},
]

print("Stock Tracker")
print("---------------")

total_investment = 0

for stock in stocks:
    investment = stock["shares"] * stock["price"]
    total_investment += investment
    print(f"{stock['name']}: {stock['shares']} shares at ${stock['price']:.2f} each = ${investment:.2f}")

print(f"\nTotal Investment: ${total_investment:.2f}")
