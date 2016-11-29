import xml.etree.ElementTree as ET

def loadConfig(xmlFile):

    config = {}
    config['Steps'] = []
    tree = ET.parse(xmlFile)
    root = tree.getroot()

    steps = root.findall('Step')

    for step in steps:
        config['Steps'].append(etree_to_dict(step))

    return config

def etree_to_dict(t):
    children = t.getchildren()
    # This is an "array" element with all the same children
    if len(children) > 0 and all(c.tag == children[0].tag for c in children):
        d = { 'items': [] }
        for child in children:
            d['items'].append(etree_to_dict(child))
    # This is a dictionary parent with different children
    elif len(children) > 0:
        d = {}
        for child in children:
            d[child.tag] = etree_to_dict(child)
    # This is a root node with no children and maybe some attributes
    else:
        d = {'Value' : t.text}
    attr = {k: v for k, v in t.attrib.iteritems()}
    if len(attr) > 0:
        d['attr'] = attr
    return d
