# TurboWorkflows

TurboWorflows is an open-source tool to create and manage approval workflows that can be easily integrated with third party services.

## Stack

This software is built using Django 4.2 and Vanilla Javascript and CSS.

## Installation

Follow these steps to install TurboWorkflows:

1. **Clone the repository**
   Clone the TurboWorkflows repository to your local machine:

   `bash git clone https://github.com/yourusername/turboworkflows.git`
   <br>

2. **Set up a Conda environment (Optional)**
    It's recommended to use a Conda environment to isolate your project and avoid conflicts with other packages. If you're using Miniconda, you can set up a Conda environment like this:
```
    conda create --name turboworkflows python=3.9
    conda activate turboworkflows
```
<br>

3. **Install the dependencies**

    Navigate to the project directory and install the required packages using pip:
    `pip install -r requirements.txt`

4. **Set up the .env file**

    Create a .env file in the project root directory to store your environment variables. Here's a template for your file:

```
    SECRET_KEY=your-django-secret-key
    DEBUG=True
    DB_NAME=your-database-name
    DB_USER=your-database-user
    DB_PASSWORD=your-database-password
    DB_HOST=your-database-host
    DB_PORT=your-database-portenv
```
<br>

5. **Set up the database**
    We're using PostgreSQL for our database. Make sure you have it installed and running. Apply the migrations to set up the database:

    `python manage.py migrate`
    <br>

6. **Start the server**
    Run: `python manage.py runserver`

You should now be able to access TurboWorkflows at http://localhost:8000.

7. **Next steps**
   * Create the superuser
   * Access the Django Admin at http://localhost:8000/admin.
   * Start using it!

Developed by [Alternova, Inc](https://alternova.com).