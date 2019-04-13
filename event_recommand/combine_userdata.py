import xlwt
import xlrd
import os
import pandas as pd

based_data = xlrd.open_workbook(filename=r'./based/race_info_based.xls')
sheet1 = based_data.sheet_by_index(0)
race_id_set = sheet1.col_values(1)
race_id_len=3295



# def combineEvent(race_id):
#     userlenfilename = r'./event_participant/{}usertest.xls'.format(str(race_id))
#     user_Fdata = xlrd.open_workbook(filename=filename)
#     sheet1 = user_Fdata.sheet_by_index(2)
#     user_id_set = sheet1.col_values(0)
#     user_id_len = len(user_id_set)
#
#     # filename = r'./yuan/{}usertest.xls'.format(str(race_id))
#     filename = r'./yuan/acc_info_test{}.xls'.format(str(stopnum))
#     for
#
#
# # 只显示到关注人数>3的赛事
# # print(race_id_len)
# for index in range(1,race_id_len):

def getUserList(race_id):
    userlenfilename = r'./event_participant/{}usertest.xls'.format(str(race_id))
    user_Fdata = xlrd.open_workbook(filename=userlenfilename)
    sheet1 = user_Fdata.sheet_by_index(2)
    user_id_set = sheet1.col_values(0)
    print('已获取race_id为：'+str(race_id)+'的赛事用户信息！')
    return user_id_set

def compare2Set(baseduserlist=[],userlist1=[]):
    countA=0
    countB=0
    for userindex in userlist1:
        if userindex not in baseduserlist:
            baseduserlist.append(userindex)
            countA = countA + 1
            print(str(countA)+'添加user_id:'+userindex+' 至基础list')
        else:
            countB=countB+1
            print(str(countB)+'. 原有list已存在user_id:'+userindex)
    print('比较完成基础list与chosen_list'+'\n')
    return baseduserlist


baseduser_data=[]
for numindex in range(1,3):
    race_id=int(race_id_set[numindex])
    print('正在比较basedlist与id为'+str(race_id)+'的赛事userlist！')
    userlist2=getUserList(race_id)
    baseduser_data=compare2Set(baseduser_data,userlist2)
    # baseduser_data.extend(mergedlist)

# print(baseduser_data)
data1 = pd.DataFrame({
    'user_id':baseduser_data,
                     })
data1.to_excel(u'./event_participant_Foutput/combine{}usertest.xlsx'.format(race_id), index=False, encoding='"utf_8_sig')
print('已完成合并ID排序1至2的赛事关注者！'+'\n')