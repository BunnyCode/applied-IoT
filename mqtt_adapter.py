from simple import MQTTClient
import project_secrets


class MQTT:
    def __init__(self):
        self.client_id = project_secrets.MQTT_CLIENT_ID
        self.server = project_secrets.MQTT_HOST
        self.user = project_secrets.MQTT_USERNAME
        self.password = project_secrets.MQTT_PASSWORD
        self.mqtt_client = MQTTClient(
            client_id=self.client_id,
            server=self.server,
            user=self.user,
            password=self.password,
        )

    def connect(self):
        print("Conecting to %s MQTT broker" % (self.server))
        self.mqtt_client.connect()

    def publish(self, topic, message):
        self.mqtt_client.publish(topic, message)
    
    def subscribe(self, topic):
        self.mqtt_client.subscribe(topic)

    def set_callback(self, callback):
        self.mqtt_client.set_callback(callback)

    def disconnect(self):
        self.mqtt_client.disconnect()

    def check_msg(self):
        self.mqtt_client.check_msg()
