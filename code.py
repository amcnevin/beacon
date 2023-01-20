import os

import socketpool
import wifi
import microcontroller
import json

from adafruit_httpserver.server import HTTPServer
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.server import HTTPMethod
from adafruit_httpserver.status import HTTPStatus, CommonHTTPStatus


from beacon import Beacon
from color import Color
from action import ActionFactory

ssid = os.getenv("CIRCUITPY_WIFI_SSID")
pwd = os.getenv("CIRCUITPY_WIFI_PASSWORD")

print("")
print("Connecting to", ssid)
wifi.radio.connect(ssid, pwd)
print("Connected to", ssid)
print(f"Listening on http://{wifi.radio.ipv4_address}:80")

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)
beacon = Beacon()


@server.route("/beacon", method=HTTPMethod.POST)
def update_beacon(request):

    try:
        print(request.body)
        body = json.loads(request.body)
        print(body)
        action = ActionFactory.build(body)

        beacon.process_action(action)

        value = ""
        status = CommonHTTPStatus.OK_200
    except ValueError as ve:
        value = f"Bad Request: {ve}"
        status = CommonHTTPStatus.BAD_REQUEST_400

    return HTTPResponse(body=value, status=status)


@server.route("/health")
def get_health(request):
    status = {}

    status["health"] = "GREEN"
    status["enabled"] = beacon.enabled
    status["temp"]= microcontroller.cpu.temperature
    status["frequency"] = microcontroller.cpu.frequency
    status["voltage"] = microcontroller.cpu.voltage
    return HTTPResponse(body=json.dumps(status))



print("Server Starting")
# Never returns
server.serve_forever(str(wifi.radio.ipv4_address))

print("Server Shutting down....")