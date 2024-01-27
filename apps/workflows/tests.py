from django.test import TestCase
from apps.authentication.models.profile import Profile

# Create your tests here.
from apps.authentication.models.role import Role
from apps.workflows.models import Workflow, WorkflowStepForm, UserFormField, UserFormContent
from django.core.exceptions import ValidationError
from apps.authentication.models import Company
from django.contrib.auth import get_user_model
from apps.authentication.models.company_profile_set import CompanyProfileSet

class AddWorkflowToRoleSignalTest(TestCase):
    def setUp(self):
        # Create a company
        self.company = Company.objects.create(company_name='Test Company')

    def test_workflow_added_to_admin_role(self):
        # get the admin role for the company
        admin_role = Role.objects.get(company=self.company, role_name='admin')

        # Create a new workflow for the company
        workflow = Workflow.objects.create(company=self.company, workflow_name='Test Workflow')

        # Check that the workflow was added to the admin role's workflows
        self.assertIn(workflow, admin_role.workflows.all(), "Workflow was not added to admin role")


User = get_user_model()
class UserFormContentTest(TestCase):
    def setUp(self):
        self.company1 = Company.objects.create(company_name='Company 1')
        self.company2 = Company.objects.create(company_name='Company 2')

        self.user1 = User.objects.create_user(username='user1', password='password', is_superuser=False)
        self.user2 = User.objects.create_user(username='user2', password='password', is_superuser=False)

        self.profile1 = Profile.objects.create(user=self.user1)
        self.profile2 = Profile.objects.create(user=self.user2)

        self.CompanyProfileSet1 = CompanyProfileSet.objects.create(profile=self.profile1, company=self.company1)
        self.CompanyProfileSet2 = CompanyProfileSet.objects.create(profile=self.profile2, company=self.company2)

        self.workflow1 = Workflow.objects.create(company=self.company1, workflow_name='Test Workflow 1')
        self.workflow2 = Workflow.objects.create(company=self.company2, workflow_name='Test Workflow 2')

        self.user_form1 = WorkflowStepForm.objects.create(company=self.company1, workflow_step_name='UserForm 1', workflow=self.workflow1)
        self.user_form2 = WorkflowStepForm.objects.create(company=self.company2, workflow_step_name='UserForm 2', workflow=self.workflow2)

        self.field1 = UserFormField.objects.create(company=self.company1, public_name='Field 1', code='1', type='LongText')
        self.field2 = UserFormField.objects.create(company=self.company2, public_name='Field 2', code='2', type='ShortText')

    def test_validate_company(self):
        user_form_content = UserFormContent(user_form=self.user_form1)
        user_form_content.field = self.field1
        user_form_content.order = 1
        user_form_content.save(current_user=self.user1)  # Pass the current user as an argument to the save() method
        saved_user_form_content = UserFormContent.objects.get(id=user_form_content.id)

        # Check that the saved UserFormContent has the expected attributes
        self.assertEqual(saved_user_form_content.user_form, self.user_form1)

        user_form_content = UserFormContent(user_form=self.user_form1)
        user_form_content.field = self.field2
        user_form_content.order = 1
        
        with self.assertRaises(ValidationError): 
            user_form_content.save(current_user=self.user1)  # Should raise ValidationError because field2 is from a different company than user_form1

        user_form_content = UserFormContent(user_form=self.user_form2)
        user_form_content.field = self.field1
        user_form_content.order = 1
        
        with self.assertRaises(ValidationError): 
            user_form_content.save(current_user=self.user1)  # Should raise ValidationError because user_form2 is from a different company than current_user
        