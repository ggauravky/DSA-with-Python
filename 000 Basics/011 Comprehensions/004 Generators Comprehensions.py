daily_sales=[5,10,15,20,25,30]

total_cups=(sale for sale in daily_sales if sale>10)
print(total_cups)