from django.test import TestCase
from apps.authentication.models.role import Role
from apps.defaults.models import StatusMessage
from django.contrib.auth import get_user_model
from apps.authentication.models.profile import Profile
from apps.workflows.models import Workflow, WorkflowStepForm, UserFormField, UserFormContent
from apps.authentication.models import Company
from django.contrib.auth import get_user_model
from apps.authentication.models.company_profile_set import CompanyProfileSet
from apps.workflows.models.workflow_step_approval import WorkflowStepApproval
from apps.authentication.models.company_department import CompanyDepartment
from apps.authentication.models.company_position import CompanyPosition

# Create your tests here.
class StatusMessageTestCase(TestCase):
    def test_is_active_default(self):
        # Create a new StatusMessage instance
        status_message = StatusMessage.objects.create(
            status_message_name="Test message",
            content="Test content"
        )

        # Check if is_active is False
        self.assertFalse(status_message.is_active)

User = get_user_model()
class BaseTestCase(TestCase):
    # Create your tests here.
    
    def setUp(self):
        self.company1 = Company.objects.create(company_name='Company 1')
        self.company2 = Company.objects.create(company_name='Company 2')

        self.user1 = User.objects.create_user(username='user1', password='password', is_superuser=False)
        self.user2 = User.objects.create_user(username='user2', password='password', is_superuser=False)
        self.user3 = User.objects.create_user(username='user3', password='password', is_superuser=True)
        self.user4 = User.objects.create_user(username='user4', password='password', is_superuser=True)

        self.profile1 = Profile.objects.create(user=self.user1)
        self.profile2 = Profile.objects.create(user=self.user2)
        self.profile3 = Profile.objects.create(user=self.user3)
        self.profile4 = Profile.objects.create(user=self.user4)

        self.workflow1 = Workflow.objects.create(company=self.company1, workflow_name='Test Workflow 1')
        self.workflow2 = Workflow.objects.create(company=self.company2, workflow_name='Test Workflow 2')

        self.role1 = Role.objects.create(company=self.company1, role_name='Role 1')
        self.role2 = Role.objects.create(company=self.company2, role_name='Role 2')
        
        self.role1.workflows.add(self.workflow1)
        self.role2.workflows.add(self.workflow2)

        self.department1 = CompanyDepartment.objects.create(company=self.company1, department_name='Department 1')
        self.department2 = CompanyDepartment.objects.create(company=self.company2, department_name='Department 2')

        self.position1 = CompanyPosition.objects.create(company=self.company1, position_name='Position 1', is_approver=True)
        self.position2 = CompanyPosition.objects.create(company=self.company2, position_name='Position 2')

        self.CompanyProfileSet1 = CompanyProfileSet.objects.create(profile=self.profile1, company=self.company1, role=self.role1,
                                                                   department=self.department1, position=self.position1, direct_manager=self.profile3)
        self.CompanyProfileSet2 = CompanyProfileSet.objects.create(profile=self.profile2, company=self.company2, role=self.role2,
                                                                   department=self.department2, position=self.position2, direct_manager=self.profile4)
        self.CompanyProfileSet3 = CompanyProfileSet.objects.create(profile=self.profile3, company=self.company1, role=self.role1,
                                                                   department=self.department1, position=self.position1, direct_manager=self.profile3)
        self.CompanyProfileSet4 = CompanyProfileSet.objects.create(profile=self.profile4, company=self.company2, role=self.role2,
                                                                   department=self.department2, position=self.position2, direct_manager=self.profile4)

        self.user_form1 = WorkflowStepForm.objects.create(company=self.company1, workflow_step_name='UserForm 1')
        self.user_form2 = WorkflowStepForm.objects.create(company=self.company2, workflow_step_name='UserForm 2')
        self.user_approval1 = WorkflowStepApproval.objects.create(company=self.company1, workflow_step_name='User Approval 1', required_position=self.position1)

        self.field1 = UserFormField.objects.create(company=self.company1, public_name='Field 1', code='1', type='LongText')
        self.field2 = UserFormField.objects.create(company=self.company2, public_name='Field 2', code='2', type='ShortText')

        self.user_form_content1 = UserFormContent(user_form=self.user_form1, field=self.field1, order=1)
        self.user_form_content2 = UserFormContent(user_form=self.user_form2, field=self.field2, order=1)
        