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
    sheet1 = user_Fdata.sheet_by_index(0)
    user_id_set = sheet1.col_values(1)
    user_partcipating=sheet1.col_values(5)
    user_list1=[]
    user_list2=[]
    user_info=[1,2]
    for index in range(1,len(user_id_set)):
        user_list1.append(user_id_set[index])
    for index2 in range(1,len(user_partcipating)):
        user_list2.append(user_partcipating[index2])
    user_info[0]=user_list1
    user_info[1]=user_list2
    print('已获取race_id为：'+str(race_id)+'的赛事用户信息！')
    return user_info

def compare2Set(baseduser_idlist=[],baseduser_plist=[],user_infolist=[]):
    countA=0
    countB=0
    for user_index in range(len(user_infolist[0])):
        if user_infolist[0][user_index] not in baseduser_idlist:
            baseduser_idlist.append(user_infolist[0][user_index])
            baseduser_plist.append(user_infolist[1][user_index])

            countA = countA + 1
            print(str(countA)+'添加user_id:'+user_infolist[0][user_index]+' 至基础list')
        else:
            countB=countB+1
            print(str(countB)+'. 原有list已存在user_id:'+user_infolist[0][user_index])
    print('比较完成基础list与chosen_list')
    return baseduser_idlist,baseduser_plist


baseduser_id=[]
baseduser_partin=[]
based_user_infotuple=(baseduser_id,baseduser_partin)
# getUserList(539)
# getUserList(540)
for raceindex in range(1,3295):
    race_id = int(race_id_set[raceindex])
    print('正在比较basedlist与id为' + str(race_id) + '的赛事userlist！')
    userlistinfo=getUserList(race_id)
    newbaseduser_info=compare2Set(baseduser_id,baseduser_partin,userlistinfo)
    baseduser_id=newbaseduser_info[0]
    baseduser_partin=newbaseduser_info[1]
    lenbased_id=len(baseduser_id)
    print('基础list中现有user_id数量为'+str(lenbased_id)+'个！')



# for numindex in range(1,3):
#     race_id=int(race_id_set[numindex])
#     print('正在比较basedlist与id为'+str(race_id)+'的赛事userlist！')
#     userlist2=getUserList(race_id)
#     baseduser_data=compare2Set(baseduser_data,userlist2)
#     # baseduser_data.extend(mergedlist)

# print(baseduser_data)
data1 = pd.DataFrame({
    'user_id':baseduser_id,
    'user_part in':baseduser_partin
                     })
data1.to_excel(u'./combine14235usertest.xlsx', index=False, encoding='"utf_8_sig')
print('已完成合并ID为583至14235的赛事关注者！'+'\n')