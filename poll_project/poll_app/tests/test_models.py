from django.test import TestCase
from ..models import Poll


class MyTestClass(TestCase):
    """
    Test that testing is working
    """
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData: Run once to set up non-modified data for all class methods.')
        pass

    def setUp(self):
        print('setUp: Run once for every test method to setup clean data.')
        pass

    def test_false_is_false(self):
        print('Method: test_false_is_false.')
        self.assertFalse(False)

    # @skipIf(True, 'Remove this test')
    # def test_false_is_true(self):
    #     print('Method: test_false_is_true')
    #     self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print('Method: test_one_plus_one_equals_two.')
        self.assertEqual(1 + 1, 2)


class PollTest(TestCase):
    """ Test for Poll model """

    def setUp(self):
        Poll.objects.create(
            name = 'Социологический опрос',
            start_date = '2020-07-10',
            end_date = '2020-07-11',
            description = 'Отражает общественное мнение')
        Poll.objects.create(
            name='Литературный опрос',
            start_date='2019-09-9',
            end_date='2019-10-10',
            description='Вопросы по литературе')

    def test_poll_name(self):
        poll_social = Poll.objects.get(name='Социологический опрос')
        poll_literature = Poll.objects.get(name='Литературный опрос')

