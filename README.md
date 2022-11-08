# project3

The instructions for project 3 can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03).

The python file titled `ebay.dl` contains codes to scrape information from ebay and to store the results in `.json` or `.csv` files. The files contain information about the `name` of the item, the `price` of the item in cents, the `status` of the item stating whether the item is "Brand New", "Refurbished", "Pre-owned", etc., the price of `shipping` in cents, a boolean value for whether the item has `free_returns`, and the number of `items_sold` (as an integer).

To run the python file, use the following command line:
```
$ python3 ebay-dl.py 'bouncy ball'
```
where `'bouncy ball'` can be replaced by the search term of your choice. If your search term contains multiple words, be sure to use quotation marks! By deafult, the program downloads the first 10 pages of the eBay search query. If you wish to adjust this to your fancy, simply use the following command line:
```
$ python3 ebay-dl.py 'bouncy ball' --num_pages=5
```
where `5` can be replaced by the number of pages you want. By deafult, the program downloads the search queries in `.json` format. If you wish to change the download format to `.csv`, simply add the command line flag `--csv` like below:
```
$ python3 ebay-dl.py 'bouncy ball' --csv
