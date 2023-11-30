import lxml.etree as et

root = et.Element('knights')
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight = et.SubElement(root, "knight", title=title)
        knight_name = et.SubElement(knight, 'knight_name')
        knight_name.text = name
        et.SubElement(knight, 'color').text = color
        et.SubElement(knight, 'quest').text = quest
        et.SubElement(knight, 'comment').text = comment

xml_doc = et.tostring(root, pretty_print=True, xml_declaration=True).decode()
print(xml_doc)

tree = et.ElementTree(root)
tree.write('knights.xml', pretty_print=True, xml_declaration=True)
