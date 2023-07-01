import json
import machine
import time
import project_secrets
from mqtt_adapter import MQTT

# Setup pins
Pin = machine.Pin
led = Pin("LED", Pin.OUT)
photoresistor = machine.ADC(Pin(27, Pin.IN))

# Variables
mqtt_client = MQTT()


# Reset the board
def reset():
    print("Resetting board...")
    time.sleep(3)
    machine.reset()


def led_toggle(value):
    if value == 1:
        led.value(value)
    else:
        led.value(value)


def get_photoresistor_value():
    photoresistor_value = photoresistor.read_u16()
    print("Photoresistor value: ", photoresistor_value)

# def send_data_to_endpoint(temperature, humidity):
#     time.sleep(1)
#     sensor_data_temp_and_humidity = json.dumps({"feeds":{"temp": temperature, "humidity": humidity}})
#     try:
#         mqtt_client.publish(
#             project_secrets.MQTT_PUBLISH_GROUP_T_H, str(sensor_data_temp_and_humidity)
#         )
#         print("pushed data")
#     except Exception as e:
#         print(f"Failed to publish message: {e}")


# Read DHT11 sensor
def dht_sensor():
    import dht
    d = dht.DHT11(Pin(11))
    d.measure()
    print("Temperature: ", d.temperature())
    print("Humidity: ", d.humidity())
    # send_data_to_endpoint(d.temperature(), d.humidity())

def blink_sequence():
    time.sleep(1)
    led_toggle(1)
    time.sleep(1)
    led_toggle(0)
    time.sleep(1)
    led_toggle(1)
    time.sleep(2)
    led_toggle(0)   

# Main loop
def main():
    blink_sequence()
    # mqtt_client.connect()
    get_photoresistor_value()
    dht_sensor()
   


if __name__ == "__main__":
    while True:
        main()
