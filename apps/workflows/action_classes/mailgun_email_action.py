import requests
import environ
import json

class MailgunEmailAction:
    """
    - This is a class that sends emails using mailgun
    - The class must be added to the __init__.py file in the action_classes folder in order for the import to work
    - Allowed params in kwargs:
        - to_list: list of emails to send to - required
        - cc_list: list of emails to cc - optional
        - bcc_list: list of emails to bcc - optional
        - template_name: name of the mailgun template - required
        - template_variables: dictionary with mailgun variables - optional
          If the template variables are not found, an empty JSON will be sent and the template might be sent with the placeholders.
    """

    def __init__(self, **kwargs):
        # add all kwargs to the class
        for key, value in kwargs.items():
            setattr(self, key, value)

        # reading .env file
        env = environ.Env()
        environ.Env.read_env()

        # Get Mailgun variables from .env file
        self.url = env('MAILGUN_URL')
        self.api_key = env('MAILGUN_API_KEY')
        self.domain = env('MAILGUN_DOMAIN')
        self.sender = env('MAILGUN_SENDER')

        if self.test_run:
            self.template_name = "turboworkflows - vacaciones aprobadas"
            self.template_variables = {
                'cash_days': '5',
                'employee_name': 'Test',
                'end_date': '2023-01-02',
                'start_date': '2023-01-10'
            }

    def send(self):
        # we create the data parameter to send with mailgun
        if not hasattr(self, 'to_list') or not hasattr(self, 'template_name'):
            response = {
                "text": "to_list and template_name are required.",
                "status_code": 400
            }
        else:
            # check optional variables
            self.cc_list = [] if not hasattr(self, 'cc_list') else self.cc_list
            self.bcc_list = [] if not hasattr(self, 'bcc_list') else self.bcc_list
            self.template_variables = {} if not hasattr(self, 'template_variables') else self.template_variables
            
            # send request to mailgun
            response = requests.post(self.url, auth=("api", self.api_key),
            data={
                "to": self.to_list,
                "cc": self.cc_list,
                "bcc": self.bcc_list,
                "template": self.template_name,
                "h:X-Mailgun-Variables": json.dumps(self.template_variables)
                })

        # Manage success or failure
        if response.status_code == 200:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email, status code: {response.status_code}")
