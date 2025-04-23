# Assignment 6

## How to Run
1. Clone this repo
2. Create a virtual environment
3. Install dependencies with `pip install -r requirements.txt`
4. Set up your `.env` file
5. load the sample articles into your MySQL database, run the command:

python manage.py load_articles



7. Run migrations and start the server:


python manage.py makemigrations 

python manage.py migrate 

python manage.py runserver


## .env Sample
Create a `.env` file with:

DB_NAME=your_db 

DB_USER=your_username 

DB_PASSWORD=your_password 

DB_HOST=localhost 

DB_PORT=3306
