from myClass import Repo

myRepo = Repo()
unsuccessful = True
while(unsuccessful):
    try:
        numContributors = int(input("How many contributors are in your repository: "))
        unsuccessful = False
    except:
        print("That is not an integer!")
    
for i in range(numContributors):
    contributor = input("Enter contributor " + str(i + 1) + ": ")
    myRepo.addContributor(contributor)
    
contributors = "|"
for contributor in myRepo.contributors:
    contributors += contributor
    contributors += "|"
    
print("Contributors in the repository: " + contributors)