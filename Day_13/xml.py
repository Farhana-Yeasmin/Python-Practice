import xml.etree.ElementTree as ET

# Create the root element of the XML tree
root = ET.Element("people")

# Create some child elements and add them to the root element
person1 = ET.SubElement(root, "person")
name1 = ET.SubElement(person1, "name")
name1.text = "John"
age1 = ET.SubElement(person1, "age")
age1.text = "28"
city1 = ET.SubElement(person1, "city")
city1.text = "New York"

person2 = ET.SubElement(root, "person")
name2 = ET.SubElement(person2, "name")
name2.text = "Alice"
age2 = ET.SubElement(person2, "age")
age2.text = "23"
city2 = ET.SubElement(person2, "city")
city2.text = "London"

# Write the XML tree to a file
tree = ET.ElementTree(root)
tree.write("/home/farhana/Desktop/people.xml")



