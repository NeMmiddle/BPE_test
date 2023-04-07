import collections

import requests

result = requests.get('https://python.org')
output_text = collections.Counter(result.text)

for symbol, quantity in sorted(output_text.items()):
    print(f'{symbol}: {quantity}')
