import os

import socketpool
import wifi
import microcontroller
import json

from adafruit_httpserver.server import HTTPServer
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.server import HTTPMethod
from adafruit_httpserver.status import HTTPStatus, CommonHTTPStatus

from service import BeaconService
from repository import BeaconRepository


ssid = os.getenv("CIRCUITPY_WIFI_SSID")
pwd = os.getenv("CIRCUITPY_WIFI_PASSWORD")

print("")
print("Connecting to", ssid)
wifi.radio.connect(ssid, pwd)
print("Connected to", ssid)
print(f"Listening on http://{wifi.radio.ipv4_address}:80")

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)
# Inversion of Control
repo = BeaconRepository()
service = BeaconService(repo)

@server.route("/beacon", method=HTTPMethod.POST)
def update_beacon(request):
    """
    POST to update the beacon
    """
    try:
        action = json.loads(request.body)
        # TODO add action validation
        print(action)
        service.process_action(action)
        value = "OK"
        status = CommonHTTPStatus.OK_200
    except ValueError as ve:
        value = f"Bad Request: {ve}"
        status = CommonHTTPStatus.BAD_REQUEST_400

    response = HTTPResponse(request=request, status=status)
    return response.send(body=value)


@server.route("/health")
def get_health(request):
    # TODO move this to a HealthProvider or HealthIndicator pattern
    status = {}
    # TODO determine what constitutes a YELLOW or RED state? maybe enabled?
    status["health"] = "GREEN"
    status["enabled"] = service.is_enabled()
    status["temp"] = microcontroller.cpu.temperature
    status["frequency"] = microcontroller.cpu.frequency
    status["voltage"] = microcontroller.cpu.voltage
    response = HTTPResponse(request=request, status=CommonHTTPStatus.OK_200)
    return response.send(body=json.dumps(status))



print("Server Starting")
# Never returns
server.serve_forever(str(wifi.radio.ipv4_address))

print("Server Shutting down....")