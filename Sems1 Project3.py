import datetime

# A Program for Honest Harry's Used Car Lot Sales

# Written by Mark Hannem on February 13th, 2022

# Program Edited on Feb. 15, 16, 18, 21

# Define Program Constants
TAX_RATE = .15
FINANCE_FEE = 39.99
TRANS_FEE = .01
LUX_TAX = .016

# Inputs with Validations and Outside Loop
while True:
    while True:
        allowed_char = set("1234567890-")
        InvDate = input("Enter the invoice date (YYYY-MM-DD): ")
        if InvDate == "":
            print("Invoice date cannot be blank please - re-enter.")
        elif set(InvDate).issubset(allowed_char) == False:
            print("Invoice date has invalid characters please - re-enter.")
        elif len(InvDate) != 10:
            print("Invoice date must be 10 characters please - re-enter.")
        else:
            break
    InvDate = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
    InvDateDsp = "{:%B %d, %Y}".format(InvDate)
    while True:
        CustFirst = input("Enter the customers first name: ").title()
    
        if CustFirst == "":
            print("Customers first name cannot be blank please - re-enter.")
        else:
            break
    while True:
        CustLast = input("Enter the customers last name: ").title()
    
        if CustLast == "":
            print("Customers last name cannot be blank please - re-enter.")
        else:
            break
    StAdd = input("Enter customers Address: ")
    City = input("Enter customers City: ")
    while True:
        Prov = input("Enter customers Province (AA): ").upper()
        if Prov == "":
            print("Province cannot be blank please - re-enter.")
        elif len(Prov) != 2:
            print("Province must be 2 characters please - re-enter.")
        elif Prov.isalpha() == False:
            print("Province must be letters only please - re-enter.")
        else:
            break
    while True:
        PosCode = input("Enter Members Postal Code (A1A 1A1) - With 1 Space: ").upper()
        if PosCode == "":
            print("Province cannot be blank please - re-enter.")
        elif len(PosCode) != 7:
            print("Province must be 7 characters with 1 space please - re-enter.")
        else:
            break
    while True:
        PhonNum = input("Enter the customers 10 digit phone number (7095551234): ")
        if PhonNum == "":
            print("Phone number cannot be blank please - re-enter.")
        elif len(PhonNum) != 10:
            print("Phone number must be 10 digits please - re-enter.")
        elif PhonNum.isdigit() == False:
            print("Phone number must be only digits - re-enter.")
        else:
            break
    while True:
        PlatNum = input("Enter the customers plate number (ABC123): ").upper()
        if PlatNum == "":
            print("Plate number cannot be blank please - re-enter.")
        elif len(PlatNum) != 6:
            print("Province must be 6 characters please - re-enter.")
        else:
            break
    CarMake = input("Enter the customers cars make (Ex: Honda): ")
    CarMod = input("Enter the customers cars model (Ex: Civic): ")
    CarYr = input("Enter the customers cars year (Ex: 2015): ")
    while True:
        try:
            SellPrice = int(input("Enter the cars selling price (Max of 50,000): "))
        except:
            print("Cars selling price must be a valid number please - re-enter.")
        else:
            if SellPrice == "":
                print("Cars selling price cannot be blank please - re-enter.")
            elif SellPrice > 50000:
                print("Cars selling price must less then or equal to 50000 please - re-enter.")
            else:
                break
    while True:
        try:
            TrdInAmt = int(input("Enter the cars trade in value , if none put 0 (Zero to Selling Price Value): "))
        except:
            print("Cars trade in amount must be a valid number please - re-enter.")
        else:
            if TrdInAmt == "":
                print("Cars trade in amount cannot be blank please - re-enter.")
            elif TrdInAmt > SellPrice:
                print("Cars trade in amount must less then or equal to the selling price please - re-enter.")
            else:
                break
    SalPerNam = input("Enter the salespersons name: ").title()
    while True:
        CCNum = input("Enter the customers 16 digit credit card number : ")

        if CCNum == "":
            print("Credit Card Number cannot be blank please - re-enter.")
        elif CCNum.isdigit() == False:
            print("Credit Card Number must only contain digits please - re-enter.")
        elif len(CCNum) != 16:
            print("Credit Card Number must only be 16 digits with no spaces please - re-enter.")
        else:
            break
    while True:
        CCExp = input("Enter the customers credit card expiry date (MM/YY) : ")
        allowed_char = set("1234567890/")
        if CCExp == "":
            print("Credit Card Expiry cannot be blank please - re-enter.")
        elif set(CCExp).issubset(allowed_char) == False:
            print("Credit Card Number must only contain digits please - re-enter.")
        elif len(CCExp) != 5:
            print("Credit Card Number must only be 4 digits with slash (MM/YY) please - re-enter.")
        else:
            break
    print()
    print("# Years    # Payments    Financing Fee    Total Price    Monthly Payment")
    print("------------------------------------------------------------------------")
    for Years in range(1, 5):
        PriceAftTrd = SellPrice - TrdInAmt
        Taxes = TAX_RATE * SellPrice

        if SellPrice <= 5000.00:
            LicFee = 75.00
        else:
            LicFee = 165.00

        if SellPrice > 20000.00:
            TransFee = SellPrice * (TRANS_FEE + LUX_TAX)
        else:
            TransFee = SellPrice * TRANS_FEE

        TotSales = PriceAftTrd + Taxes + LicFee + TransFee + (FINANCE_FEE * Years)
        TotSalesDsp = "${:,.2f}".format(TotSales)
        NumPay = Years * 12
        FinFee = FINANCE_FEE * Years
        FinFeeDsp = "${:,.2f}".format(FinFee)
        MthPay = TotSales / NumPay
        MthPayDsp = "${:,.2f}".format(MthPay)

        print("  {:>3}          {:>3}           {:>7}       {:>10}         {:>10}  ".format(Years, NumPay, FinFeeDsp,
                                                                                             TotSalesDsp, MthPayDsp))
    print()

    # Formatting
    PriceAftTrd = SellPrice - TrdInAmt
    Taxes = TAX_RATE * SellPrice
    if SellPrice <= 5000.00:
        LicFee = 75.00
    else:
        LicFee = 165.00
    if SellPrice > 20000.00:
        TransFee = SellPrice * (TRANS_FEE + LUX_TAX)
    else:
        TransFee = SellPrice * TRANS_FEE
    ReceiptId = f"{CustFirst[0]}{CustLast[0]}-{PlatNum[3:6]}-{PhonNum[6:10]}"
    CustName = f"{CustFirst[0]}.{CustLast}"
    FullCPP = City + "," + Prov + "," + PosCode
    SellPriceDsp = "${:,.2f}".format(SellPrice)
    TrdInAmtDsp = "${:,.2f}".format(TrdInAmt)
    PriceAftTrdDsp = "${:,.2f}".format(PriceAftTrd)
    TaxesDsp = "${:,.2f}".format(Taxes)
    LicFeeDsp = "${:,.2f}".format(LicFee)
    TransFeeDsp = "${:,.2f}".format(TransFee)
    FstPayDateDsp = InvDate + datetime.timedelta(days=30)
    FstPayDate = "{:%d-%b-%y}".format(FstPayDateDsp)

    # Next screen, Inside Loop

    while True:
        Continue = input("Enter the payment schedule you want to follow (1-4): ")

        if Continue == "":
            print("Payment schedule cannot be blank - please re-enter.")
        elif Continue != "1" and Continue != "2" and Continue != "3" and Continue != "4":
            print("Payment schedule must be between 1 and 4 - please re-enter.")
        else:
            break
    print()
    if Continue == "1":
        print()
        print("       Honest Harry Car Sales")
        print("      Used Car Sale and Receipt")
        print()
        print("Invoice Date: {}".format(InvDateDsp))
        print("Receipt No: {}".format(ReceiptId))
        print("Salesperson: {}".format(SalPerNam))
        print()
        print("Sold to:")
        print("     {:<30}".format(CustName))
        print("     {:<30}".format(StAdd))
        print("     {:<30}".format(FullCPP))
        print()
        print("Car Details:")
        print("     {:<5} {:<13}   {:<10}".format(CarYr, CarMake, CarMod))
        print("-------------------------------------")
        print("Sale price:                {:>10}".format(SellPriceDsp))
        print("Trade Allowance:           {:>10}".format(TrdInAmtDsp))
        print("Price after Trade:         {:>10}".format(PriceAftTrdDsp))
        print("                           ----------")
        print("HST:                       {:>10}".format(TaxesDsp))
        print("License Fee:               {:>10}".format(LicFeeDsp))
        print("Transfer Fee:              {:>10}".format(TransFeeDsp))
        print("                           ----------")
        TotSales = PriceAftTrd + Taxes + LicFee + TransFee + (FINANCE_FEE * 1)
        TotSalesDsp = "${:,.2f}".format(TotSales)
        print("Total Sales Cost:          {:>10}".format(TotSalesDsp))
        print("-------------------------------------")
        print("Terms: 1           Total payments: 12 ")
        MthPay1 = TotSales / 12
        MthPay1Dsp = "${:,.2f}".format(MthPay1)
        print("Monthly payment:           {:>10}".format(MthPay1Dsp))
        print("First payment date:        {:>10}".format(FstPayDate))
        print()
        print("    Honest Harry Car Sales")
        print("Best used cars at the best price!")
        print()
        Continue2 = input("Do you want to enter another sale? (Y-Yes/N-No): ").upper()
        if Continue2 == "N":
            exit()

    elif Continue == "2":
        print()
        print("       Honest Harry Car Sales")
        print("      Used Car Sale and Receipt")
        print()
        print("Invoice Date: {}".format(InvDateDsp))
        print("Receipt No: {}".format(ReceiptId))
        print("Salesperson: {}".format(SalPerNam))
        print()
        print("Sold to:")
        print("     {:<30}".format(CustName))
        print("     {:<30}".format(StAdd))
        print("     {:<30}".format(FullCPP))
        print()
        print("Car Details:")
        print("     {:<5} {:<13}   {:<10}".format(CarYr, CarMake, CarMod))
        print("-------------------------------------")
        print("Sale price:                {:>10}".format(SellPriceDsp))
        print("Trade Allowance:           {:>10}".format(TrdInAmtDsp))
        print("Price after Trade:         {:>10}".format(PriceAftTrdDsp))
        print("                           ----------")
        print("HST:                       {:>10}".format(TaxesDsp))
        print("License Fee:               {:>10}".format(LicFeeDsp))
        print("Transfer Fee:              {:>10}".format(TransFeeDsp))
        print("                           ----------")
        TotSales2 = PriceAftTrd + Taxes + LicFee + TransFee + (FINANCE_FEE * 2)
        TotSales2Dsp = "${:,.2f}".format(TotSales2)
        print("Total Sales Cost:          {:>10}".format(TotSales2Dsp))
        print("-------------------------------------")
        print("Terms: 2           Total payments: 24 ")
        MthPay2 = TotSales2 / 24
        MthPay2Dsp = "${:,.2f}".format(MthPay2)
        print("Monthly payment:           {:>10}".format(MthPay2Dsp))
        print("First payment date:        {:>10}".format(FstPayDate))
        print()
        print("    Honest Harry Car Sales")
        print("Best used cars at the best price!")
        print()
        Continue2 = input("Do you want to enter another sale? (Y-Yes/N-No): ").upper()
        if Continue2 == "N":
            exit()

    elif Continue == "3":
        print()
        print("       Honest Harry Car Sales")
        print("      Used Car Sale and Receipt")
        print()
        print("Invoice Date: {}".format(InvDateDsp))
        print("Receipt No: {}".format(ReceiptId))
        print("Salesperson: {}".format(SalPerNam))
        print()
        print("Sold to:")
        print("     {:<30}".format(CustName))
        print("     {:<30}".format(StAdd))
        print("     {:<30}".format(FullCPP))
        print()
        print("Car Details:")
        print("     {:<5} {:<13}   {:<10}".format(CarYr, CarMake, CarMod))
        print("-------------------------------------")
        print("Sale price:                {:>10}".format(SellPriceDsp))
        print("Trade Allowance:           {:>10}".format(TrdInAmtDsp))
        print("Price after Trade:         {:>10}".format(PriceAftTrdDsp))
        print("                           ----------")
        print("HST:                       {:>10}".format(TaxesDsp))
        print("License Fee:               {:>10}".format(LicFeeDsp))
        print("Transfer Fee:              {:>10}".format(TransFeeDsp))
        print("                           ----------")
        TotSales3 = PriceAftTrd + Taxes + LicFee + TransFee + (FINANCE_FEE * 3)
        TotSales3Dsp = "${:,.2f}".format(TotSales3)
        print("Total Sales Cost:          {:>10}".format(TotSales3Dsp))
        print("-------------------------------------")
        print("Terms: 3           Total payments: 36 ")
        MthPay3 = TotSales3 / 36
        MthPay3Dsp = "${:,.2f}".format(MthPay3)
        print("Monthly payment:           {:>10}".format(MthPay3Dsp))
        print("First payment date:        {:>10}".format(FstPayDate))
        print()
        print("    Honest Harry Car Sales")
        print("Best used cars at the best price!")
        print()
        Continue2 = input("Do you want to enter another sale? (Y-Yes/N-No): ").upper()
        if Continue2 == "N":
            exit()
    else:
        print()
        print("       Honest Harry Car Sales")
        print("      Used Car Sale and Receipt")
        print()
        print("Invoice Date: {}".format(InvDateDsp))
        print("Receipt No: {}".format(ReceiptId))
        print("Salesperson: {}".format(SalPerNam))
        print()
        print("Sold to:")
        print("     {:<30}".format(CustName))
        print("     {:<30}".format(StAdd))
        print("     {:<30}".format(FullCPP))
        print()
        print("Car Details:")
        print("     {:<5} {:<13}   {:<10}".format(CarYr, CarMake, CarMod))
        print("-------------------------------------")
        print("Sale price:                {:>10}".format(SellPriceDsp))
        print("Trade Allowance:           {:>10}".format(TrdInAmtDsp))
        print("Price after Trade:         {:>10}".format(PriceAftTrdDsp))
        print("                           ----------")
        print("HST:                       {:>10}".format(TaxesDsp))
        print("License Fee:               {:>10}".format(LicFeeDsp))
        print("Transfer Fee:              {:>10}".format(TransFeeDsp))
        print("                           ----------")
        TotSales4 = PriceAftTrd + Taxes + LicFee + TransFee + (FINANCE_FEE * 4)
        TotSales4Dsp = "${:,.2f}".format(TotSales4)
        print("Total Sales Cost:          {:>10}".format(TotSales4Dsp))
        print("-------------------------------------")
        print("Terms: 4           Total payments: 48 ")
        MthPay4 = TotSales4 / 48
        MthPay4Dsp = "${:,.2f}".format(MthPay4)
        print("Monthly payment:           {:>10}".format(MthPay4Dsp))
        print("First payment date:        {:>10}".format(FstPayDate))
        print()
        print("    Honest Harry Car Sales")
        print("Best used cars at the best price!")
        print()
        Continue2 = input("Do you want to enter another sale? (Y-Yes/N-No): ").upper()
        if Continue2 == "N":
            exit()