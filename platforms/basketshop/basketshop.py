import requests
from bs4 import BeautifulSoup


class Basketshop:
    def __init__(self):
        pass

    def parse(self) -> list:
        self.size = 11
        self.url = f"https://www.basketshop.ru/catalog/sale/oncourt/?size%5B0%5D={self.size}&sizechart=US"

        self.list_shoes = []
        self.r = requests.get(self.url)
        self.bs = BeautifulSoup(self.r.content)
        self.bs_all_product = self.bs.find('div', {'class': 'category__products'}).\
            find_all("div", {'class': 'product-card'})
        for self.bs_product in self.bs_all_product:
            self.list_shoes.append(
                {
                    'name': self.bs_product.find('span', {'itemprop': 'name'}).text,
                    'price': str(
                        self.bs_product.find('meta', {'itemprop': 'price'})['content']
                    ),
                    'image_url': self.bs_product.find('img', {'itemprop': 'image'})['data-src'],
                    'discount': str(
                        self.bs_product.find('div', {'class': 'product-card__label new'}).text.
                        replace('-', '').replace('%\t', '')
                    ),
                    'data_id': str(self.bs_product['data-id'])
                }
            )
        return self.list_shoes

if __name__ == "__main__":
    basketshop_client = Basketshop()
    basketshop_client.parse()