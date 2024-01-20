from django.test import TestCase

# Create your tests here.
from apps.authentication.models import Company, Role

class CreateRoleForCompanySignalTest(TestCase):
    def setUp(self):
        # Create a company
        self.company = Company.objects.create(company_name='Test Company')

    def test_roles_created_for_new_company(self):
        # Check that a 'default' Role was created for the new Company
        default_role = Role.objects.filter(company=self.company, role_name='default')
        self.assertTrue(default_role.exists(), "'default' Role was not created for new company")
        self.assertTrue(default_role.first().is_default, "'default' Role is not set as default")

        # Check that an 'admin' Role was created for the new Company
        admin_role = Role.objects.filter(company=self.company, role_name='admin')
        self.assertTrue(admin_role.exists(), "'admin' Role was not created for new company")
