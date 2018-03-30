# Import the admin codes, and the github python api library
import admin_codes
import github

# Set up the github api authentication stuff
github_api = github.GitHub(admin_codes.username, admin_codes.password)

# get a list of the repos
repos = github_api.user.repos.get()

username = input("Enter the user to be removed from all bargreenellingson repos: ")

for repo in repos:
    github_api.repos('bargreenellingson')(repo.name).collaborators(username).delete()

print(username +" has been removed from all repositories, thanks and come again!")