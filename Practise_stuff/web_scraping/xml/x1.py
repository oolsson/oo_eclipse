import xml.etree.ElementTree as ET
tree = ET.parse('xml_data.xml')
root = tree.getroot()

'''
 https://docs.python.org/2/library/xml.etree.elementtree.html
'''

#print root.getchildren()[1].getchildren()
for i in root.getchildren():
    print i.getchildren()
    
print'1--------------------------'

for i in root.findall("./country"):
    print i.getchildren()
    

print'2--------------------------'

for i in root.findall("./country/neighbor"):
    print i
#     print i,i.tag,i.attrib
#     print i.get('name')

print "Nodes  that have a 'year' child "

for i in root.findall(".//year/.."):
    print i.tag,i.get('name'), i.attrib, i.items(),i.keys()
    
print"Nodes with name='Singapore' that have a 'year' child"

for i in root.findall(".//year/..[@name='Singapore']"):
    print i.tag,i.get('name'), i.attrib, i.items(),i.keys()
    
print 'oooooooooooooooooooooooooooooooooo'
for i in root.findall("./country/"):
    print i
