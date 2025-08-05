from datetime import date

#TODO: check if price_a is within 5% higher or lower than price_b
# calculate the lower and upper bounds of the acceptable range around price_b
# then check if price_a falls within that range
# handles both higher and lower differences within the specified percentage and uses clear and concise comparisons
def check_price_range(price_a, price_b):
  # Calculate the 5% difference
  five_percent = 0.05 * price_b# calculates 5% of price_b and stores it in the five_percent variable

  # Calculate the lower and upper bounds of the acceptable range
  #5% lower amount
  lower_bound = price_b - five_percent# calculates the lower_bound by subtracting five_percent from price_b

  #5% higher amount
  upper_bound = price_b + five_percent# calculates the upper_bound by adding five_percent to price_b

  # Check if price_a falls within the range
  # check if price_a is greater than or equal to the lower_bound and less than or equal to the upper_bound
  if lower_bound <= price_a <= upper_bound:
    print("OK")
  else:
    print("Not OK")

# Example usage:
check_price_range(100, 103)  # Output: OK
check_price_range(100, 96)   # Output: OK
check_price_range(100, 106)  # Output: Not OK
check_price_range(100, 94)   # Output: Not OK


