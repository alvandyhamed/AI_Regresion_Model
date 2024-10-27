from Classes.PerdictionPrice import PredictionPrice

stock_symbol = input("Symbole مورد نظر خود را وارد کنید  ")

perdict = PredictionPrice(stock_symbol, '2020-01-01', '2024-01-01')

perdict.run()
