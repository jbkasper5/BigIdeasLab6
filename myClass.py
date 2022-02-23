class Repo:
    def __init__(self):
        self.owner = "Jake"
        self.contributors = []
        self.creationDate = {
            "Month": "February",
            "Day": 16,
            "Year": 2022
        }
    
    def addContributor(self, contributor):
        self.contributors.append(contributor)