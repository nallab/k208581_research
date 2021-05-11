# 階層が深いJsonData を引っ張り出すプログラム
def search(arg, cond):
    res = []
    if cond(arg):
        res.append(arg)
    if isinstance(arg, list):
        for item in arg:
            res += search(item, cond)
    elif isinstance(arg, dict):
        for value in arg.values():
            res += search(value, cond)
    return res

def has_start_key(arg):
    if isinstance(arg, dict):
        return arg.keys() == {"property","description"}

def get_start(arg):
    return search(arg, has_start_key)

# 値の
def get_value(list_datas):
    all_value = []
    for data in list_datas:
        prop_value = data['property']['value']
        desc_value = data['description']['value']
        all_value.append([prop_value, desc_value])
    return all_value