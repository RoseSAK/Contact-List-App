Contact List App - Rose Azad Khan
==================================

This Django app displays a database of contacts for anyone to view and search.
There is an admin page from which new contacts and their details can be added to the database.
Admin login details:
  Email: roseazadkhan@gmail.com
  Password: Solirius

Run in virtual environment such as Anaconda and using Python 3

How to run:
- Activate virtual environment
>>> python manage.py runserver

How to update the database with model changes:
- Make changes in models.py file
>>> python manage.py makemigrations
>>> python manage.py migrate

Further Improvements:
- Create tests for test-driven development
- Alter the search function to search contact details and manager - it currently
  works for the name, address and department fields only
- CSS templates for all views
- Fix/change link to main site on admin page
