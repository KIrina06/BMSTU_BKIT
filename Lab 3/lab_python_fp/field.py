def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        b = [item[i] for item in items for i in item if i == args[0] and item[i] is not None]
        return b
    else:
        b = [{i: item[i]} for item in items for i in item for arg in args if arg == i and item[i] is not None]
        return b