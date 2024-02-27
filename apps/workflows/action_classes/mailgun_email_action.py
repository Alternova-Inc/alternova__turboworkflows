import requests
import environ

class MailgunEmailAction:
    """
    - This is a class that sends emails using mailgun
    - The class must be added to the __init__.py file in the action_classes folder in order for the import to work
    - Allowed params in kwargs:
        - cc_list: list of emails to cc
        - bcc_list: list of emails to bcc
        - subject_text: string with the email subject
        - body_text: string with the email body
    """

    def __init__(self, **kwargs):
        # add all kwargs to the class
        for key, value in kwargs.items():
            setattr(self, key, value)

        # reading .env file
        env = environ.Env()
        environ.Env.read_env()

        # Get Mailgun API key and domain from .env file
        self.url = env('MAILGUN_URL')
        self.api_key = env('MAILGUN_API_KEY')
        self.domain = env('MAILGUN_DOMAIN')
        self.sender = env('MAILGUN_SENDER')

    def send(self):
        if not hasattr(self, 'cc_list'):
            self.cc_list = []
        if not hasattr(self, 'bcc_list'):
            self.bcc_list = []

        if not hasattr(self, 'subject_text') or not hasattr(self, 'body_text'):
            response = {
                "error": "subject_text and body_text are required.",
                "status_code": 400
            }
        else:
            response = requests.post(self.url, auth=("api", self.api_key),
            data={"from": self.sender,
                "to": self.cc_list,
                "bcc": self.bcc_list,
                "subject": self.subject_text,
                "text": self.body_text,
                })

        # Now you can do something with the response
        if response.status_code == 200:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email, status code: {response.status_code}")
