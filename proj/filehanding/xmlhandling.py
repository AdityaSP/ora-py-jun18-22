import xml.dom.minidom as dom
import pdb
pdb.set_trace()

doc_model = dom.parse('persons.xml')
persons = doc_model.getElementsByTagName('Person')

for person in persons:
    print "-" * 30
    children = [child for child in person.childNodes if child.nodeType == 1]
    for child in children:
        print child.nodeName, child.childNodes[0].data

# person = persons[0]
# print persons
# children = person.childNodes
# print children
# for child in children:
#     #print dir(child)
#     if child.nodeType == 1:
#         print child.nodeName, child.childNodes[0].data