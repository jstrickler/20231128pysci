import lxml.etree as et

tree = et.parse('DATA/solar.xml')
print(f"tree: {tree}")

root = tree.getroot()
print(f"root: {root}")
for element in root:
    if 'planets' in element.tag:
        for planet in element.findall('planet'):
            print(planet.get('planetname'))
            for moon in planet.findall('moon'):
                print(f"    {moon.text}")