def remove_extra(ips_list):
    corrct_list = []
    for item in ips_list:
        if item not in corrct_list:
            corrct_list.append(item)
    return corrct_list
ips_list = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.15', 'y'),
    ('192.168.0.11', 'y')
]
result = remove_extra(ips_list)
print(result)