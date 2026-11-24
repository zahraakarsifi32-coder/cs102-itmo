"""Task 2: group survey respondents by age and format the results."""
import argparse
import sys


class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


class AgeGroup:
    def __init__(self, lower, upper=None):
        self.lower = lower
        self.upper = upper
        self.respondents = []

    def contains(self, age):
        return age >= self.lower and (self.upper is None or age <= self.upper)

    def label(self):
        if self.upper is None:
            return f"{self.lower}+"
        return f"{self.lower}-{self.upper}"

    def format(self):
        ordered = sorted(self.respondents, key=lambda person: (-person.age, person.name))
        return f"{self.label()}: " + ", ".join(str(person) for person in ordered)


class Survey:
    def __init__(self, boundaries):
        boundaries = list(boundaries)
        if any(value < 0 for value in boundaries) or boundaries != sorted(set(boundaries)):
            raise ValueError("Age boundaries must be nonnegative and strictly increasing")
        self.groups = []
        lower = 0
        for upper in boundaries:
            self.groups.append(AgeGroup(lower, upper))
            lower = upper + 1
        self.groups.append(AgeGroup(lower))

    def add(self, respondent):
        for group in self.groups:
            if group.contains(respondent.age):
                group.respondents.append(respondent)
                return
        raise ValueError("Age must be nonnegative")

    def results(self):
        return [group.format() for group in reversed(self.groups) if group.respondents]


def main():
    parser = argparse.ArgumentParser(description="Group respondents by age")
    parser.add_argument("boundaries", type=int, nargs="+")
    args = parser.parse_args()
    survey = Survey(args.boundaries)
    for line in sys.stdin:
        line = line.strip()
        if line == "END":
            break
        if not line:
            continue
        name, age = line.rsplit(",", 1)
        survey.add(Respondent(name.strip(), int(age)))
    for line in survey.results():
        print(line)


if __name__ == "__main__":
    main()
