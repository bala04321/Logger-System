# Nallapati Bala Yashaswini
So, the overall assignment was about creating a Flask application with a logger that utilizes a circular linked list data structure and which is operational for 8 working hours.

So the approach for this assignment is 
First we will setup up the flask framework, then we integrate the logger using the circular linked list, and finally add an api endpoint to interact with the logger

1. setup FLASK :- to ensure that you have the flask environment, you can install it using the pip command.
"pip install Flask"

2. Flask Application Structure
Here’s a simple way to structure your Flask application:
app.py: The main Flask application.
logger.py: The Logger class using a circular linked list.
log_node.py: A node class for each log entry.

3.Running the Flask application
To run the Flask application:

Make sure all the files are saved.
Navigate to the directory containing app.py.
Run the command: python app.py.
Use a tool like Postman or CURL to test the endpoints.

4. python app.py
after running this command we will get this output.

5. To check if the API endpoint is working:

"curl http://localhost:5000/logs"
Here's how you can interact with the Flask application:
To add a log entry, send a POST request to http://localhost:5000/log with the appropriate JSON payload containing the log details.
To retrieve logged data, send a GET request to http://localhost:5000/logs.


6.To test if the logging restrictions are in place:
Run the Flask application.
Try to send a log entry outside the specified hours using a tool like Postman or curl.
The server should respond with an error message if you try to log outside of 9:00 AM to 5:00 PM, and successfully log entries during those hours.
