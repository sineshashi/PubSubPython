from typing import Callable, Any, Dict, List, Union, Optional
from collections import defaultdict
from concurrent import futures
import abc
from sortedcontainers import SortedList

class PriorityException(Exception):
    ...

class AcknowledgeMessage:
    def __init__(
        self,
        success: bool,
        error: Optional[Exception] = None
    ) -> None:
        self.success = success
        self.error = error

class Message(abc.ABC):
    def __init__(self, message: Any) -> None:
        self._message = message

    @property
    def message(self) -> Any:
        return self._message

class Subscriber:
    def __init__(self, callable: Callable, priority: int = 0) -> None:
        if priority < 0:
            raise PriorityException("Priority can't be less than 0.")
        self._priority = priority
        self._callable = callable
    
    @property
    def priority(self) -> int:
        return self._priority

    def call(self, message: Message) -> None:
        self._callable(message)

class Topic:
    def __init__(self, topic: str) -> None:
        self._topic = topic

    def __str__(self) -> str:
        return self._topic
    
    def __repr__(self) -> str:
        return str(self)
    
    def __hash__(self) -> int:
        return hash(self._topic)
    
    def __eq__(self, other: "Topic") -> bool:
        return self._topic == other._topic

class MessageQueueSubscribers:
    def __init__(self, number_of_threads: int, wait_for_subscribers_response: bool) -> None:
        self._topic_subscribers: Dict[Topic, SortedList[Subscriber]] = defaultdict(lambda: SortedList(key=lambda x: -x.priority))
        self._thread_pool = futures.ThreadPoolExecutor(number_of_threads)
        self._wait_for_subscribers_response = wait_for_subscribers_response

    def add(self, topic: Topic, subscriber: Subscriber) -> None:
        self._topic_subscribers[topic].add(subscriber)

    def publish(self, topic: Topic, message: Message) -> AcknowledgeMessage:
        futures_list: List[futures.Future] = []
        for subscriber in self._topic_subscribers[topic]:
            futures_list.append(self._thread_pool.submit(subscriber.call, message))
        
        if self._wait_for_subscribers_response:
            for future in futures.as_completed(futures_list):
                try:
                    future.result()
                except Exception as e:
                    return AcknowledgeMessage(
                        success=False,
                        error = e
                    )
            return AcknowledgeMessage(success=True)
        else:
            return AcknowledgeMessage(success=True)

    def __del__(self) -> None:
        self._thread_pool.shutdown()

class MessageQueue:
    _message_queue = None

    class _MessageQueue:
        def __init__(self, number_of_workers: int, wait_for_subscribers_response: bool) -> None:
            '''
            If wait_for_subscibers_response is false, messages will always be acknowledged even if some error occures.
            '''
            self._subscribers = MessageQueueSubscribers(number_of_workers, wait_for_subscribers_response)

        def subscribe(self, topic: Topic, subscriber: Subscriber) -> None:
            self._subscribers.add(topic, subscriber)

        def publish(self, topic: Topic, message: Message) -> AcknowledgeMessage:
            return self._subscribers.publish(topic, message)

    def __new__(cls, number_of_workers: int = 4, wait_for_subscribers_response: bool=True) -> "_MessageQueue":
        if cls._message_queue is None:
            cls._message_queue = cls._MessageQueue(number_of_workers, wait_for_subscribers_response)
        return cls._message_queue
    
    def __getattribute__(self, __name: str):
        return getattr(MessageQueue._message_queue, __name)

    def __setattr__(self, __name: str, __value) -> None:
        return setattr(MessageQueue._message_queue, __name, __value)
