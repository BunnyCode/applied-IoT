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
SDA_PIN = Pin(14)
SCL_PIN = Pin(15)

# Variables
i2c = machine.I2C(1, sda=SDA_PIN, scl=SCL_PIN, freq=400000)
seesaw = StemmaSoilSensor(i2c)
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
    # set a percentage value for the photoresistor
    photoresistor_value = photoresistor.read_u16() / 65535 * 100
    photoresistor_percentage = "%.2f" % photoresistor_value
    return photoresistor_percentage
    

def send_data_to_endpoint(temperature, humidity, moisture, photoresistor_percentage):
    time.sleep(1)
    sensor_data_temp_and_humidity = json.dumps({"feeds":{"temp": temperature, "humidity": humidity, "soil": moisture, "light": photoresistor_percentage}})
    try:
        mqtt_client.publish(
            project_secrets.MQTT_PUBLISH_GROUP, str(sensor_data_temp_and_humidity)
        )
        print("pushed data")
    except Exception as e:
        print(f"Failed to publish message: {e}")


# Read DHT11 sensor
def dht_sensor():
    import dht
    d = dht.DHT11(Pin(11))
    d.measure()
    return d


def soil_sensor():
    moisture = seesaw.get_moisture() / 20
    return moisture

def blink_sequence(): # Blink sequence an delay of cycles
    time.sleep(0.5)
    led_toggle(1)
    time.sleep(0.5)
    led_toggle(0)
    time.sleep(0.5)
    led_toggle(1)
    time.sleep(2.5)
    led_toggle(0)   
 
# Main loop
def main():
    blink_sequence()
    # mqtt_client.connect()
    light_precentage = get_photoresistor_value()
    dht_values = dht_sensor()
    moisture = soil_sensor()

    print("Temperature: ", dht_values.temperature())
    print("Humidity: ", dht_values.humidity())
    print("Moisture: ", moisture , "%")
    print("Photoresistor value: ", light_precentage , "%")
    send_data_to_endpoint(dht_values.temperature(), dht_values.humidity(), moisture, light_precentage)


if __name__ == "__main__":
    mqtt_client.connect()
    print("Connected to MQTT broker")
    while True:
        try:   
            main()
        except Exception as e:
            print(f"Failed to run main: {e}")

