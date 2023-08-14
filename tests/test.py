import unittest, time
from src.main import (
    Message,
    Subscriber,
    Topic,
    MessageQueue,
)

class TestMessageQueue(unittest.TestCase):

    def test_basic_publish_subscribe(self):
        topic = Topic("test_topic")
        subscriber1_called = [False]
        subscriber2_called = [False]

        def subscriber1_callback(message):
            subscriber1_called[0] = True

        def subscriber2_callback(message):
            subscriber2_called[0] = True

        subscriber1 = Subscriber(subscriber1_callback)
        subscriber2 = Subscriber(subscriber2_callback)

        message = Message("Hello, World!")
        message_queue = MessageQueue()

        message_queue.subscribe(topic, subscriber1)
        message_queue.subscribe(topic, subscriber2)

        acknowledge_message = message_queue.publish(topic, message)
        self.assertTrue(subscriber1_called[0])
        self.assertTrue(subscriber2_called[0])
        self.assertTrue(acknowledge_message.success)

    def test_non_blocking_publish(self):
        topic = Topic("test_topic")
        subscriber1_called = [False]
        subscriber2_called = [False]

        def subscriber1_callback(message):
            subscriber1_called[0] = True

        def subscriber2_callback(message):
            subscriber2_called[0] = True

        subscriber1 = Subscriber(subscriber1_callback)
        subscriber2 = Subscriber(subscriber2_callback)

        message = Message("Hello, World!")
        message_queue = MessageQueue(wait_for_subscribers_response=False)

        message_queue.subscribe(topic, subscriber1)
        message_queue.subscribe(topic, subscriber2)

        acknowledge_message = message_queue.publish(topic, message)
        time.sleep(1)
        self.assertTrue(subscriber1_called[0])
        self.assertTrue(subscriber2_called[0])
        self.assertTrue(acknowledge_message.success)

if __name__ == '__main__':
    unittest.main()
