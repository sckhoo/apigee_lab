import os
import gspread

#sa = gspread.service_account("sa.json")

print(os.getcwd())
sa = gspread.service_account("sa.json")
sh = sa.open("phone number")

wks = sh.worksheet("Phone")

#print("Rows", wks.row_count)
#print("Cols", wks.col_count)
#print(wks.acell('B2').value)
#print(wks.get('A2:B2'))
#wks.update('A3', "Megan")
#wks.update('A5:B5', [["Ashlee",'987654']])
wks.update('C2', '=UPPER(A2)', raw=False)