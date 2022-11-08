import argparse
import requests
from bs4 import BeautifulSoup
import json
import csv

def parse_itemssold(text):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string.

    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text: 
        return int(numbers) 
    else: 
        return None

def parse_price(text):
    numbers=''
    if text[0]=='$':
        for char in text:
            if char in '1234567890':
                numbers+=char
            elif char==' ':
                break
        return int(numbers)
    else:
        return None


def parse_shipping(text):
    numbers=''
    if text[0]=='+':
        for char in text:
            if char in '1234567890':
                numbers+=char
            elif char==' ':
                break
        return int(numbers)
    else:
        return 0

if __name__ == '__main__':

    # get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON.')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages', default=10)
    parser.add_argument('--csv', action='store_true')
    args = parser.parse_args()
    print('args.search_term=', args.search_term)

    # list of all items found in all ebay webpages
    items = []

    # loop over the ebay webpages
    for page_number in range(1,int(args.num_pages)+1):

        # build the url
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
        url += args.search_term
        url +='&_sacat=0&LH_TitleDesc=0&_pgn='
        url += str(page_number)
        url += '&rt=nc'
        print('url=',url) 

        # download the html
        r = requests.get(url)
        status = r.status_code
        print('status=', status)
        html = r.text

        # process the html
        soup = BeautifulSoup(html, 'html.parser')

        # loop over the items in the page
        tags_items = soup.select('.s-item')
        for tag_item in tags_items:

            tags_name = tag_item.select('.s-item__title')
            name = None
            for tag in tags_name:
                name = tag.text

            tags_free_returns = tag_item.select('.s-item__free-returns')
            free_returns = False
            for tag in tags_free_returns: 
                free_returns = True

            tags_price = tag_item.select('.s-item__price')
            price = None
            for tag in tags_price:
                price = parse_price(tag.text)

            tags_status = tag_item.select('.SECONDARY_INFO')
            status = None
            for tag in tags_status:
                status = tag.text

            items_sold = None
            tags_itemssold = tag_item.select('.s-item__hotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)

            tags_shipping=tag_item.select('.s-item__shipping, .s-item__freeXDays')
            shipping=None
            for tag in tags_shipping:
                shipping = parse_shipping(tag.text)

            item = {
                'name': name,
                'free_returns': free_returns,
                'price': price,
                'status': status,
                'shipping': shipping,
                'items_sold': items_sold,
            }
            items.append(item)

    #print('len(tags_items)=', len(tags_items))
    #print('len(items)', len(items))

    filename='_'.join(args.search_term.split(' '))
    if args.csv:
        with open(filename+'.csv', 'w') as f:
            header=items[0].keys()
            writer = csv.DictWriter(f, fieldnames = header)
            writer.writeheader()
            writer.writerows(items[1:])
                
    else:
        with open(filename+'.json', 'w', encoding='ascii') as f:
            f.write(json.dumps(items[1:]))