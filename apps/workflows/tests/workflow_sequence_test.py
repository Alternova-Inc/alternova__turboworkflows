from django.test import TestCase
from apps.authentication.models.profile import Profile

# Create your tests here.
from apps.workflows.models import Workflow, WorkflowStepForm, UserFormField, UserFormContent
from django.core.exceptions import ValidationError
from apps.authentication.models import Company
from django.contrib.auth import get_user_model
from apps.authentication.models.company_profile_set import CompanyProfileSet
from apps.workflows.models.workflow_sequence import WorkflowSequence
from apps.workflows.models.workflow_step_approval import WorkflowStepApproval

User = get_user_model()
class WorkflowSequenceTest(TestCase):
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

        self.user_form1 = WorkflowStepForm.objects.create(company=self.company1, workflow_step_name='UserForm 1')
        self.user_form2 = WorkflowStepForm.objects.create(company=self.company2, workflow_step_name='UserForm 2')
        self.user_form3 = WorkflowStepApproval.objects.create(company=self.company1, workflow_step_name='UserForm 3')

        self.field1 = UserFormField.objects.create(company=self.company1, public_name='Field 1', code='1', type='LongText')
        self.field2 = UserFormField.objects.create(company=self.company2, public_name='Field 2', code='2', type='ShortText')

        self.user_form_content1 = UserFormContent(user_form=self.user_form1, field=self.field1, order=1)
        self.user_form_content1.save(current_user=self.user1)
        self.user_form_content2 = UserFormContent(user_form=self.user_form2, field=self.field2, order=1)
        self.user_form_content2.save(current_user=self.user2)

    def validate_type_assignation(self):
        '''
        Checks that the saved UserFormContent has the expected automatically assigned attributes
        '''
        workflow_sequence = WorkflowSequence(workflow=self.workflow1, form_step=self.user_form1, order=1)
        workflow_sequence.save(current_user=self.user1)  # Pass the current user as an argument to the save() method
        saved_workflow_sequence = WorkflowSequence.objects.get(id=workflow_sequence.id)

        
        self.assertEqual(saved_workflow_sequence.type, 'Form')

    def validate_single_step_condition(self):
        '''
        Checks that the workflow_sequence can't have more than one step
        '''
        workflow_sequence = WorkflowSequence(workflow=self.workflow1, form_step=self.user_form1, approval_step=self.user_form3, order=1)
        with self.assertRaises(ValidationError):
            workflow_sequence.full_clean() # Should raise ValidationError because two steps were added

    def test_validate_company(self):
        '''
        Checks that the workflow and the form_step are from the same company
        '''
        workflow_sequence = WorkflowSequence(workflow=self.workflow1, form_step=self.user_form2, order=1)
        with self.assertRaises(ValidationError):
            workflow_sequence.save(current_user=self.user1) # Should raise ValidationError because the workflow and the form_step are from different companies
    
            