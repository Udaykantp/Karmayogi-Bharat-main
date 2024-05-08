class Contributor:
    def __init__(self, name):
        self.name = name
        self.contributions = []

    def add_contribution(self, contribution):
        self.contributions.append(contribution)

class Contribution:
    def __init__(self, date, description):
        self.date = date
        self.description = description

class KarmayogiBharat:
    def __init__(self):
        self.contributors = {}

    def add_contributor(self, name):
        if name not in self.contributors:
            self.contributors[name] = Contributor(name)

    def add_contribution(self, contributor_name, contribution):
        if contributor_name in self.contributors:
            self.contributors[contributor_name].add_contribution(contribution)
        else:
            print(f"Contributor '{contributor_name}' not found.")

# Example usage:
project = KarmayogiBharat()

project.add_contributor("Alice")
project.add_contributor("Bob")

project.add_contribution("Alice", Contribution("2024-05-08", "Implemented feature X"))
project.add_contribution("Bob", Contribution("2024-05-09", "Fixed bug Y"))

# Print contributions for each contributor
for contributor_name, contributor in project.contributors.items():
    print(f"{contributor_name}'s contributions:")
    for contribution in contributor.contributions:
        print(f"- {contribution.date}: {contribution.description}")
