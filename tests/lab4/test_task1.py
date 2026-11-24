import unittest

from src.lab4.task1 import HISTORY_FILE, MOVIES_FILE, MovieCatalog, MovieRecommender, parse_ids


class MovieRecommenderTests(unittest.TestCase):
    def setUp(self):
        self.catalog = MovieCatalog({1: "A", 2: "B", 3: "C", 4: "D", 5: "E"})

    def test_assignment_example(self):
        recommender = MovieRecommender.from_files(MOVIES_FILE, HISTORY_FILE)
        self.assertEqual(recommender.recommend([2, 4]), "Дюна")

    def test_parse_ids(self):
        self.assertEqual(parse_ids("2, 4,2"), [2, 4, 2])

    def test_at_least_half_and_ignore_unmatched_histories(self):
        recommender = MovieRecommender(self.catalog, [[1, 3], [4, 4, 4]])
        self.assertEqual(recommender.recommend([1, 2]), "C")

    def test_odd_number_of_watched_films(self):
        recommender = MovieRecommender(self.catalog, [[1, 4, 4, 4], [1, 2, 5]])
        self.assertEqual(recommender.recommend([1, 2, 3]), "E")

    def test_repeated_views_count(self):
        recommender = MovieRecommender(self.catalog, [[1, 3, 3], [1, 4]])
        self.assertEqual(recommender.recommend([1]), "C")

    def test_duplicate_watched_ids_do_not_change_similarity(self):
        recommender = MovieRecommender(self.catalog, [[2, 3]])
        self.assertEqual(recommender.recommend([1, 1, 2]), "C")

    def test_weighted_extension(self):
        recommender = MovieRecommender(self.catalog, [[1, 3], [1, 2, 4]])
        self.assertEqual(recommender.recommend([1, 2]), "C")
        self.assertEqual(recommender.recommend([1, 2], weighted=True), "D")

    def test_no_candidate(self):
        recommender = MovieRecommender(self.catalog, [[1, 2]])
        self.assertIsNone(recommender.recommend([1, 2]))
        self.assertIsNone(recommender.recommend([]))


if __name__ == "__main__":
    unittest.main()
