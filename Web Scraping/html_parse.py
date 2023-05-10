import urllib.request
import re
import os
import xml.etree.ElementTree as ET
import json

def parseTable(html):
    html = sanitization(html)
    pattern = re.compile("(<tr><td>.+?tr>)")
    rowList = re.findall(pattern,html)

    dataList = [[]]

    addressList = []

    # addressDict = {
    #     "Address":[],
    #     "City":[],
    #     "State":[]
    # }
    addressDict = {}

    for row in rowList:
        dataMatcherRegex = "<tr><td>(.+?)<\/td><td>(.+?)<\/td><td>(.+?)<\/td><td>"
        """
        => To use the group() function first search the regex then use it otherwise
        """
        dataMatcher = re.search(dataMatcherRegex,row)
        if dataMatcher:
            address = dataMatcher.group(1)
            city = dataMatcher.group(2)
            state = dataMatcher.group(3)

            """
            => use findall() it will return a list then iterate it to get the data
            """    
            # addressDict["Address"].append(address)
            # addressDict["City"].append(city)
            # addressDict["State"].append(state)
            
            addressDict = {
                "Address": address,
                "City": city,
                "State": state
            }
            addressList.append(addressDict)

        # print(addressDict)    

        # dataMatcher = re.findall(dataMatcherRegex,row)
        # for data in dataMatcher:
        #     address = data[0]
        #     city = data[1]
        #     state = data[2]
            
            dataList.append([address,city,state])
            # print(dataList)
    
    print(json.dumps(addressList))
    saveDataToCSV(dataList)
    saveDataToXML(dataList)            


def sanitization(html):
    sanitizeRegex = re.compile("<table.*?<\/td><\/tr>")
    html = sanitizeRegex.sub(" ",html)
    return html


def saveDataToXML(dataList):
    root = ET.Element("Info")
    for record in dataList:
        if(record):
            address1 = ET.SubElement(root, "addressInfo")
            addres = record[0]
            state = record[1]
            city = record[2]

            lineAddress = ET.SubElement(address1, "lineAddress")
            lineAddress.text = addres

            states = ET.SubElement(address1, "State")
            states.text = state

            cities = ET.SubElement(address1, "City")
            cities.text = city
        
        tree = ET.ElementTree(root)
        tree.write("/home/farhana/Desktop/info.xml")
        

def saveDataToCSV(dataList):
    # filePath="/home/farhana/Desktop/All Python/factoryOutput.csv"
    # ourFile = open(filePath,"w")

    directoryPath="/home/farhana/Desktop/All Python"
    filePath = os.path.join(directoryPath,"demo.csv")
    
    ourFile = open(filePath,"w")

    # Write the heading
    ourFile.write("Address, City, State")

    for record in dataList:
        for item in record:
            itemAsString =  str(item)
            ourFile.write(itemAsString)
            ourFile.write(",")
        ourFile.write("\n")
    ourFile.close()            


url = "https://www.summet.com/dmsi/html/codesamples/simpleTable.html"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html_bytes = response.read()
html = html_bytes.decode()
dataTable = parseTable(html)