import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Format price')
    parser.add_argument('price', type=str, help='input image name')
    return parser.parse_args()


def get_format_price(price):
    return '{:,.2f}'.format(float(price)).replace(',', ' ').replace('.00', '')

if __name__ == '__main__':
    args = get_args()
    price = args.price
    print(get_format_price(price))
