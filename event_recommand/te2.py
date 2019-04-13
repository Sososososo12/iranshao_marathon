import xlrd
import xlwt

userlenfilename = r'./event_participant/{}usertest2.xls'.format(str(583))
user_Fdata = xlrd.open_workbook(filename=userlenfilename)
sheet1 = user_Fdata.sheet_by_index(0)
user_id_set = sheet1.col_values(1)

print(user_id_set)
print(len(user_id_set))
user_id_set_dup=list(set(user_id_set))
print(user_id_set_dup)
print(len(user_id_set_dup))
