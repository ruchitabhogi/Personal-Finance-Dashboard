# Personal-Finance-Dashboard
A Personal-Finance-Dashboard using Python


This project is a simple Finance Dashboard web application that allows users to input their financial data and visualize their expenditures through various charts. The app is built using   Python's HTTP server  ,   Matplotlib   for visualization, and   HTML/CSS   for the frontend.

## Features

- Users can input their   income   and several categories of   expenses   such as:
  - Electricity Bill
  - Food Expenses
  - Cosmetics
  - Loan Repayment
  - Medicine
  - Savings (Optional)
  
- The app visualizes the expenditure data through multiple charts:
  -   Pie chart  : Breakdown of expenses by category.
  -   Histogram  : Frequency of expenses.
  -   Scatter plot  : Expense amount by category.
  -   Bar plot  : Visual comparison of expenses across categories.

## Tech Stack

-   Python  : Used for building the backend server and handling form submissions.
-   Matplotlib  : Used to create and visualize expense charts.
-   HTML/CSS  : Used for the frontend, creating a simple and responsive form for input.
-   HTTPServer  : A simple HTTP server for handling GET and POST requests.

## How It Works

1. The user fills out a form with their name, income, and various expenses.
2. Upon submission, the data is processed by the Python backend.
3. Charts representing the expenditure breakdown are generated using   Matplotlib   and displayed to the user.
   
Here’s a brief explanation of the code:
1.   Imports  :
   - `http.server`: Used to create a simple HTTP server for handling requests.
   - `os` and `urllib.parse`: Handle URL encoding and file-related operations.
   - `matplotlib`: Used to create visualizations (pie charts, histograms, etc.).
   - `numpy`: Included for numerical operations but not directly used in this version.

2.   HTML Form  :
   - The form is presented in HTML with CSS for styling. It asks for the user's name, income, and various expenses (electricity, food, cosmetics, etc.).

3.   Server Logic  :
   - A class `RequestHandler` is created to handle both `GET` and `POST` requests.
   -   GET  : Serves the HTML form when the user accesses the root URL (`/`).
   -   POST  : Receives the form data, processes it, and generates visual charts based on the user's input.

4.   Data Processing  :
   - The form data (name, income, and expenses) is parsed, and the expenses are stored in a dictionary.

5.   Visualization  :
   - A `generate_dashboard` function creates four types of charts (pie chart, histogram, scatter plot, and bar plot) based on the expenses.
   - The charts are saved as a PNG file and displayed to the user.

6.   Running the Server  :
   - The `run()` function starts the server on port 8000, listening for incoming requests.

This is a simplified finance dashboard where users input financial data, and the app generates visual reports.

## Prerequisites

Ensure you have Python installed and the required packages:

```bash
pip install matplotlib
```

## Running the Project

To run the project on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/ruchitabhogi/Personal-Finance-Dashboard.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Personal-Finance-Dashboard
   ```

3. Run the server:

   ```bash
   !python bar.py
   ```

4. Open your browser and go to `http://localhost:8000` to access the dashboard.

## Input
![11](https://github.com/user-attachments/assets/e99b2a0d-03bc-4e01-9ef5-2c5d59752b29)


## Output
![22](https://github.com/user-attachments/assets/317424cb-f0e6-4080-8f96-f34bd0346bc4)









