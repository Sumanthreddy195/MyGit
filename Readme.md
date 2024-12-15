# Django IoT Project

This project is a Django-based application designed to receive and process payloads from IoT devices.

## Features
- Two models: `Device` and `Payload`.
- API endpoint to process incoming payloads.
- Duplicate payload detection using `fCnt`.
- Base64 decoding and Hexadecimal conversion.
- Status tracking for each device.


## Setup Instructions

### Prerequisites
1. Python 3.8 or higher installed.

### Steps to Set Up Locally
1. Clone the repository:
   git clone <your-repository-url>
   cd django_iot_project
2. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # For Linux/Mac
   .venv\Scripts\activate     # For Windows  
3. Install dependencies:
    pip install -r requirements.txt
4. Apply database migrations:
    python manage.py makemigrations
    python manage.py migrate
5. Start the development server:
    python manage.py runserver
6. Access the application:
    Root: http://127.0.0.1:8000/
    API: http://127.0.0.1:8000/api/
   
