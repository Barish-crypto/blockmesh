with open('proxies.txt', 'r') as f:
    proxies = f.readlines()

with open('proxies.txt', 'w') as f:
    for proxy in proxies:
        f.write('http://' + proxy)
