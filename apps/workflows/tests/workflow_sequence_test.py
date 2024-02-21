from apps.defaults.tests import BaseTestCase
from django.core.exceptions import ValidationError
from apps.workflows.models.workflow_sequence import WorkflowSequence

# Create your tests here.
class WorkflowSequenceTest(BaseTestCase):
    ''''
    Test module for WorkflowSequence model
    '''

    def validate_type_assignation(self):
        '''
        Checks that the saved UserFormContent has the expected automatically assigned attributes
        '''
        workflow_sequence = WorkflowSequence(workflow=self.workflow1, form_step=self.user_form1, order=1)
        workflow_sequence.save()
        saved_workflow_sequence = WorkflowSequence.objects.get(id=workflow_sequence.id)

        self.assertEqual(saved_workflow_sequence.type, 'Form')

    def validate_single_step_condition(self):
        '''
        Checks that the workflow_sequence can't have more than one step
        '''
        workflow_sequence = WorkflowSequence(workflow=self.workflow1, form_step=self.user_form1, approval_step=self.user_approval1, order=1)
        with self.assertRaises(ValidationError):
            workflow_sequence.full_clean() # Should raise ValidationError because two steps were added

    def test_validate_company(self):
        '''
        Checks that the workflow and the form_step are from the same company
        '''
        workflow_sequence = WorkflowSequence(workflow=self.workflow1, form_step=self.user_form2, order=1)
        with self.assertRaises(ValidationError):
            workflow_sequence.save(current_user=self.user1) # Should raise ValidationError because the workflow and the form_step are from different companies
            