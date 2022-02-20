
try:
    numeratorValue = int(input("Enter the numerator value: "))
    denominatorValue = eval(input("Enter the denominator value: "))

    divisionResult = numeratorValue  / denominatorValue

    if (denominatorValue == 0):
        pass
    else:
        
        print("Division of ",numeratorValue, 
          "and",  denominatorValue, " is", divisionResult)

except NameError: print("Please look into the variables")
except ZeroDivisionError: print("Denominator can't be ZERO!!! for division...")
except ValueError: print("Please look into the values Entered!")
else: print("Executing the ELSE Block")
finally: print("Executing the FINALLY Block")

