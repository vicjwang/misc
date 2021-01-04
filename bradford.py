import argparse
import matplotlib.pyplot as plt
import requests
from collections import Counter
from bs4 import BeautifulSoup


SQ_10K = 'https://www.sec.gov/Archives/edgar/data/1512673/000162828020002303/sq-20191231.htm'



def main(url):
    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    numbers = [d for d in soup.get_text() if d.isdigit()]

    freq = Counter()
    for number in numbers:
        freq.update(number[0])

    del freq['0']

    x = []
    y = []
    print(freq)
    for i in range(1, 10):
        num = freq[str(i)]
        denom = sum(freq.values())
        print(i, num/denom)

        x.append(i)
        y.append(num/denom)

    plt.bar(x, y)
    plt.show()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url')

    args = parser.parse_args()
    url = args.url
    main(url)
