from lxml import etree

def node2json(node):
    rez="{\n"
    print(node.tag, node.keys(), node.values())
    print('id =', node.get('id'))
    # if len(node)!=25:
    #     print(len(node))
    for subnode in node:
        # print(subnode.tag)
        print(subnode.tag, subnode.keys(), subnode.text)
    rez=rez+"}\n"
    return rez
#yml parser
#tree = etree.parse('database-lamoda.xml')
tree = etree.parse('minibase-lamoda.xml')
nodes = tree.xpath('/yml_catalog/shop/offers/offer')
fb = open("database.js","w")
fb.write("database={")
for node in nodes:  # Перебираем элементы
    node2json(node)
    break

fb.write("};")



