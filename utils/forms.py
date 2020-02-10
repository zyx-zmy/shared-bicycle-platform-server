from django.forms.fields import Field
from django.utils.translation import ugettext_lazy
from django.core import validators
from django.core.exceptions import ValidationError
import json


def validate_form(form_class, data):
    form = form_class(data)
    if form.is_valid():
        return True, form.cleaned_data
    errors = []
    for key, field in form.declared_fields.items():
        if field.required and key not in data:
            errors.append({"field": key, "code": "missing_field"})
        elif key in form.errors:
            errors.append({"field": key, "code": "invalid"})
    return False, errors


class SimpleDictField(Field):
    default_error_messages = {
        'invalid': ugettext_lazy('Enter a valid value.'),
    }

    def __init__(self, inner_field=None, *args, **kwargs):
        self.inner_field = inner_field
        super(SimpleDictField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return None
        if type(value) is str:
            try:
                value = json.loads(value)
            except ValueError:
                pass
        if type(value) is not dict:
            raise ValidationError(self.error_messages['invalid'])
        return value


class NullBooleanField(Field):
    values = {
        '0': False,
        '1': True,
        'true': True,
        'false': False,
        'True': True,
        'False': False
    }

    def clean(self, value):
        super(NullBooleanField, self).clean(value)

        if not self.required:
            if value in [None, '']:
                return None

        value = str(value).lower()
        if value not in self.values:
            raise ValidationError('', code='type_invalid')

        return self.values[value]
