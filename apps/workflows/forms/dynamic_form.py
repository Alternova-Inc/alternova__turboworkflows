from django import forms

class DynamicForm(forms.Form):
    """
    A dynamic form that generates form fields based on the provided json_fields.

    :param json_fields: A dictionary containing the field names as keys and field types as values.
                        The field types can be 'ShortText', 'Numeric', 'LongText', 'MultipleSelection',
                        'SingleSelection', 'Date', or 'Boolean'.

    Example:
    {
        "name": "CharField",
        "age": "IntegerField",
        "Personal Intro": "TextField",
        "Hobbies": {
            "type": "MultipleSelection",
            "choices": ["Reading", "Writing", "Coding"]
        },
        "Country": {
            "type": "SingleSelection",
            "choices": ["Colombia", "USA", "UK"]
        },
        "Birthdate": "Date",
        "Is Employed": "Boolean"
    }
    """

    def __init__(self, *args, **kwargs):
        json_fields = kwargs.pop('json_fields')
        super(DynamicForm, self).__init__(*args, **kwargs)
        
        for name, field_info in json_fields.items():
            if isinstance(field_info, dict) and 'type' in field_info:
                field_type = field_info['type']
                if field_type == 'MultipleSelection':
                    choices_array = field_info.get('choices', [])
                    choices = [(i, choice) for i, choice in enumerate(choices_array)]
                    self.fields[name] = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple())
                elif field_type == 'SingleSelection':
                    choices_array = field_info.get('choices', [])
                    choices = [(i, choice) for i, choice in enumerate(choices_array)]
                    self.fields[name] = forms.ChoiceField(choices=choices)
            else:
                field_type = field_info
                if field_type == 'ShortText':
                    self.fields[name] = forms.CharField(max_length=150)
                elif field_type == 'Numeric':
                    self.fields[name] = forms.FloatField()
                elif field_type == 'LongText':
                    self.fields[name] = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 500}))
                elif field_type == 'Date':
                    self.fields[name] = forms.DateField()
                elif field_type == 'Boolean':
                    self.fields[name] = forms.BooleanField()
                
                # Add more field types as needed
                