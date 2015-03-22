
import pandas as pd
import xml.etree.ElementTree as ET
tree = ET.parse('fin_statement.xml')
root = tree.getroot()

'''
 https://docs.python.org/2/library/xml.etree.elementtree.html
'''


    
print'1--------------------------'

for i in root.findall("./"):
    print i


print'mapping table-------------------------------'    
list1=[[],[]]
 
 
for i in root.findall("./FinancialStatements/COAMap/"):
#     print i.attrib
#     print i.get('coaItem'), i.text
    list1[0].append(i.get('coaItem'))
    list1[1].append(i.text)
S2=pd.Series(list1[1],index=list1[0])
print S2
print S2.to_dict()
    

print'qarterly--------------------------------------------'
count=0
lst3=[]
for i in root.findall("./FinancialStatements/InterimPeriods/"):
#     print i
    print i.attrib
    print i.attrib['EndDate']
    lst=[]
    lst2=[]
    lst3.append(i.attrib['EndDate'])
#     for ii in i.findall("./Statement/"):
    for ii in i.findall("./Statement/FPHeader/StatementDate"):pass
#         print ii.text
    for ii in i.findall("./Statement/lineItem"):
#         print ii.get('coaCode'), ii.text
        lst.append(ii.text)
        lst2.append(ii.get('coaCode'))
#         print count
    S=pd.Series(lst, index=lst2)
    if count==0:
        df=pd.DataFrame(S)
    else:
        df[str(count)]=S
    count +=1
df.columns=lst3
df2=df.T
df2.insert(0, 'ticker', 'aaa')
# df2=df.pivot(df.values, df.columns, df.index)
print df2.to_string()




    
# print'--------------------------'
# 
# for i in root.findall("./FinancialStatements/InterimPeriods/"):
#     print i
#     print i.attrib
#     print i.get('Type')
#     print i.text
#     print i.getchildren()
#  
# for i in root.findall("./country/neighbor"):
#     print i
#  
#  
# print "Nodes  that have a 'year' child "
#  
# for i in root.findall(".//year/.."):
#     print i.tag,i.get('name'), i.attrib, i.items(),i.keys()
#      
# print"Nodes with name='Singapore' that have a 'year' child"
#  
# for i in root.findall(".//year/..[@name='Singapore']"):
#     print i.tag,i.get('name'), i.attrib, i.items(),i.keys()
#      
#  
# for i in root.findall("./country/"):
#     print i
