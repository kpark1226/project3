# project3

The instructions for project 3 can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03).

The python file titled `ebay.dl` contains codes to scrape information from ebay and to store the results in `.json` or `.csv` files. The files contain information about the `name` of the item, the `price` of the item in cents, the `status` of the item stating whether the item is "Brand New", "Refurbished", "Pre-owned", etc., the price of `shipping` in cents, a boolean value for whether the item has `free_returns`, and the number of `items_sold` (as an integer).

The following command runs the file of the specified search term:
```
$ python3 ebay-dl.py 'search term'
```
This will then generate a json file for the search term that includes the first 10 pages of the eBay search query. However, you are able to change how many pages to download with the following command:
```
$ python3 ebay-dl.py 'search term' --num_pages=3
```
Here, the code will run through the first 3 pages. 

The commands above generate `.json` files, and you can add `--csv` at the end of the command to create `.csv` files:
```
$ python3 ebay-dl.py 'search term' --csv
