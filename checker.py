import os
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm


def check(xml):
      for url_el in tqdm(xml.find_all('url')):
            url_to_check = url_el.loc.string
            r = requests.head(url_to_check, allow_redirects=True)
            if r.status_code != 200:
                  print('BAD URL:', url_to_check, r)


if __name__ == '__main__':
      try:
            assert(len(os.sys.argv) >= 2)
            file_name = os.sys.argv[1]
      except:
            print('USAGE: python3 checker.py FILENAME')

      with open(file_name) as f:
            xml = BeautifulSoup(f.read(), 'lxml')
            check(xml)
