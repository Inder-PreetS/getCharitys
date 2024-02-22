# FastAPI Project

This is a sample FastAPI project demonstrating basic setup and usage.

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/getCharitys.git
    ```

2. Navigate to the project directory:

    ```bash
    cd getCharitys
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

    This command starts the server with automatic reloading enabled, meaning any changes you make to the code will trigger a server restart.

2. Open your web browser and go to `http://localhost:8000/docs` to access the API documentation (Swagger UI) and interact with the endpoints.

3. Additionally, you can test the charity search endpoint by accessing the following URL:


    ```
    http://localhost:8000/charity/search?query={query}&offset={offset}&limit={limit}
    ```

    Replace `{query}`, `{offset}`, and `{limit}` with your desired values. This URL will search for charities based on the specified query, offset, and limit.

4. To stop the server, press `Ctrl + C` in the terminal where the server is running.

