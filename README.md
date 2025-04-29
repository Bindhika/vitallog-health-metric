# VitalLog: Health Metrics Tracker

VitalLog is a Flask-based web application designed to help users track and manage their health metrics, such as weight and blood pressure, over time. The application provides a user-friendly interface for adding, viewing, updating, and deleting health metrics, along with graphical summaries to visualize trends.

## Features
- **Add Metrics**: Record health metrics with type, value, unit, and timestamp.
- **View Metrics**: Display all metrics with an option to see the latest recorded metric.
- **Update and Delete Metrics**: Edit or remove metrics as needed.
- **Graphical Summaries**: Generate interactive graphs to visualize trends over time using Matplotlib.
- **Responsive Design**: A mobile-friendly interface powered by Bootstrap.
- **Secure and Scalable**: Built with Flask and SQLAlchemy for reliability and scalability.

## Technologies Used
- Python (Flask Framework)
- SQLAlchemy (Database ORM)
- Matplotlib (Data Visualization)
- Bootstrap (Frontend Styling)
- SQLite (Database)

## Installation

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.8 or higher
- Virtual Environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vital-log.git

   - Navigate to the project directory:cd vital-log

- Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

- Install dependencies:pip install -r requirements.txt

- Run the application:python app.py
- Usage
- Open your web browser and navigate to http://127.0.0.1:5000/.
- Use the interface to add, view, update, or delete health metrics.
- Generate graphs by visiting /metrics_chart to see trends.

Project Structure
project/
├── app.py                # Main application file
├── models.py             # Database models
├── templates/            # HTML templates
│   ├── index.html        # Home page
│   ├── create.html       # Add metric page
│   ├── metrics.html      # View metrics page
│   ├── update.html       # Update metric page
│   ├── metrics_chart.html # Graph display page
├── static/               # Static assets (CSS, JS, images)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

---

### Instructions:
1. Copy this `README.md` into the root directory of your project.
2. Update the repository URL (`https://github.com/your-username/vital-log.git`) with your actual GitHub repository URL.
3. Modify any section (e.g., Technologies Used, Features) to match your project specifics.







   
