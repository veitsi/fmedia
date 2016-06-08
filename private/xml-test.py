from lxml import etree


def key2value_str(key, value):
    return "'" + key + "':'" + str(value) + "'"


assert key2value_str('_id', 123456) == "'_id':'123456'"


def node2json(node):
    rez = "{"
    #print(node.tag, node.keys(), node.values())
    rez += key2value_str('_id:', node.get('id') )
    # if len(node)!=25:
    for subnode in node:
        # print(subnode.tag)
        if subnode.tag == 'price' or subnode.tag=='market_category' or subnode.tag=='typePrefix' or subnode.tag=='description':
            rez =rez+','+key2value_str(subnode.tag, subnode.text)
        print(subnode.tag, subnode.keys(), subnode.text)
    rez = rez + "}\n"
    return rez


# yml parser
# tree = etree.parse('database-lamoda.xml')
tree = etree.parse('minibase-lamoda.xml')
nodes = tree.xpath('/yml_catalog/shop/offers/offer')
fb = open("database.js", "w")
fb.write("var objects={")
for node in nodes:  # Перебираем элементы
    print(node2json(node))
    break

fb.write("};")
fb.close()
