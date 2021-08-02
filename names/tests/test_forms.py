from django.test import SimpleTestCase

from names.forms import SampleNameForm


class SampleNameFormTest(SimpleTestCase):

    def test_sample_name_form_first_name_help_text(self):
        form = SampleNameForm()
        self.assertEqual(
            form.fields['first_name'].help_text, 'Enter your first name')

    def test_sample_name_form_last_name_help_text(self):
        form = SampleNameForm()
        self.assertEqual(
            form.fields['last_name'].help_text, 'Enter your last name')
