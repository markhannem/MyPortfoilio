# A program for the St. John's Marina & Yacht Club billing & receipt system

# Written by Mark Hannem on January 30, 2022,
# Revisions on Jan 31, Feb 1 and Feb 2, 2022

# Define program constants
EVEN_SITE_COST = 80.00
ODD_SITE_COST = 120.00
ALT_PER_MEM_COST = 5.00
WEEK_SITE_CLEAN_FEE = 50.00
VID_SURV_FEE = 35.00
HST_RATE = .15
STD_MTH_DUES = 75.00
EX_MTH_DUES = 150.00
PROS_FEE = 59.99

# User inputs
SitNum = int(input("Enter the Site Number (1-100): "))
MemName = input("Enter Members Name: ")
StAdd = input("Enter Members Address: ")
City = input("Enter Members City: ")
Prov = input("Enter Members Province (AA): ").upper()
PosCode = input("Enter Members Postal Code (A1A 1A1): ").upper()
PhoneNum = input("Enter Members Home Phone Number (7095551234): ")
CellNum = input("Enter Members Cell Phone Number (7095551234): ")
MemType = input("Enter Member Type (S/E): ").upper()
AltMemNum = int(input("Enter Number of Alternate Members: "))
WeekSiteClean = input("Enter Members Site Cleaning Choice (Y/N): ").upper()
VidSir = input("Enter Members Video Surveillance Choice (Y/N): ").upper()


# Output, Formatting & Calculations
print()
print("     St. John's Marina & Yacht Club")
print("          Yearly Member Receipt")
print()
print("─" * 41)
print()
print("Client Name and Address:")
print()
print("{:<24s}".format(MemName))
print("{:<24s}".format(StAdd))
FullCPP = City + "," + Prov + " " + PosCode
print("{:<24s}".format(FullCPP))
print()
print("Phone: {:<10s}(H)".format(PhoneNum))
print("       {:<10s}(C)".format(CellNum))
print()
if MemType == "S":
    MemTypeDsp = "Standard"
else:
    MemTypeDsp = "Executive"
print("Site #: {:<3}        Member type: {:>9}".format(SitNum, MemTypeDsp))
print()
print("Alternate members:                     {:>2}".format(AltMemNum))
if WeekSiteClean == "N":
    print("Weekly site cleaning:                  No")
else:
    print("Weekly site cleaning:                 Yes")

if VidSir == "N":
    print("Video surveillance:                    No")
else:
    print("Video surveillance:                   Yes")

print()
if SitNum % 2 == 0:
    SiteCharge = EVEN_SITE_COST + (ALT_PER_MEM_COST * AltMemNum)
else:
    SiteCharge = ODD_SITE_COST + (ALT_PER_MEM_COST * AltMemNum)

SiteChargeDsp = "${:,.2f}".format(SiteCharge)
print("Site Charges:                   {:>9s}    ".format(SiteChargeDsp))

if WeekSiteClean == "Y" and VidSir == "Y":
    ExtraCharge = WEEK_SITE_CLEAN_FEE + VID_SURV_FEE
elif WeekSiteClean == "Y" and VidSir == "N":
    ExtraCharge = WEEK_SITE_CLEAN_FEE
elif WeekSiteClean == "N" and VidSir == "Y":
    ExtraCharge = VID_SURV_FEE
else:
    ExtraCharge = 0
ExtraChargeDsp = "${:,.2f}".format(ExtraCharge)
print("Extra Charges:                    {:>7s}    ".format(ExtraChargeDsp))
print("                                ---------")

SubTotal = SiteCharge + ExtraCharge
SubTotalDsp = "${:,.2f}".format(SubTotal)
print("Subtotal:                       {:>9s}     ".format(SubTotalDsp))

SalesTax = HST_RATE * SubTotal
SalesTaxDsp = "${:,.2f}".format(SalesTax)
print("Sales Tax (HST):                  {:>7s}          ".format(SalesTaxDsp))
print("                                ---------")

TotMthChrg = SiteCharge + ExtraCharge + SalesTax
TotMthChrgDsp = "${:,.2f}".format(TotMthChrg)
print("Total monthly charges:          {:>9s}      ".format(TotMthChrgDsp))

if MemType == "S":
    MthDues = STD_MTH_DUES
else:
    MthDues = EX_MTH_DUES
MthDuesDsp = "${:,.2f}".format(MthDues)
print("Monthly dues:                     {:>7s}      ".format(MthDuesDsp))
print("                                ---------")

TotMthFee = TotMthChrg + MthDues
TotMthFeeDsp = "${:,.2f}".format(TotMthFee)
print("Total monthly fees:             {:>9s}     ".format(TotMthFeeDsp))

TotYrlyFee = TotMthFee * 12
TotYrlyFeeDsp = "${:,.2f}".format(TotYrlyFee)
print("Total yearly fees:             {:>10s}           ".format(TotYrlyFeeDsp))
print()

MthPaymnt = (TotYrlyFee + PROS_FEE) / 12
MthPaymntDsp = "${:,.2f}".format(MthPaymnt)
print("Monthly payment:                {:>9s}       ".format(MthPaymntDsp))
print()
print("─" * 41)
print()
print("Issued: 2022-01-31")
print("HST Reg No: 549-33-5849-4720-9885")
print()

CanFee = .60 * (SiteCharge * 12)
CanFeeDsp = "${:,.2f}".format(CanFee)
print("Cancellation fee:               {:>9s}               ".format(CanFeeDsp))





