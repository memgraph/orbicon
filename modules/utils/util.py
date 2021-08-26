def merge_dicts(dict_1, dict_2):
    for key, value in dict_2.items():
        if key in dict_1 and dict_1[key] is not None and dict_1[key].is_processed:
            continue
        dict_1[key] = value
    return dict_1
