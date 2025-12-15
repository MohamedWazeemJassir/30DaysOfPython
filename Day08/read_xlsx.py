import openpyxl

wb = openpyxl.load_workbook("TRANSACTION_FILE.xlsx")
print(wb.sheetnames)
#sheet = wb.active
sheet = wb["Expenses"]

#sheet["H2"] = '=SUM(C1:C100)'

h2_cell = sheet["H2"]
print(h2_cell.value)

h3_cell = sheet["H3"]
print(h3_cell.value)

print("end")
wb.save("TRANSACTION_FILE.xlsx")
