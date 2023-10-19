# xBlog

Welcome to my xBlog project! A personal blog project is a web-based platform that allows individuals to create and publish their own content, typically in the form of articles, stories, or posts, on topics of their choice. Please follow these instructions to get up and running quickly.

## Installation

1. **Clone the Repository**

   Clone the project repository to your local machine using Git:
   ```bash
   git clone https://github.com/ahmedsserag/xBlog.git
   cd xBlog
   
2. ***Create a Virtual Environment***

     Work within a virtual environment to isolate project dependencies.
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows: env\Scripts\activate
     
3. ***Install Dependencies***

    Use pip to install the project's dependencies from the requirements.txt file:
    ```bash
    pip install -r requirements.txt
    
4. ***Set Up the Database***
   
    Run the following commands to apply database migrations and create a superuser.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    
6. ***Run the Development Server***
   
    Start the Django development server:
    ```bash
    python manage.py runserver
  You can access the admin interface at http://localhost:8000/admin/.
  
  
  ========Thank You !!!=========