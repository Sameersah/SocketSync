# WebSocket Client-Server Example

This repository contains a simple WebSocket client-server example using Python and JavaScript. The server is implemented using Python's `asyncio` and `websockets` libraries, while the client is implemented using HTML and JavaScript.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Server](#server)
- [Client](#client)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- `websockets` library for Python
- A web browser

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/websocket-example.git
    cd websocket-example
    ```

2. Install the required Python libraries:
    ```sh
    pip install websockets
    ```

## Usage

### Running the Server

1. Navigate to the server directory:
    ```sh
    cd server
    ```

2. Run the server:
    ```sh
    python3 server.py
    ```

### Running the Client

1. Open the `client.html` file in a web browser:
    ```sh
    open client.html
    ```

2. Enter a message in the input field and click the "Send Message" button to send a message to the server 10,000 times.

## Server

The server is implemented in Python using the `asyncio` and `websockets` libraries. It listens for incoming WebSocket connections and echoes back any messages it receives, appending "i got it" to each message.




Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.


