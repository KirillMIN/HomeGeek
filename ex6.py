
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
product = []
num = 0
while True:

    control = input("For quit  0, for continue  Enter, for analytics Y")
    if control == '0':
        break
    num = num + 1
    if control == 'Y':
        print(f'\n  analytics \n {"*" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feat = input(f'Input feature "{f}"')
        features[f] = int(feat) if (f == 'price' or f == 'quantity') else feat
        analytics[f].append(features[f])
    product.append((num, features))
