import xml.etree.ElementTree as ET
tree = ET.parse('xml_data.xml')
root = tree.getroot()

#print root.getchildren()[1].getchildren()
for i in root.getchildren():
    print i.getchildren()
    
print'llloooooooooooooooooooooooooooo'
for i in root.findall("./country/neighbor"):
    print i,i.tag,i.attrib
    print i.get('name')
