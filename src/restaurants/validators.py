from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
		
def validate_email(value):
		email = value
		if ".edu" in email:
			raise ValidationError('We do not accept .edu emails')

CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']		

def validate_category(value):
	cat = value.capitalize()
	if value not in CATEGORIES and cat not in CATEGORIES:
		raise ValidationError('{} is not a valid category'.format(value))
