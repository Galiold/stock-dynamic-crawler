from selenium import webdriver
from crawler import crawl
from spreadsheet import generate_sheet
import os.path as path


prices = {}
start_date = '1398-07-01'
end_date = '1398-07-23'

file_name = start_date + 'to' + end_date
cur_dir = path.dirname(__file__)
out_dir = path.join(cur_dir, '../out')  # For saving the outpput in the out folder in the rot

if __name__ == '__main__':
    browser = webdriver.Chrome('./chromedriver')

    urls = {
        'dollar_price': 'http://www.tgju.org/chart/price_dollar_rl/2',
        'euro_price': 'http://www.tgju.org/chart/price_eur/2',
        'dirham_price': 'http://www.tgju.org/chart/price_aed/2',
        'yuan_price': 'http://www.tgju.org/chart/price_cny/2',
        'crude_price': 'http://www.tgju.org/chart/energy-crude-oil/2',
        'brent_price': 'http://www.tgju.org/chart/energy-brent-oil/2',
        'opec_price': 'http://www.tgju.org/chart/oil_opec/2',
        'mazut_price': 'http://www.tgju.org/chart/energy-heating-oil/2',
        'global_gold_price': 'http://www.tgju.org/chart/ons/2'
    }

    for url in urls:
        print('Fetching %s...' % urls[url])
        prices[url] = crawl(urls[url], browser, start_date, end_date)
        print('Fetching done\n')

    with open(path.join(out_dir, file_name + '.txt'), 'wt') as f:
        f.write(str(prices))

    generate_sheet(prices, path.join(out_dir, file_name + '.xlsx'))

    browser.quit()
