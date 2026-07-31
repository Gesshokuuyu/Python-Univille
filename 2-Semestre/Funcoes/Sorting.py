def sortValues(values:list, type = 'ASC'):
    reverse = False
    if(type == "DESC"):
            reverse = True

    return sorted(values, reverse=reverse)

print(sortValues([1,5,7,9,2,3,6], "DESC"))