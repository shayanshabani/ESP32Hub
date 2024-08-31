import time


class Device:
    def __init__(self, name, topic, mqtt_client, redis_client):
        self.name = name
        self.topic = topic
        self.mqtt_client = mqtt_client
        self.redis_client = redis_client
        self.elements = None

    def publish_message(self, message):
        self.mqtt_client.publish(self.topic, message)

    def on_message(self, message):
        pass

    def get(self):
        pass

    def get_element(self):
        pass


class BooleanActuator(Device):
    def __init__(self, name, topic, mqtt_client, redis_client):
        super().__init__(name, topic, mqtt_client, redis_client)

    def turn_on(self):
        self.publish_message('on')

    def turn_off(self):
        self.publish_message('off')


class IntegerActuator(Device):
    def __init__(self, name, topic, mqtt_client, redis_client):
        super().__init__(name, topic, mqtt_client, redis_client)

    def send_int(self, number):
        self.publish_message(str(number))


class Sensor(Device):
    def __init__(self, name, topic, mqtt_client, redis_client):
        super().__init__(name, topic, mqtt_client, redis_client)

    def on_message(self, message):
        timestamp = int(time.time())
        self.redis_client.setex(f"{self.name}:{timestamp}", 3600, message)

    def get_data(self):
        current_time = int(time.time())
        one_hour_ago = current_time - 3600

        recent_messages = []

        for key in self.redis_client.scan_iter(f"{self.name}:*"):
            key_timestamp = int(key.decode().split(':')[1])
            if one_hour_ago <= key_timestamp <= current_time:
                message = self.redis_client.get(key).decode("utf-8")
                recent_messages.append((key_timestamp, message))

        recent_messages.sort()

        return recent_messages
