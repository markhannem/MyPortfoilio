# A program for the Edsel Car Rental Company to calculate car rentals

# Written by: Mark Hannem
# Date Written: Jan 17 2021

# Define Program Constants
COST_PER_DAY = 35.00
COST_PER_KM = .10
HST_RATE = .15

# Gather data from the user
CustName = input("Enter Name of Customer: ")
PhoneNum = input("Enter Customer Phone Number: ")
NumDaysRent = int(input("Enter Number of Days Car Rented: "))
PreMileage = int(input("Enter Number of Kilometers when Car Rented: "))
PostMileage = int(input("Enter Number of Kilometers when Car Returned: "))

# Perform required calculations
TotKmsTrav = PostMileage - PreMileage
DayCost = NumDaysRent * COST_PER_DAY
MileageCost = TotKmsTrav * COST_PER_KM
RentCost = DayCost + MileageCost
HST = DayCost * HST_RATE
TotRentCost = RentCost + HST

# Display out results for the user
print()
print("Customers Names:                          ", CustName)
print("Customers Phone Number:                   ", PhoneNum)
print("Number of Days Car Rented:                ", NumDaysRent)
print("Number of Kilometers when Car Rented:     ", PreMileage)
print("Number of Kilometers when Car Returned:   ", PostMileage)
print("Cost of Rental:                           ", RentCost)
print("HST @ 15%:                                ", HST)
print()
print("Total Cost of Rental:                     ", TotRentCost)



