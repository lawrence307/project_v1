#**Datavisual-expense App**

##**Introduction**

**Datavisual-expense App** is a Python-based web application designed to help users categorize and visualize their expenses as well as their source of income and how their money flows. The app automatically categorizes expenses and income sources based on predefined rules and generates interactive charts to display expense and income  trends over time.
The deployed application can be navigated through [Datavisual-expenseAPP](https://project-v1.onrender.com/)
Project's [Blog Post](https://medium.com/@lawrence_muthini/my-first-project-53486198e81e)
**AUTHORS:**
Lawrence Nzomo - the project develover find me on [Linked-in](https://www.linkedin.com/in/lawrence-nzomo-1769302b6/)
##**Project Name:**

##**Datavisual-expense App**

##**Table of Contents**

  1. Introduction
  2. Features
  3. Installation
  4. Usage
  5. Contributing
  6. Related Projects
  7. License

##**Features**

**Expense Categorization:** Automatically categorizes expenses based on predefined rules.
**Data Visualization:** Generates interactive charts to display expense trends over time.


##**Installation**

To install and run the Datavisual-expense App, follow these steps:

Clone the repository:
_(Use this code_)
`git clone https://github.com/lawrence307/project_v1.git
cd project_v1`

**Create a virtual environment:
**
bash script
`python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate``

**Install dependencies:**

bash script
`pip install -r requirements.txt`

**Set up the database:**

bash script
`flask db init
flask db migrate -m "Initial migration."
flask db upgrade`

**Run the application:**

bash
`python run`

**##Usage**

Once the application is running, navigate to http://127.0.0.1:5000 in your web browser to start using the Datavisual-expense App.

**##Contributing**

Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.

**##Related Projects**

Here are some related projects you might find interesting:
1. Flask - The micro web framework used for this project.
2. SQLAlchemy - The SQL toolkit used for database interactions.

**##License**

This project is licensed under the MIT License. See the LICENSE file for more details.


