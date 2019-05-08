import xlwt
import xlrd
import pandas as pd


datafile='./based/race_info.xls'
workbook=xlrd.open_workbook(datafile)
sheet=workbook.sheet_by_index(0)
race_id=sheet.col_values(1)
race_id=race_id[1:]
address=sheet.col_values(2)
address=address[1:]
address_len=len(address)

race_id_all=[]
address1=[]
for index in range(0,address_len):

    item_race_id=race_id[index]
    race_id_all.append(item_race_id)
    # item.split()
    item_address = address[index].split()[0]
    address1.append(item_address)

data1 = pd.DataFrame({
    'race_id':race_id_all,
    'location2': address1,
                          })
data1.to_excel(u'./based/race_info_address2.xls', index=False,encoding='"utf_8_sig')