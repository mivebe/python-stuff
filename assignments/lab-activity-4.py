# # lab-activity-4.py

# def main():
#   # Input: Total sales prior to any discount
#   sales = float(input("Enter the total sales amount: $"))

#   # Determine discount rate based on sales ranges
#     #  - No discount for sales less than $100.
#     #  - 5% discount for sales between $100 and $499.99.
#     #  - 10% discount for sales between $500 and $999.99.
#     #  - 15% discount for sales between $1000 and $4999.99.
#     #  - 20% discount for sales of $5000 or more.
#   if sales < 100:
#     discount_rate = 0.0
#   elif 100 <= sales < 500:
#     discount_rate = 0.05
#   elif 500 <= sales < 1000:
#     discount_rate = 0.10
#   elif 1000 <= sales < 5000:
#     discount_rate = 0.15
#   else:
#     discount_rate = 0.20

#   # Calculate discount, discounted price, GST, and final amount
#   discount = sales * discount_rate
#   discounted_price = sales - discount
#   gst = discounted_price * 0.05
#   final_amount = discounted_price + gst

#   # Display the bill
#   print("\n--- Bill Summary ---")
#   print(f"Total Sales: ${sales:.2f}")
#   print(f"Discount Rate: {discount_rate * 100:.2f}%")
#   print(f"Discount Amount: ${discount:.2f}")
#   print(f"Discounted Price: ${discounted_price:.2f}")
#   print(f"G.S.T. (5%): ${gst:.2f}")
#   print(f"Final Amount to Pay: ${final_amount:.2f}")

# if __name__ == "__main__":
#   main()



def phone_call_charges():
  # Define area codes and their rates
  rates = {
    "403": 2.95,
    "780": 3.12,
    "101": 1.15,
    "202": 1.78
  }
  default_rate = 2.50

  # Get user input
  area_code = input("Enter the area code: ")
  minutes = float(input("Enter the number of minutes used: "))

  # Determine the rate based on the area code
  rate = rates.get(area_code, default_rate)

  # Calculate the charge
  charge = minutes * rate

  # Display the results
  print("\n--- Phone Call Summary ---")
  print(f"Length of call: {minutes:.2f}")
  print(f"Area Code: {area_code}")
  print(f"Rate per Minute: ${rate:.2f}")
  print(f"Total Charge: ${charge:.2f}")

if __name__ == "__main__":
  phone_call_charges()

