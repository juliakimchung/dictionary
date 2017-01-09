stockDict = { 'GM': 'General Motors', 'CAT': 'Caterpillar', 'EK': 'Eastman Kodak'}

purchases = [( 'GM', 100, '10-sep-2001', 48), ('CAT', 100, '1-apr-1999', 24), ('EK', 200, '1-jul-1998', 56)]
ticker1 = str(purchases[0][1] * purchases[0][3])
ticker2 = str(purchases[1][1] * purchases[1][3])
ticker3 = str(purchases[2][1] * purchases[2][3])
print(ticker1)
print(stockDict['GM'])
purchase_history = {'General Motors': ticker1, 'Caterpiller': ticker2, 'Eastman Kodak': ticker3}
new_print = {"I have purchased " + k + " stock for $" + v for (k, v) in purchase_history.items()}
print(new_print)

new_purchase_history = { 'GM': str(48), 'CAT': str(24), 'EK': str(56)}
new_purchase_print = { "I have " + k + "'s " + v + " stocks" for (k, v) in new_purchase_history.items()}
print(new_purchase_print)