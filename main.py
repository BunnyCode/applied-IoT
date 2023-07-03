import json
import machine
import time
import project_secrets
from mqtt_adapter import MQTT
from stemma_soil_sensor import StemmaSoilSensor

# Setup pins
Pin = machine.Pin
led = Pin("LED", Pin.OUT)
photoresistor = machine.ADC(Pin(27, Pin.IN))

# Variables
# mqtt_client = MQTT()


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
    # set a percentage value for the photoresistor
    photoresistor_value = photoresistor.read_u16() / 65535 * 100
    photoresistor_percentage = "%.2f" % photoresistor_value
    return photoresistor_percentage
    

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

def soil_sensor():
    SDA_PIN = Pin(14)
    SCL_PIN = Pin(15)
    i2c = machine.I2C(1, sda=SDA_PIN, scl=SCL_PIN, freq=400000)
    seesaw = StemmaSoilSensor(i2c)

    # get moisture
    moisture = seesaw.get_moisture() / 20
    return moisture

def blink_sequence():
    time.sleep(0.5)
    led_toggle(1)
    time.sleep(0.5)
    led_toggle(0)
    time.sleep(0.5)
    led_toggle(1)
    time.sleep(2)
    led_toggle(0)   
 
# Main loop
def main():
    blink_sequence()
    # mqtt_client.connect()
    photo_percentage = get_photoresistor_value()
    dht_sensor()
    moisture = soil_sensor()

    print("Moisture: ", moisture , "%")
    print("Photoresistor value: ", photo_percentage , "%")


if __name__ == "__main__":
    while True:
        try:   
            main()
        except Exception as e:
            print(f"Failed to run main: {e}")

