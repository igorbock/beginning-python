def dictionary_sorter(data_dict):
    # Write code here
    if data_dict == {}:
        return {}
    novo = sorted(data_dict.items(), key=lambda item: item[1])
    return dict(novo)    

print(dictionary_sorter({'a': 3, 'b': 1, 'c': 2}))
print(dictionary_sorter({}))