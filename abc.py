import time
from tb_gateway_mqtt import TBGatewayMqttClient
gateway = TBGatewayMqttClient("localhost", "EZyncKnyhRUTADg8RvJs")
gateway.connect()
gateway.gw_connect_device("Test Device A2")

gateway.gw_send_telemetry("Test Device A2", {"ts": int(round(time.time() * 1000)), "values": {"temperature": 42.2}})
gateway.gw_send_attributes("Test Device A2", {"firmwareVersion": "2.3.12"})

gateway.gw_disconnect_device("Test Device A2")
gateway.disconnect()
