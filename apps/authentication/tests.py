from django.forms import ValidationError
from django.test import TestCase

# Create your tests here.
from apps.authentication.models import Company, Role
from apps.defaults.tests import BaseTestCase

class CreateRoleForCompanySignalTest(TestCase):
    """
    Test case for the signal that creates default roles for a new company.
    """
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

class CompanyProfileSetTest(BaseTestCase):
    """
    Test module for the CompanyProfileSet model
    """

    def test_user_must_have_direct_manager(self):
        from apps.authentication.models.company_profile_set import CompanyProfileSet
        """
        Test that a user must have a direct_manager
        """
        self.CompanyProfileSet1.direct_manager = None
        with self.assertRaises(CompanyProfileSet.direct_manager.RelatedObjectDoesNotExist):
            self.CompanyProfileSet1.full_clean()

    def test_user_cannot_be_own_direct_manager(self):
        """
        Test that a non is_superuser user can't be its own direct_manager
        """
        self.CompanyProfileSet1.direct_manager = self.profile1   
        with self.assertRaises(ValidationError):
            self.CompanyProfileSet1.full_clean()
