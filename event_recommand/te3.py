import xlrd

dataname = r'./user_done_participant/alluser_filtered.xlsx'
data = xlrd.open_workbook(filename=dataname)
sheet1 = data.sheet_by_index(1)
user_id_set = sheet1.col_values(0)
user_id_len = len(user_id_set)

print(user_id_set[user_id_len-1])