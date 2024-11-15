# Showcase
# Compute Change Application

A Python application that calculates the optimal combination of dollar bills and coins for a given monetary amount. 

---


## Prerequisites

Ensure you have the following installed:

- **Python 3.8 or higher**
- **PyCharm (optional)**: Recommended for a better development experience.

You will also need the following Python libraries:

- None (this project relies only on standard Python libraries).

---

## Setup

1. **Clone the Repository**  
   Clone the project repository to your local machine using:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
2. **Create a Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
3. **Open in Pycharm (If Virtual Environment Created)**
- Open Pycharm
- Select File > Open and navigate to the project folder
- Pycharm should automatically detect the venv if created. If not, configure the Python interpretor manually through File > Settings > Python Interpreter
4. **Run the Application**
  - Execute the application from the terminal or PyCharm's run configuration:
    ```bash
    python main.py

## Usage
When you run the script, it will prompt you for a monetary amount. Enter the amount in the format Dollars.Cents. Example:
  Please enter the amount: 123.45

## Testing
This project includes unit tests to ensure correct functionality. You can run the tests as follows: 
1. Open the terminal or PyCharm terminal
2. Run the tests using:
   ```bash
   python -m unittest showcaseTest.py
3. Check the output to confirm all tests pass
