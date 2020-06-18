from xml.etree import ElementTree

class ParseXML():
    def __init__(self,xmlPath):
        self.xmlPath = xmlPath
    
    def _getRoot(self):
        tree = ElementTree.parse(self.xmlPath)
        return tree.getroot()
    
    def findNodeByName(self,parentNode,nodeName):
        nodes = parentNode.findall(nodeName)
        return nodes
    
    def getNodeOfChildText(self,node):
        childrenTextDict = {i.tag:i.text for i in list(node.iter())[1:]}        
#         childrenTextDict={}
#         for i in list(node.iter())[1:]:
#             childrenTextDict[i.tag] = i.text            
        return childrenTextDict
    
    def getDataFromXml(self):
        root = self._getRoot()
        books = self.findNodeByName(root, "book")
        dataList = []
        for book in books:
            childrenText = self.getNodeOfChildText(book)
            dataList.append(childrenText)
        return dataList

if __name__ == '__main__':
    xml = ParseXML("./TestData.xml")
    datas = xml.getDataFromXml()
    print(datas)
    for i in datas:
        print(i["name"])