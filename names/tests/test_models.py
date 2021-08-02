from django.test import TestCase

from names.models import SampleName


class SampleNameModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SampleName.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        samplename = SampleName.objects.get(id=1)
        field_label = samplename._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        samplename = SampleName.objects.get(id=1)
        field_label = samplename._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_first_name_max_length(self):
        samplename = SampleName.objects.get(id=1)
        max_length = samplename._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 50)

    def test_last_name_max_length(self):
        samplename = SampleName.objects.get(id=1)
        max_length = samplename._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 50)

    def test_object_name_is_first_name_space_last_name(self):
        samplename = SampleName.objects.get(id=1)
        exp_object_name = f'{samplename.first_name} {samplename.last_name}'
        self.assertEqual(str(samplename), exp_object_name)
