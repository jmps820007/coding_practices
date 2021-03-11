def count_products(data):
    products = {}
    for d in data:
        name, count = d.split(' ')
        count = int(count)
        if name in products:
            products[name] += count
        else:
            products[name] = count
    print(products)
    return products



data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
count_products(data)