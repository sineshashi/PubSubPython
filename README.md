# Educational Messaging System

A simple messaging system project created for educational purposes to practice concepts related to concurrency and low-level design in Python.

## Project Overview

The Educational Messaging System is a small project aimed at providing hands-on experience with concepts such as concurrency, thread pools, and low-level design patterns. The project simulates a basic message queue system where messages can be published to different topics, and subscribers can receive and process these messages asynchronously.

## Features

- Publish and subscribe to topics using a simulated message queue.
- Utilize a thread pool to handle asynchronous message processing.
- Practice fundamental concepts of concurrency, thread safety, and low-level design.
- Explore different strategies for handling message processing and synchronization.

## Motivation

The primary motivation behind this project is to provide a practical learning experience in the following areas:

- Understanding the basics of concurrent programming.
- Implementing thread-safe data structures.
- Exploring different methods of synchronization.
- Practicing low-level design principles for efficient and scalable systems.

## Getting Started

To get started with the Educational Messaging System project, follow these steps:

1. **Clone the repository:** Open your terminal and execute the following command to clone the project repository to your local machine:

   ```bash
   git clone https://github.com/sineshashi/pubsubpython.git
   ```
2. **Navigate to the project directory:** Change your working directory to the project folder:

   ```bash
   cd pubsubpython
   ```
3. Install the dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Limitations

* **Simplified Messaging Logic:** The messaging system in this project is intentionally simplified for educational purposes. In a real-world scenario, additional considerations like message persistence, fault tolerance, and scalability would need to be addressed.
* **Limited Error Handling:** Error handling is minimal in this project to focus on concurrency concepts. In a production system, robust error handling and recovery mechanisms would be crucial.

## Suggestions for Further Improvements

* **Enhanced Error Handling:** Implement more comprehensive error handling mechanisms to handle scenarios like network failures, subscriber crashes, and message processing errors.
* **Advanced Synchronization Techniques:** Explore advanced synchronization mechanisms such as semaphores, condition variables, and read-write locks to gain a deeper understanding of concurrent programming.
* **Message Persistence:** Integrate message persistence to ensure messages are not lost even in case of system crashes.
* **Distributed Messaging System:** Extend the project to simulate a distributed messaging system where messages can be published and received across multiple nodes.

## Contributing

This project is primarily for educational purposes. However, contributions, suggestions, and discussions are welcome! Feel free to open issues and contribute to enhance this project's learning experience.
