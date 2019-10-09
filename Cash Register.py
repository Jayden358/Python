#Jayden Williams
#9/19
#Cash Register


num_items = 100
cost_per_item = 3.75
tax_rate = .09

#calculate and store the sub total
sub_total = num_items * cost_per_item

#calculate the amount of tax and store result
tax_amount = sub_total * tax_rate

#calculate the total price and store amount
total_price = sub_total + tax_amount

#print receipt
sep1= ": "
sep2= ": $"
print("SALES RECEIPT")
print("Number of items "  ,num_items, sep =sep1,end =" ")
print("Cost per item "  ,cost_per_item, sep =sep2, end=" ")
print("Tax rate "  ,tax_rate, sep= sep1)
print("Tax amount ", tax_amount, sep =sep2)
print("TOTAL SALE PRICE ", total_price, sep =sep2)

input()
