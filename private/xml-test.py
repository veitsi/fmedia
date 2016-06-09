from lxml import etree


def key2value_str(key, value):
    return "'" + key + "':'" + str(value) + "'"


assert key2value_str('_id', 123456) == "'_id':'123456'"


def node2json(node):
    rez = "{"
    # print(node.tag, node.keys(), node.values())
    rez += key2value_str('_id:', node.get('id'))
    # if len(node)!=25:
    pictures_mode = False
    for subnode in node:
        # print(subnode.tag, subnode.keys(), subnode.values(), subnode.text)
        if pictures_mode and subnode.tag != 'picture':
            pictures_mode = False
            rez = rez + "]"
        if subnode.tag == 'market_category' or subnode.tag == 'typePrefix' or subnode.tag == 'description':
            rez = rez + ',' + key2value_str(subnode.tag, subnode.text)
        elif subnode.tag == 'picture':
            if pictures_mode:
                rez = rez + ",'" + subnode.text + "'"
            else:
                pictures_mode = True
                rez = rez + ",pictures:['" + subnode.text + "'"
        elif subnode.tag == "param":
            rez = rez + "," + key2value_str(subnode.values()[0], subnode.text)
    rez = rez + "}"
    return rez


def issue_size(node):
    for subnode in node:
        if len(subnode.values()) == 2:
            return subnode.text


def issue_price(node):
    for subnode in node:
        if subnode.tag == 'price':
            return float(subnode.text)


# yml parser
# tree = etree.parse('database-lamoda.xml')
tree = etree.parse('minibase-lamoda.xml')
nodes = tree.xpath('/yml_catalog/shop/offers/offer')
folded_nodes = {}
prices = {}
sizes = {}
print(len(nodes))
fb = open("database.js", "w")
fb.write("var objects=[\n")
for i in range(len(nodes)):  # Перебираем элементы
    # fb.write(node2json(nodes[i]))
    # fb.write(",\n")
    # print(node2json(nodes[i]))
    current = nodes[i].get('id')[:14]
    current_price = issue_price(nodes[i])
    current_size = issue_size(nodes[i])
    if current not in folded_nodes:
        folded_nodes[current] = 1
        prices[current] = current_price
        sizes[current] = current_size
    else:
        folded_nodes[current] += 1
        if current_price > prices[current]:
            prices[current] = current_price
        sizes[current] = sizes[current] + "," + current_size
    print(nodes[i].get('id'), current, issue_price(nodes[i]), issue_size(nodes[i]))

print(len(folded_nodes))
print(folded_nodes)
print(prices)
print(sizes)
fb.write("];")
fb.close()
