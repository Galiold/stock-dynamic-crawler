from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import itertools


def crawl(url, browser, start_date, end_date):
    date_price = []
    crawling_done = False
    delay = 15  # seconds

    browser.get(url)

    '''
    In order to set the time interval, we need to send the start and end time to selectors in the website, to do so, we
    should wait for these elements to load completely and then send the data, we do this in a try/catch block.
    '''
    try:
        WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.ID, 'min')))
        beginning_time = browser.find_element_by_id('min')
        beginning_time.send_keys(start_date)
        beginning_time.send_keys(Keys.RETURN)

        WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.ID, 'max')))
        beginning_time = browser.find_element_by_id('max')
        beginning_time.send_keys(end_date)
        beginning_time.send_keys(Keys.RETURN)
    except exceptions.TimeoutException:
        print("Loading took too much time!")

    '''
    The tables holding the data in tgju.com consist of odd and even rows, after they are loaded we select both groups
    of them.
    '''
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr.even')))
    except exceptions.TimeoutException:
        print("Loading took too much time!")

    '''
    The tables in tgju only show up to 100 items in one page, so we need to grab the next button and select it after we
    have processed the data in the showing folder.
    '''
    next_btn = browser.find_element_by_css_selector('a#DataTables_Table_0_next.paginate_button.next')

    while True:
        rows_odd = browser.find_elements_by_css_selector('tr.odd')
        rows_even = browser.find_elements_by_css_selector('tr.even')

        '''
        Count of odd and even rows is not equal, so we use the zip_longest function to iterate on both of them up until
        the larger list finishes.
        '''
        for odd, even in itertools.zip_longest(rows_odd, rows_even):
            if even:
                columns = odd.find_elements_by_css_selector('td')
                date_price.append([columns[3].text, columns[4].text])
                columns = even.find_elements_by_css_selector('td')
                date_price.append([columns[3].text, columns[4].text])
            else:
                columns = odd.find_elements_by_css_selector('td')
                date_price.append([columns[3].text, columns[4].text])

        '''
        Crawling is finished when the next button is disabled, we set this flag to true upon seeing the disabled
        button
        '''
        if crawling_done:
            break

        next_btn.send_keys(Keys.RETURN)
        try:
            WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr.even')))
        except exceptions.TimeoutException:
            print("Loading took too much time!")
        next_btn = browser.find_element_by_css_selector('a#DataTables_Table_0_next.paginate_button.next')
        try:
            '''
            Here if we find the disabled button, we will set the crawling_done flag to true, and after that we run the
            algorithm one more time to collect the data from the last page.
            '''
            next_btn_disabled = browser.find_element_by_css_selector(
                'a#DataTables_Table_0_next.paginate_button.next.disabled')
            crawling_done = True
        except exceptions.NoSuchElementException:
            pass

    print('%s records fetched' % (len(date_price)))
    return date_price
