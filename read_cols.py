import re
from test import loading_province

a= loading_province.names
b= loading_province.provinces
print(b[5])
region_data=re.findall('region=(.*?)&region_scope',b[5])[0]
print(region_data)
