import unittest

from src.lab4.task2 import Respondent, Survey


class SurveyTests(unittest.TestCase):
    def test_boundaries_and_group_order(self):
        survey = Survey([18, 25, 100])
        for name, age in [("A", 0), ("B", 18), ("C", 19), ("D", 25), ("E", 26), ("F", 100), ("G", 101)]:
            survey.add(Respondent(name, age))
        self.assertEqual(survey.results(), [
            "101+: G (101)", "26-100: F (100), E (26)",
            "19-25: D (25), C (19)", "0-18: B (18), A (0)",
        ])

    def test_name_tie_and_skip_empty_groups(self):
        survey = Survey([18, 25, 35])
        for name, age in [("Иванов", 21), ("Дьячков", 21), ("Соколов", 23)]:
            survey.add(Respondent(name, age))
        self.assertEqual(survey.results(), ["19-25: Соколов (23), Дьячков (21), Иванов (21)"])

    def test_empty_survey(self):
        self.assertEqual(Survey([18, 25]).results(), [])

    def test_invalid_boundaries(self):
        with self.assertRaises(ValueError):
            Survey([25, 18])
        with self.assertRaises(ValueError):
            Survey([18, 18])


if __name__ == "__main__":
    unittest.main()
