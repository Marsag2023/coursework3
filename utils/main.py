from functions import json_operations, sort_operations, print_result

file_convert = json_operations()
data_operations = sort_operations(file_convert)
for dat in data_operations:
    print_result(dat)
