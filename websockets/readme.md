### What are WebSockets?

WebSockets are a communication protocol that provides full-duplex communication channels over a single TCP connection. Unlike HTTP, which is request-response-based, WebSockets allow for real-time, two-way communication between a client (e.g., a browser) and a server. This makes WebSockets ideal for applications like chat apps, live notifications, real-time gaming, and collaborative tools.

### Key Features of WebSockets:
- **Full-Duplex Communication**: Both client and server can send and receive messages simultaneously.
- **Persistent Connection**: Once established, the connection remains open, reducing the overhead of repeatedly opening and closing connections.
- **Low Latency**: Ideal for real-time applications due to minimal delay in communication.


Examples: 
- Miro boards

## How to run the code

How It Works:
Server:
The server listens on ws://localhost:8765.
When a client connects, it starts an echo handler that listens for messages from the client and sends back an "Echo" response.


Client:
The client connects to the server and sends a message ("Hello, Server!").

It waits for the server's response and prints it.
Running the Example:

Install the websockets library:
Start the server:
Run the client in a separate terminal:
You should see the client send a message and receive an echoed response from the server.