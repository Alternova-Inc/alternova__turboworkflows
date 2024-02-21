# Create your tests here.
from apps.defaults.tests import BaseTestCase
from apps.workflows.models import UserFormContent
from django.core.exceptions import ValidationError


class UserFormContentTest(BaseTestCase):
    ''''
    Test module for UserFormContent model
    '''

    def test_validate_company(self):
        '''
        Checks that the user_form and the form_field are from the same company
        '''
        user_form_content = UserFormContent(user_form=self.user_form1, field=self.field2, order=1)
        
        with self.assertRaises(ValidationError): 
            user_form_content.save()  # Should raise ValidationError because field2 is from a different company than user_form1