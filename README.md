# Job Board Web Application

This is a web application built with Flask that allows users to post and browse job listings.

# Prerequisites
- Python 3.6 or higher
- Flask 1.1.2 or higher
- Flask-SQLAlchemy
I was also using the venv virtual environment to run the project. This can be ran using the commands: 

```
python3 -m venv venv
source venv/bin/activate
```

# Installation
Clone the repository to your local machine
Install the required dependencies

# Usage
To run the application, navigate to the correct directory and type python app.py in the terminal.
    Alternatively, run the file in an IDE like VSCode as I do in the tutorial. 
In your browser, navigate to localhost:5000 to access the job board homepage
From the homepage, you can browse job listings, add new job listings, and delete job listings

# Architecture Design
I followed a client-server architecture design for this project. The client is responsible for displaying the user interface, while the server processes user input and interacts with the database. I used Flask as the web framework and SQLite as the database while using Flask-SQLAlchemy. 

The application has several routes, each of which maps to a specific function that either displays a page or performs a database operation. The database schema consists of a single table, Job, which has columns for id, title, description, hourly_wage, and contact_email.

I chose this architecture because it is a simple and straightforward way to build a web application. Flask provides an easy-to-use interface for handling HTTP requests and rendering HTML templates. SQLite is a lightweight database management system that is well-suited for small-scale applications like this one.

# Changes from Project Proposal
In my original project proposal, I considered using either the publish-subscribe architecture or the client-server architecture. Ultimately, I decided the client-server would be a better fit for this project. I made this decision because a client-server architecture is more straightforward to implement and maintain for a small-scale web application like this one. The publish-subscribe architecture would be better suited for larger-scale applications that require real-time data updates and have more complex data relationships.
