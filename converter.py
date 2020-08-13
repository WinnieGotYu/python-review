print("How many kilometers did you cycle today?")
kms = input()
miles = float(kms) / 1.60934
rounded = round(miles, 2)
print(f"{kms} kilometeres is equal to {rounded} miles")
