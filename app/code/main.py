url = 'https://www.1mg.com/drugs/sinarest-new-tablet-648652'

import requests
from bs4 import BeautifulSoup

# html = requests.get(url).content  # load cached instead
html = open('page.html', 'rb').read()
bs = BeautifulSoup(html, 'html5lib')

ids = ('product_introduction', 'product_uses', 'product_benefits', 'side_effects', 'how_to_use', 'how_works', 'product_substitutes', 'quick_tips', 'safety_advice')

for i in ids:
    info = bs.find(id=i).find_next_sibling("div")
    globals()[i] = info.text

# product_introduction = product_introduction.text
# assert product_introduction[:20] == 'Product introduction'
# product_introduction = product_introduction[20:]

# product_uses = product_uses.text
# product_uses = [i.strip() for i in product_uses.split('\n') if i.strip()]
# assert product_uses[0].startswith('Uses of')
# product_uses = product_uses[1:]

product_benefits

data = {i: eval(i) for i in ids}
print(data)