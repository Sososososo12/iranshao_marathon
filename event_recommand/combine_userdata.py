import xlwt
import xlrd
import os

based_data = xlrd.open_workbook(filename=r'./based/race_info_based.xls')
sheet1 = based_data.sheet_by_index(0)
race_id_set = sheet1.col_values(1)
race_id_len=3295



def combineEvent(race_id):
    userlenfilename = r'./event_participant/{}usertest.xls'.format(str(race_id))
    user_Fdata = xlrd.open_workbook(filename=filename)
    sheet1 = user_Fdata.sheet_by_index(2)
    user_id_set = sheet1.col_values(0)
    user_id_len = len(user_id_set)

    # filename = r'./yuan/{}usertest.xls'.format(str(race_id))
    filename = r'./yuan/acc_info_test{}.xls'.format(str(stopnum))
    for


# 只显示到关注人数>3的赛事
# print(race_id_len)
for index in range(1,race_id_len):


