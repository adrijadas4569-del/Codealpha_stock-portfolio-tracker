#Hardcoded stock prices
stock_prices={
    "AAPL":180,
    "TSLA":250,
    "GOOGL":140,
    "MSFT":320
}
total_investment= 0
print("📈 Welcome to Stock Portfolio Tracker")
print("Available Stocks:",",".join(stock_prices.keys()))
while True:
    stock_name= input("\n🗣️ Enter stock name(or type'done'to finish):").upper()
    if stock_name== "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not available.")
        continue
    quantity= int(input("Enter quantity:"))
    investment= stock_prices[stock_name]*quantity
    total_investment+= investment
    print(f"✅ Added{quantity}shares of{stock_name}")
    print(f"Investment Value:💸 {investment}")
print("\n💰Total Investment Value:💸 ",total_investment)
    
save=input("Do you want to save this to a file?(yes/no):").lower()
if save=="Yes":
    file=open("portfolio.txt","w")
    file.write("Total Investment Value:💸 "+str(total_investment))
    file.close()
print("📄 Data saved to Portfolio.txt")
print("✅ Thank you for using Stock Portfolio Tracker")
