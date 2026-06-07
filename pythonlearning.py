# using dictionaries to make stock price updater

stock = {}
def enter_the_stock():
 n = int(input("how many stock_name you want to enter: "))
 for i in range(n):
    stock_name = input(f"enter the name of stock {i+1}: ")
    price_name = float(input(f"enter the price of stock {i+1}: "))
    stock[stock_name] = price_name
 print(stock)
def update_stock():
 stock_change = input("enter the stock the you want to change the price")
 price_name = float(input("enter the price"))
 if stock_change in stock:
  stock[stock_change] = price_name
 else:
   print("not found")
 print(stock)
def add_new():
 new_stock = input("enter the stock name")
 new_price = float(input("enter the price of new stock"))
 stock[new_stock] = new_price
 print(stock)
def delete_stock():
 deleted_stock = input("enter the stock you want to delete")
 if deleted_stock in stock:
  del stock[deleted_stock]
 else:
   print("not found")
 print(stock)
print("menu bar:"
"1.add stock"
"2.add new stock"
"3.delete stock"
"4.update stock"
"5.exit")
while True:
 choice = int(input("enter choice"))
 if choice == 1:
  enter_the_stock()
 elif choice == 2:
  add_new()
 elif choice == 3:
  delete_stock()
 elif choice == 4:
  update_stock()
 elif choice == 5:
  break

 
