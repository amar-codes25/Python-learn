"""
Amount = P(1 + R/100)** T
ci = Amount - p
"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time: "))
amount1 = principal * (1 + rate/100) ** time
amount2 = principal * pow((1 + rate/100), time)
print(round(amount2 ,2))
ci = amount1 - principal
print("Compund interest", round(ci))

