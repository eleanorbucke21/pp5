from django.forms import ModelForm
from .models import Poll


class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'choice_one', 'choice_two', 'choice_three']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'question': 'Question',
            'choice_one': 'Choice One',
            'choice_two': 'Choice Two',
            'choice_three': 'Choice Three',

        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].label = False
