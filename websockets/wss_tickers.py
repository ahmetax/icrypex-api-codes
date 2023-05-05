import websocket
import json
import time

def on_open(ws):
    print("on_open")

    subscribe={
        "c":"tickers",
        "s":True
    }

    ws.send("subscribe|"+json.dumps(subscribe))

def on_message(ws, message):
    print('on_message')
    if not message.startswith("tickers"):
        # print(message)
        return
    message=message[8:]
    obj = json.loads(message)
    for r in obj['t']:
        # print(r)
        # pair, price, volume, 24hr change
        print(f"{r['ps']:10} {float(r['p']):18.10f} {float(r['v']):15.4f} {float(r['cp']):8.2f}%")
    time.sleep(2)
    # ws.close()

def on_error(ws, error):
    print("on_error")
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("on_close")


if __name__ == "__main__":
    url = "wss://istream.icrypex.com"
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.run_forever()
