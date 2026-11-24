"""Task 1: recommend an unwatched film from similar viewing histories."""
import argparse
from collections import Counter
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent
MOVIES_FILE = DATA_DIR / "movies.txt"
HISTORY_FILE = DATA_DIR / "history.txt"


def parse_ids(line):
    """Convert comma-separated movie IDs to a list of integers."""
    return [int(item.strip()) for item in line.split(",") if item.strip()]


class MovieCatalog:
    def __init__(self, movies):
        self.movies = dict(movies)

    @classmethod
    def from_file(cls, path):
        movies = {}
        with open(path, encoding="utf-8-sig") as file:
            for line in file:
                if line.strip():
                    movie_id, title = line.strip().split(",", 1)
                    movies[int(movie_id)] = title.strip()
        return cls(movies)

    def get_title(self, movie_id):
        return self.movies[movie_id]


class MovieRecommender:
    def __init__(self, catalog, histories):
        self.catalog = catalog
        self.histories = histories

    @classmethod
    def from_files(cls, movies_path, history_path):
        catalog = MovieCatalog.from_file(movies_path)
        with open(history_path, encoding="utf-8-sig") as file:
            histories = [parse_ids(line) for line in file if line.strip()]
        return cls(catalog, histories)

    def recommend(self, watched, weighted=False):
        watched = set(watched)
        if not watched:
            return None

        scores = Counter()
        for history in self.histories:
            common = len(watched.intersection(history))
            # At least half of the current user's distinct films must match.
            if common * 2 < len(watched):
                continue
            weight = common / len(watched) if weighted else 1

            # Retain repeated views, but never recommend an already watched film.
            for movie_id in history:
                if movie_id not in watched and movie_id in self.catalog.movies:
                    scores[movie_id] += weight

        if not scores:
            return None

        # The task allows any tied movie; choose the smallest ID deterministically.
        best_id = min(scores, key=lambda movie_id: (-scores[movie_id], movie_id))
        return self.catalog.get_title(best_id)


def main():
    parser = argparse.ArgumentParser(description="Movie recommendation")
    parser.add_argument("--weighted", action="store_true")
    parser.add_argument("--movies", type=Path, default=MOVIES_FILE)
    parser.add_argument("--history", type=Path, default=HISTORY_FILE)
    args = parser.parse_args()
    recommender = MovieRecommender.from_files(args.movies, args.history)
    result = recommender.recommend(parse_ids(input()), weighted=args.weighted)
    print(result if result is not None else "Нет рекомендаций")


if __name__ == "__main__":
    main()
