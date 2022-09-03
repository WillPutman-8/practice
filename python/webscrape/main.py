from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-gaming-z-trio-10g-lhr/p/N82E16814137677?Description=" \
      "rtx%203080&cm_re=rtx_3080-_-14-137-677-_-Product&quicklink=true"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)