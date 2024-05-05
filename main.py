import requests
import pprint
import time
import threading
import keyboard

def request_for_bitget():
    urlETCBTC = 'https://api.bitget.com/api/v2/spot/market/orderbook?symbol=ETCBTC&type=step0&limit=100'
    urlBTCUSDT = 'https://api.bitget.com/api/v2/spot/market/orderbook?symbol=BTCUSDT&type=step0&limit=100'
    urlETCUSDT = 'https://api.bitget.com/api/v2/spot/market/orderbook?symbol=ETCUSDT&type=step0&limit=100'
    responseETCBTC = requests.get(urlETCBTC)
    responseBTCUSDT = requests.get(urlBTCUSDT)
    responseETCUSDT = requests.get(urlETCUSDT)
    dataETCBTC = responseETCBTC.json()
    dataBTCUSDT = responseBTCUSDT.json()
    dataETCUSDT = responseETCUSDT.json()
    data = { 
        "BTCUSDT" :
        dataETCBTC,
        "ETHUSDT" :
        dataBTCUSDT,
        "ETHBTC" :
        dataETCUSDT
    }
    return data

stop = True
def continuous_function():
    global stop
    while stop:
        data_from_bitget = request_for_bitget()
        pprint.pprint(data_from_bitget)
        time.sleep(5)

def stop_function():
    global stop
    while stop:
        if keyboard.is_pressed('q'):
            stop = False
    print("Оба потока остановлены.")



thread1 = threading.Thread(target=continuous_function)
thread2 = threading.Thread(target=stop_function)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
