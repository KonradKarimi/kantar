# ABOUT

Aptitude Test (Kantar)

# HOW TO USE

To use this project, follow these steps:

1. Clone the repository
2. Make sure python is installed on your machine (tested on python 3.9)
3. `cd` into the repository
4. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

## To start the server:

1. Run the following command in the terminal:
    ```
    python main.py
    ```
2. The server will start on port default port 8000

## Client application:

1. `cd` into the client folder
2. Run the following example command in the terminal:
    ```
    python simple_client.py sort 10 5 18 35 4 78
    ```
3. Run the following example command in the terminal:
    ```
    python simple_client.py reverse 178 35 18 10 5 4  
    ```

## Running tests:

1. `cd` into the repository
2. Run the following command in the terminal:
    ```
    python -m unittest tests/test_server.py
    ```
3. Run the following command in the terminal:
    ```
    python -m unittest tests/test_sort_functions.py
    ```

# KNOWN ISSUES

- lack tests for simple client application
- no docker as for now

