from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import urllib.parse
import matplotlib.pyplot as plt
import numpy as np

# HTML form and CSS styles (updated to include more inputs)
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Finance Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        form {
            text-align: left;
        }

        label {
            font-weight: bold;
        }

        input[type="text"],
        input[type="number"] {
            width: 100%;
            padding: 8px;
            margin: 5px 0 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Finance Dashboard</h2>
        <form action="/" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <br><br>
            <label for="income">Income:</label>
            <input type="number" id="income" name="income" required>
            <br><br>
            <label for="savings">Savings:</label>
            <input type="number" id="savings" name="savings">
            <br><br>
            <label for="electricity">Electricity Bill:</label>
            <input type="number" id="electricity" name="electricity">
            <br><br>
            <label for="food">Food Expenses:</label>
            <input type="number" id="food" name="food">
            <br><br>
            <label for="cosmetics">Cosmetics:</label>
            <input type="number" id="cosmetics" name="cosmetics">
            <br><br>
            <label for="loan">Loan Repayment:</label>
            <input type="number" id="loan" name="loan">
            <br><br>
            <label for="medicine">Medicine:</label>
            <input type="number" id="medicine" name="medicine">
            <br><br>
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
'''

# Function to generate dashboard
def generate_dashboard(name, income, expenses):
    # Data for visualization
    categories = list(expenses.keys())
    values = list(expenses.values())

    # Pie chart
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 2, 1)
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expenditure Breakdown')

    # Histogram
    plt.subplot(2, 2, 2)
    plt.hist(values, bins=len(categories), edgecolor='black')
    plt.xlabel('Categories')
    plt.ylabel('Frequency')
    plt.title('Expense Frequency')

    # Scatter plot
    plt.subplot(2, 2, 3)
    plt.scatter(categories, values, color='red')
    plt.xlabel('Categories')
    plt.ylabel('Expense Amount')
    plt.title('Expense Scatter Plot')

    # Bar plot
    plt.subplot(2, 2, 4)
    plt.bar(categories, values, color='green')
    plt.xlabel('Categories')
    plt.ylabel('Expense Amount')
    plt.title('Expense Bar Plot')

    plt.tight_layout()
    plt.savefig('expenses_charts.png')  # Save the chart as a PNG file
    plt.show()

# HTTP Request Handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        if self.path == '/':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = urllib.parse.parse_qs(post_data)
            
            if 'name' in parsed_data and 'income' in parsed_data:
                name = parsed_data['name'][0]
                income = float(parsed_data['income'][0])
                
                # Gather expense data
                expenses = {}
                for key in parsed_data:
                    if key != 'name' and key != 'income':
                        expenses[key] = float(parsed_data[key][0])

                # Generate dashboard
                generate_dashboard(name, income, expenses)
                
                # Respond with a simple message
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('<html><body><h1>Data submitted successfully!</h1></body></html>'.encode('utf-8'))
            else:
                self.send_error(400, 'Bad Request: Missing parameters')
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

# Main function to run the server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
