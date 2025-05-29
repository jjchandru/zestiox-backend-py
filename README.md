# Zestiox Backend Python Skeleton – Setup & Usage Guide

Welcome to the Zestiox Food Delivery App backend skeleton project! This guide will help you set up your development environment, install dependencies, run the Flask app, and access a sample API endpoint. No prior Python experience is required—just follow the steps below.

---

## Prerequisites

Before you begin, make sure you have the following installed on your computer:

1. **Git**
   - Download from: https://git-scm.com/downloads
   - Follow the installation instructions for your operating system.

2. **Python 3.11 or later**
   - Download from: https://www.python.org/downloads/
   - During installation, check the box that says **"Add Python to PATH"**.

3. **Visual Studio Code (VS Code)**
   - Download from: https://code.visualstudio.com/

4. **Microsoft Python Extension for VS Code**
   - Open VS Code
   - Go to the Extensions view (Ctrl+Shift+X)
   - Search for **"Python"** by Microsoft and click **Install**

---

## Setting Up the Project

1. **Clone the Project Repository**
   - Open a terminal (Command Prompt or PowerShell on Windows) in a convenient folder where you want to have this project. This can typically be the folder where the angular project is present.
   - Run the following command to clone the repository:
     ```powershell
     git clone https://github.com/jjchandru/zestiox-backend-py.git
     ```
   - Change directory to the project folder:
     ```powershell
     cd zestiox-backend-py
     ```

2. **Open the Project in VS Code**
   - Launch VS Code.
   - Click on **File > Open Folder...** and select the `zestiox-backend-py` folder.

3. **Open a Terminal in VS Code**
   - Go to **Terminal > New Terminal**. This will open a terminal at the project root.

4. **Create a Virtual Environment**
   - In the terminal, run:
     ```powershell
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On **Windows**:
       ```powershell
       .\venv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```
   - You should see `(venv)` at the start of your terminal prompt.

5. **Install Project Dependencies**
   - In the terminal, run:
     ```powershell
     pip install -r requirements.txt
     ```
   - This will install all required Python packages for the project.

6. **Switch to Your Feature Branch**
   - The following branches are available: `login`, `register`, `menu`, `cart`, `orders`, `profile`.
   - To switch to your assigned branch, run:
     ```powershell
     git checkout <branch-name>
     ```
   - Replace `<branch-name>` with your assigned branch (e.g., `login`).

---

## Running the Flask App

1. **Make Sure You Are in the Project Root Directory**
   - Your terminal should be in the `zestiox-backend-py` folder (not inside the `app` folder).

2. **Start the Flask App**
   - Run the following command:
     ```powershell
     python -m app.main
     ```
   - You should see output indicating that the Flask development server is running, e.g.:
     ```
     * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
     ```

---

## Accessing the Sample API Endpoint

- Open your web browser and go to:
  - [http://localhost:5000/employees](http://localhost:5000/employees)
- You should see a JSON response with example employee data, like:
  ```json
  {
    "employees": [
      {"id": 1, "name": "Alice", "role": "Manager"},
      {"id": 2, "name": "Bob", "role": "Chef"},
      {"id": 3, "name": "Charlie", "role": "Waiter"}
    ]
  }
  ```

---

## REST APIs to Develop

You are expected to implement the following REST API endpoints. Each endpoint should return JSON data as described below. You may use hardcoded data initially, and later connect to the database.

### 1. Login
- **Endpoint:** `POST /authenticate`
- **Request:**
  ```json
  { "mobile": "1234567890", "password": "yourpassword" }
  ```
- **Response (Success):**
  ```json
  { "message": "Login successful", "user": { "id": 1, "name": "Alice", "mobile": "1234567890" } }
  ```
- **Response (Failure):**
  ```json
  { "error": "Invalid mobile number or password" }
  ```

### 2. Register
- **Endpoint:** `POST /users`
- **Request:**
  ```json
  { "name": "Alice", "mobile": "1234567890", "password": "yourpassword", "confirm_password": "yourpassword" }
  ```
- **Response (Success):**
  ```json
  { "message": "Registration successful. Please login." }
  ```
- **Response (Failure):**
  ```json
  { "error": "Mobile number already registered" }
  ```

### 3. Menu
- **Endpoint:** `GET /menu-items`
- **Response:**
  ```json
  {
    "categories": [
      {
        "name": "Starters",
        "items": [ { "id": 1, "name": "Paneer Tikka", "price": 120 }, ... ]
      },
      ...
    ]
  }
  ```

### 4. Cart
- **Endpoint:** `GET /carts?userId=<id>`
- **Response:**
  ```json
  {
      { "id": 1, "name": "Paneer Tikka", "quantity": 2, "price": 120, "line_total": 240 },
      ...
  }
  ```
- **Endpoint:** `POST /carts`
- **Request:**
  ```json
  { "user_id": 3, "item_id": 1, "quantity": 2 }
  ```
- **Response:**
  ```json
  { "message": "Item added to cart" }
  ```

### 5. Orders
- **Endpoint:** `GET /orders?userId=<id>`
- **Response:**
  ```json
  [
    {
        "id": 1,
        "date": "2025-05-29",
        "items": [ { "name": "Paneer Tikka", "quantity": 2 } ],
        "total": 240,
        "status": "Preparing"
    },
    ...
  ]
  ```
- **Endpoint:** `POST /orders/cancel`
- **Request:**
  ```json
  { "order_id": 1 }
  ```
- **Response:**
  ```json
  { "message": "Order cancelled" }
  ```
---

## Next Steps

- Review the REST API requirements above for the features to implement.
- Use the provided folder structure and files as a starting point for your development.
- If you have any issues, check the terminal output for error messages and ensure all steps above were followed.

---

Happy coding!
