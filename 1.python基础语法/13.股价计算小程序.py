name = "传智播客"
stock_code = "003032"
stock_price = 19.99
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司：{name}，股票代码：{stock_code},当前股价:{stock_price}")
print("每日增长系数是：%.1f,经过7天增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, finally_stock_price))
