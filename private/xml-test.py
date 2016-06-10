from lxml import etree


def key2value_str(key, value):
    return "'" + key + "':'" + str(value) + "'"


assert key2value_str('_id', 123456) == "'_id':'123456'"


def lamoda_pathandfile(url):
    return url[19:]


def node2json(node):
    rez = "{"
    # print(node.tag, node.keys(), node.values())
    rez += key2value_str('_id', node.get('id')[:14])
    pictures_mode = False
    for subnode in node:
        # print(subnode.tag, subnode.keys(), subnode.values(), subnode.text)
        if pictures_mode and subnode.tag != 'picture':
            pictures_mode = False
            rez = rez + "]"
        if subnode.tag == 'market_category' or subnode.tag == 'typePrefix' or subnode.tag == 'description':
            rez = rez + ',' + key2value_str(subnode.tag, subnode.text)
        elif subnode.tag == 'picture':
            fp.write(lamoda_pathandfile(subnode.text) + "\n")
            if pictures_mode:
                rez = rez + ",'" + subnode.text + "'"
            else:
                pictures_mode = True
                rez = rez + ",'pictures':['" + subnode.text + "'"
        elif subnode.tag == "param" and len(subnode.keys()) != 2:
            rez = rez + "," + key2value_str(subnode.values()[0].lower(), subnode.text)

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
tree = etree.parse('database-lamoda.xml')
# tree = etree.parse('minibase-lamoda.xml')
nodes = tree.xpath('/yml_catalog/shop/offers/offer')
folded_nodes = {}
prices = {}
sizes = {}
jsons = {}
issues_count=0
print(len(nodes))
fb = open("../server/minibase200.js", "w")
fp = open("pictures.txt", "w")
fb.write("objects=[\n")
for i in range(len(nodes)):  # Перебираем элементы
    # fb.write(node2json(nodes[i]))
    # fb.write(",\n")
    # print(node2json(nodes[i]))
    current = nodes[i].get('id')[:14]
    current_price = issue_price(nodes[i])
    current_size = issue_size(nodes[i])
    if current not in folded_nodes:
        issues_count+=1
        if issues_count>200:
            break
        folded_nodes[current] = 1
        prices[current] = current_price
        sizes[current] = current_size
        jsons[current] = node2json(nodes[i])
    else:
        folded_nodes[current] += 1
        if current_price > prices[current]:
            prices[current] = current_price
        sizes[current] = sizes[current] + "," + current_size
    print(current, issue_price(nodes[i]), issue_size(nodes[i]), jsons[current])  # nodes[i].get('id'),

    # folded_nodes[i]=folded_nodes[i]+1
print(len(folded_nodes))
print(folded_nodes)
print(prices)
print(sizes)

for current in folded_nodes.keys():
    json = jsons[current] + ",'price':'" + str(prices[current]) + "','sizes':[" + sizes[current] + "]}"
    print(json)
    if current != list(folded_nodes.keys())[-1]:
        fb.write(json + ",\n")
    else:
        fb.write(json + "\n")

fb.write("];")
fb.close()
fp.close()
