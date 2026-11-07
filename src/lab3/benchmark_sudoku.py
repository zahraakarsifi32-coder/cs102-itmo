
import time
from concurrent.futures import ProcessPoolExecutor

from sudoku import read_sudoku, solve, check_solution


if __name__ == "__main__":
    names = ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]

    puzzles = [read_sudoku(name) for name in names]

    start = time.perf_counter()

    with ProcessPoolExecutor(max_workers=3) as executor:
        solutions = list(executor.map(solve, puzzles))

    elapsed = time.perf_counter() - start

    print("Multiprocessing:", round(elapsed, 3), "seconds")

    print("Solutions valid:", [
        solution is not None and check_solution(solution)
        for solution in solutions
    ])
