def analisa_data(data):

    aux = data.rsplit('/')[::-1]
    data_reverse = ''
    for d in aux:
        data_reverse += d+'-'

    return data_reverse[:len(data_reverse)-1]

def analisa_info(info):
    print(info)