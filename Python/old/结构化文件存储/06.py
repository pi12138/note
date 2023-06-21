import xml.etree.ElementTree as et

etree = et.ElementTree()
# help(et.ElementTree)

e = et.Element("Student")

etree._setroot(e)

e_name = et.SubElement(e, 'name')
e_name.text = 'zyp'

e_age = et.SubElement(e, 'age')
e_age.text = '20'


etree.write('v06.xml')



