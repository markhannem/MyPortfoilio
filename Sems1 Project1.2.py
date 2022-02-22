# A program for Widget Inc. to calculate employee payroll

# Written by: Mark Hannem
# Date Written: Jan 18 2021

# Define Program Constants
HOUR_PAY_RATE = 17.50
COM_PER_WIDGET = .35
INCOME_TAX_RATE = .21
CPP_RATE = .0495
EI_RATE = .016
UNION_DUE_RATE = 15.00

# Gather data from the user
EmName = input("Enter Name of Employee: ")
HrsWrkd = float(input("Enter Total Hours Worked in Pay Period: "))
WidMon = int(input("Enter Number of Widgets Made on Monday: "))
WidTues = int(input("Enter Number of Widgets Made on Tuesday: "))
WidWed = int(input("Enter Number of Widgets Made on Wednesday: "))
WidThur = int(input("Enter Number of Widgets Made on Thursday: "))
WidFri = int(input("Enter Number of Widgets Made on Friday: "))

# Perform required calculations
TotWid = WidMon + WidTues + WidWed + WidThur + WidFri
RegPay = HrsWrkd * HOUR_PAY_RATE
Comm = TotWid * COM_PER_WIDGET
GrosPay = RegPay + Comm
IncTax = INCOME_TAX_RATE * GrosPay
CPP = CPP_RATE * GrosPay
EI = EI_RATE * GrosPay
TotDeduc = IncTax + CPP + EI + UNION_DUE_RATE
NetPay = GrosPay - TotDeduc

# Display output results for the user
print()
print("Employee Names:                           ", EmName)
print("Total Widgets Made:                       ", TotWid)
print("Employee Regular Pay:                     ", RegPay)
print("Employee Commission:                      ", Comm)
print("Employee GrossPay:                        ", GrosPay)
print()
print("Income Tax Deduction:                     ", IncTax)
print("CPP Deduction:                            ", CPP)
print("EI Deduction:                             ", EI)
print("Union Due Deduction:                      ", UNION_DUE_RATE)
print()
print("Total Of All Deductions:                  ", TotDeduc)
print()
print("Total Net Pay After Deductions:           ", NetPay)