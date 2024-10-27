def labeled(data):
    data['Prediction'] = data['Close'].shift(-1)
    data.dropna(inplace=True)
    return data
