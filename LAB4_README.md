# Lab 4 — reconstructed practice project

Recreated from the supplied assignment, not recovered from the original laptop.
No external dependencies. Run from this folder or the root of the cloned repository.

## Task 1 — Movie recommendations

```powershell
py -m src.lab4.task1
```

Enter `2,4` and press Enter. Expected output: `Дюна`.

The provided text files contain the assignment's example data, not any larger original datasets.
Replace them if separate official files are available. Alternatively use `--movies` and `--history`.
The optional weighted extension is enabled by `py -m src.lab4.task1 --weighted`.
Similarity uses distinct movie IDs; repeated views count toward recommendation scores.
For ties the smallest ID is chosen, and if no recommendation exists the program prints `Нет рекомендаций` (the task does not prescribe this case).

## Task 2 — Age groups

```powershell
py -m src.lab4.task2 18 25 35 45 60 80 100
```

Enter one respondent per line, for example:

```text
Иванов Варлам Якунович,88
Дьячков Нисон Иринеевич,88
Соколов Андрей Сергеевич,15
Кошельков Захар Брониславович,105
END
```

Expected output:

```text
101+: Кошельков Захар Брониславович (105)
81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)
0-18: Соколов Андрей Сергеевич (15)
```

## Unit tests

```powershell
py -m unittest discover -s tests/lab4 -v
```

If `py` is unavailable but `python` works, substitute `python` in all commands.

## Integrating with your existing repository

Copy only `src/lab4` to the repository's `src` directory and `tests/lab4` to its `tests` directory. Do not overwrite existing Lab 4 files before checking them. Do not overwrite the repository's README or requirements. Use the branch and submission workflow required by the teacher.
