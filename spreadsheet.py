from openpyxl import Workbook
from datetime import datetime as dt

'''
For processing the data and creating a sorted excel spreadsheet, we face a challenge:
The count of records obtained from each source is not equal, meaning in some days, we have the price for one stock, and
not for the other, so we can't iterate on all the lists at the same time, and write them in a spreadsheet. One way to
solve this problem would be to add all the data to another list with an insertion-sort approach.
'''


def generate_sheet(dictionary, sheet_name):
    totals = []

    print('Inserting dollar_price...')
    for price_list in dictionary['dollar_price']:
        if len(totals) == 0:
            # If the total list is empty, start appending items to it
            totals.append([price_list[1], price_list[0], '', '', '', '', '', '', '', ''])
        else:
            placed = False
            # If there are items in the total list, we should check it the date is already in the list or not
            for i in range(len(totals)):
                if dt.strptime(totals[i][0], '%Y/%m/%d') == dt.strptime(price_list[1], '%Y/%m/%d'):
                    # If the list has the date, just write the price in the right place
                    totals[i][1] = price_list[0]
                    placed = True
                    break
                elif dt.strptime(totals[i][0], '%Y/%m/%d') < dt.strptime(price_list[1], '%Y/%m/%d'):
                    # If the list doesn't have the date, but has dates after that, we need to insert the date and the
                    # price here
                    totals.insert(i, [price_list[1], price_list[0], '', '', '', '', '', '', '', ''])
                    placed = True
                    break
            if not placed:
                # If none of the conditions mentioned above are fulfilled, we will append the date and the value to the
                # end of the sheet
                totals.append([price_list[1], price_list[0], '', '', '', '', '', '', '', ''])

    # And then we repeat the mentioned for other stocks

    print('Inserting euro_price...')
    for price_list in dictionary['euro_price']:
        placed = False
        for i in range(len(totals)):
            if dt.strptime(totals[i][0], '%Y/%m/%d') == dt.strptime(price_list[1], '%Y/%m/%d'):
                totals[i][2] = price_list[0]
                placed = True
                break
            elif dt.strptime(totals[i][0], '%Y/%m/%d') < dt.strptime(price_list[1], '%Y/%m/%d'):
                totals.insert(i, [price_list[1], '', price_list[0], '', '', '', '', '', '', ''])
                placed = True
                break
        if not placed:
            totals.append([price_list[1], '', price_list[0], '', '', '', '', '', '', ''])

    print('Inserting dirham_price...')
    for price_list in dictionary['dirham_price']:
        placed = False
        for i in range(len(totals)):
            if dt.strptime(totals[i][0], '%Y/%m/%d') == dt.strptime(price_list[1], '%Y/%m/%d'):
                totals[i][3] = price_list[0]
                placed = True
                break
            elif dt.strptime(totals[i][0], '%Y/%m/%d') < dt.strptime(price_list[1], '%Y/%m/%d'):
                totals.insert(i, [price_list[1], '', '', price_list[0], '', '', '', '', '', ''])
                placed = True
                break
        if not placed:
            totals.append([price_list[1], '', '', price_list[0], '', '', '', '', '', ''])

    print('Inserting yuan_price...')
    for price_list in dictionary['yuan_price']:
        placed = False
        for i in range(len(totals)):
            if dt.strptime(totals[i][0], '%Y/%m/%d') == dt.strptime(price_list[1], '%Y/%m/%d'):
                totals[i][4] = price_list[0]
                placed = True
                break
            elif dt.strptime(totals[i][0], '%Y/%m/%d') < dt.strptime(price_list[1], '%Y/%m/%d'):
                totals.insert(i, [price_list[1], '', '', '', price_list[0], '', '', '', '', ''])
                placed = True
                break
        if not placed:
            totals.append([price_list[1], '', '', '', price_list[0], '', '', '', '', ''])

    print('Inserting crude_price...')
    for price_list in dictionary['crude_price']:
        placed = False
        for i in range(len(totals)):
            if dt.strptime(totals[i][0], '%Y/%m/%d') == dt.strptime(price_list[1], '%Y/%m/%d'):
                totals[i][5] = price_list[0]
                placed = True
                break
            elif dt.strptime(totals[i][0], '%Y/%m/%d') < dt.strptime(price_list[1], '%Y/%m/%d'):
                totals.insert(i, [price_list[1], '', '', '', '', price_list[0], '', '', '', ''])
                placed = True
                break
        if not placed:
            totals.append([price_list[1], '', '', '', '', price_list[0], '', '', '', ''])

    print('Inserting brent_price...')
    for price_list in dictionary['brent_price']:
        placed = False
        for i in range(len(totals)):
            if dt.strptime(totals[i][0], '%Y/%m/%d') == dt.strptime(price_list[1], '%Y/%m/%d'):
                totals[i][6] = price_list[0]
                placed = True
                break
            elif dt.strptime(totals[i][0], '%Y/%m/%d') < dt.strptime(price_list[1], '%Y/%m/%d'):
                totals.insert(i, [price_list[1], '', '', '', '', '', price_list[0], '', '', ''])
                placed = True
                break
        if not placed:
            totals.append([price_list[1], '', '', '', '', '', price_list[0], '', '', ''])

    print('Inserting opec_price...')
    for price_list in dictionary['opec_price']:
        placed = False
        for i in range(len(totals)):
            if dt.strptime(totals[i][0], '%Y/%m/%d') == dt.strptime(price_list[1], '%Y/%m/%d'):
                totals[i][7] = price_list[0]
                placed = True
                break
            elif dt.strptime(totals[i][0], '%Y/%m/%d') < dt.strptime(price_list[1], '%Y/%m/%d'):
                totals.insert(i, [price_list[1], '', '', '', '', '', '', price_list[0], '', ''])
                placed = True
                break
        if not placed:
            totals.append([price_list[1], '', '', '', '', '', '', price_list[0], '', ''])

    print('Inserting mazut_price...')
    for price_list in dictionary['mazut_price']:
        placed = False
        for i in range(len(totals)):
            if dt.strptime(totals[i][0], '%Y/%m/%d') == dt.strptime(price_list[1], '%Y/%m/%d'):
                totals[i][8] = price_list[0]
                placed = True
                break
            elif dt.strptime(totals[i][0], '%Y/%m/%d') < dt.strptime(price_list[1], '%Y/%m/%d'):
                totals.insert(i, [price_list[1], '', '', '', '', '', '', '', price_list[0], ''])
                placed = True
                break
        if not placed:
            totals.append([price_list[1], '', '', '', '', '', '', '', price_list[0], ''])

    print('Inserting global_gold_price...')
    for price_list in dictionary['global_gold_price']:
        placed = False
        for i in range(len(totals)):
            if dt.strptime(totals[i][0], '%Y/%m/%d') == dt.strptime(price_list[1], '%Y/%m/%d'):
                totals[i][9] = price_list[0]
                placed = True
                break
            elif dt.strptime(totals[i][0], '%Y/%m/%d') < dt.strptime(price_list[1], '%Y/%m/%d'):
                totals.insert(i, [price_list[1], '', '', '', '', '', '', '', '', price_list[0]])
                placed = True
                break
        if not placed:
            totals.append([price_list[1], '', '', '', '', '', '', '', '', price_list[0]])

    # Saving the totals list into an excel spreadsheet
    wb = Workbook()
    ws = wb.active
    ws.append(['Date', 'Dollar Price', 'Euro Price', 'Dirham Price', 'Yuan Price', 'Crude Price', 'Brent Price',
               'Opec Price', 'Mazut Price', 'Global Gold Price'])

    for item in totals:
        ws.append(item)

    wb.save(sheet_name)
