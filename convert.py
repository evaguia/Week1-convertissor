# Converts Celsius (°C) to  Farenheit (°F) and vice versa...

def print_menu():
  print("This program converts temperatures, distances and money.")
  print("Type the number of the wanted proposition.")
  print("Temperatures: 1")
  print("Distances: 2")
  print("Money: 3")
  print("Quitter: 0")
  print("==================================")


def celsius_farenheit(temp):   # Convert celsius to farenheit
    return print(temp * 9/5 + 32)

def farenheit_celsius(temp):     # Convert farenheit to celsius
    return print(1(temp - 32) / (9/5))

def km_miles(d):             # Convert km to miles
   return print(d / 1,609)

def miles_km(d):
   return print(d * 1,609)

def euros_dollars(amount, taux = 1.08):     # Convert euros to dollars
   return print(amount * taux)

def dollars_euros(amount, taux = 1.08):
   return print(amount / taux)

def main():
   while True:
      print_menu()
      choice = input("Enter your answer: ")
      if choice == "1":
         temp = int(input("Enter a temperature: "))
         diff1 = input("Type 1 for °C to °F or 2 for °F to °C: ")
         if diff1 == "1":
            celsius_farenheit(temp)
         elif diff1 == "2":
            farenheit_celsius(temp)
         else:
            print("Unsupported input")
            pass

      elif choice == "2":
         d = int(input("Enter a distance: "))
         diff2 = input("Type 1 for km to miles or 2 for miles to km: ")
         if diff2 == "1":
            km_miles(d)
         elif diff2 == "2":
            miles_km(d)
         else:
            print("Unsupported input")
            pass

      elif choice == "3":
         amount = int(input("Enter an amount: "))
         diff3 = input("Type 1 for € to $ or 2 for $ to €: ")
         if diff3 == "1":
            euros_dollars(amount, taux = 1.08)
         elif diff3 == "2":
            dollars_euros(amount, taux = 1.08)
         else:
            print("Unsupported input")
            pass
      elif choice == "0":
         print("OK")
         print("==================================")
         break
      

main()