from lxml import etree

#os parser
# tree = etree.parse('1.xml')
# nodes = tree.xpath('/soft/os/item')  # Открываем раздел
# for node in nodes:  # Перебираем элементы
#     print(node.tag, node.keys(), node.values())
#     print('name =', node.get('name'))  # Выводим параметр name
#     print('text =', [node.text])  # Выводим текст элемента

#yml parser
#tree = etree.parse('minibase-lamoda.xml')
tree = etree.parse('database-lamoda.xml')
nodes = tree.xpath('/yml_catalog/shop/offers/offer')
for node in nodes:  # Перебираем элементы
    print(node.tag, node.keys(), node.values())
    print('id =', node.get('id'))
    if len(node)!=25:
        print(len(node))
    # for subnode in node:
    #     # print(subnode.tag)
    #     print(subnode.text)



