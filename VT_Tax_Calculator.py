rate = eval(input("What is your hourly wage? "))
hours = eval(input("How many hours did you work? "))
taxRate = 0.7633

if hours < 40:
    pay = hours * rate
else:
    pay = hours * rate
    overtimeHours = hours - 40
    overtimePay = overtimeHours * (rate * 0.5)
    pay = pay + overtimePay

print ("Your weekly pay is: $",pay)
print ("Your weekly pay after tax is: $",round(pay * taxRate, 2))

