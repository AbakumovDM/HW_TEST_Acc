import unittest
from parameterized import parameterized
from main import people, shelf, list_, add
from unittest.mock import patch

class TestAccountingUnitTest(unittest.TestCase):
    # def test_people(self):
    #     self.assertEqual('Геннадий Покемонов', people('11-2'))
    #
    # def test_people_doc_not_exist(self):
    #     self.assertIsNone(people('123-2'))
    #
    # def test_shelf(self):
    #     self.assertEqual('Номер полки 1', shelf('2207 876234'))
    #
    # def test_shelf_doc_not_exist(self):
    #     self.assertIsNone(shelf('123-2'))
    #
    # def test_list_(self):
    #     self.assertEqual([('passport', '2207 876234', 'Василий Гупкин'), ('invoice', '11-2', 'Геннадий Покемонов'), ('insurance', '10006', 'Аристарх Павлов')], list_())
    #
    # def test_add(self):
    #     self.assertEqual('документ паспорт с номером 0000 добавлен на полку 3', add('паспорт', '0000', 'Иван Иванов', '3'))
    #
    # def test_add_shelf_not_exist(self):
    #     self.assertEqual('Такой полки не существует', add('паспорт', '0000', 'Иван Иванов', '4'))

    @parameterized.expand([
        ["people", "Геннадий Покемонов", people('11-2')],
        ["people_doc_not_exist", None, people('123-2')],
        ["shelf", "Номер полки 1", shelf('2207 876234')],
        ["shelf_doc_not_exist", None, shelf('123-2')],
        ["list_", [('passport', '2207 876234', 'Василий Гупкин'), ('invoice', '11-2', 'Геннадий Покемонов'), ('insurance', '10006', 'Аристарх Павлов')], list_()],
        ["add", 'документ паспорт с номером 0000 добавлен на полку 3', add('паспорт', '0000', 'Иван Иванов', '3')],
        ["add_shelf_not_exist", 'Такой полки не существует', add('паспорт', '0000', 'Иван Иванов', '4')]
    ])
    def test_accounting(self, test_name, expected, actual):
        self.assertEqual(expected, actual)