import xmlschema


def parse(obj, xml):
    xsd = xmlschema.XMLSchema("calculations/pace.xsd-")
    xsd.validate(xml)
    xml = xsd.to_dict(xml, dict_class=dict, decimal_type=float)
    for key, value in xml.items():
        setattr(obj, key, value)
        # print(key, " -> ", value)
    return obj
