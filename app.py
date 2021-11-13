import requests
from flask import *
from lxml import html
import json

# http://127.0.0.1:7777/get-car-info?brand=mercedes-benz&city=almaty&type=cars example url

app = Flask(__name__)


@app.route('/get-car-info', methods=['GET'])
def get_car_info():
    brand = request.args.get('brand')
    city = request.args.get('city')
    car_type = request.args.get('type')
    page = request.args.get('page')

    return get_info(brand, city, car_type, page)


def clean_price_xpath(prices_xpath):
    prices = []
    for price in prices_xpath:
        if price != '₸':
            prices.append(price.replace(u'\xa0', '').strip())
    return prices


def get_info(brand, city, car_type, page):
    if page is None:
        url = f'{car_type}/{brand}/{city}/'
    else:
        url = f'{car_type}/{brand}/{city}/?page={page}'

    r = requests.get(f'https://kolesa.kz/{url}')
    tree = html.fromstring(r.content)

    titles = [title.strip() for title in tree.xpath(
        '//span[@class="a-el-info-title"]//text()')]

    prices = clean_price_xpath(tree.xpath(
        '//span[@class="price"]//text()'))

    params = [param.strip() for param in tree.xpath(
        '//div[@class="a-search-description"]//text()')]

    pictures = tree.xpath('//div[@class="pictures-list pictures-slider more-five"]/picture//img/@src')

    del pictures[0:3]

    result = []

    for index in range(len(titles)):
        if index < len(pictures):
            car_info = {'title': titles[index],
                        'price': prices[index],
                        'params': params[index],
                        'picture': pictures[index]}
            result.append(car_info)

    return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
