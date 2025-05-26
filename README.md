PageFlow
PageFlow is a basic school project developed using the Django web framework. It is a web application that allows users to create and manage content through a clean and structured interface. The project must be run inside the myproject directory.

Features:
  User registration and login system,
  Content creation and editing,
  Content listing and detailed view,
  Admin panel for managing users and content

Installation:
Follow the steps below to set up the project locally:

1. Clone the Repository
2. Create a Virtual Environment: 
  python -m venv venv ,
  source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies:
  pip install -r requirements.txt
4. Set Up the Database:
  python manage.py makemigrations ,
  python manage.py migrate
5. Create a Superuser:
  python manage.py createsuperuser
6. Run the Development Server:
  python manage.py runserver
