import xml.etree.ElementTree as etree

tree = etree.parse("/home/farhana/Desktop/csv/phoneBook.xml")
root = tree.getroot()
# Print the tag name of the root
# print(root.tag)


# Iterate through all the root's children
for child in root:
    # print the name attribute form the name dictionary
    # print(child.attrib.get['name'])
    # print(child.tag,child.text)

    # finding all the sub tag
    names=child.findall("person")
    for i in names:
        # printing all the names and phone number
        print(i.attrib['name']," ",i.text) 

#     # Print salary attribute if any
#     # print(child.attrib.get('salary',"N\/A"))

#     vps = child.findall("vp")
#     print(vps)

#     for vp in vps:
#       print("   " + vp.attrib['name'])
#       print("   -" + vp.text)