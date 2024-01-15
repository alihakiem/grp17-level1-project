company_ips = [
('192.168.0.15', 'y'),
('192.168.0.22', 'y'),
('192.168.0.14', 'y'),
('192.168.0.24', 'n'),
('192.168.0.15', 'y'),
('192.168.0.11', 'y')
]
company_ips_2 = []
for ip in company_ips:
    if ip not in company_ips_2:
        company_ips_2.append(ip)
print(company_ips_2)
