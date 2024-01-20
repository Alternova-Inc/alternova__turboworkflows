from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from apps.authentication.models.role import Role
from apps.workflows.models.workflow import Workflow
from apps.authentication.models import Company

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
