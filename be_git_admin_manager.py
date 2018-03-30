# Import the admin codes, and the github python api library
import admin_codes
import github

# Import the GUI stuff
import tkinter

# Set up the github api authentication stuff
github_api = github.GitHub(admin_codes.username, admin_codes.password)

# get a list of the repos
repos = github_api.user.repos.get()

# Temporary Github add person to repository function
def addCollaborator(repoName, username):
    github_api.repos('bargreenellingson')(repoName).collaborators(username).put()

num = 0
for repo in repos:
    print (repo.name, num)
    num += 1

username = input("Enter the username to add as a collaborator: ")

do_things = 1
while(do_things):

    num = input("Select a repository to add a user to: ")
    num = int(num)

    addCollaborator(repos[num].name, username)

    temp = input("Keep going? (Enter 0 to quit)")
    do_things = int(temp)

#Gui stuff here
# root = tkinter.Tk()

# frame = tkinter.Frame(root)
# frame.pack()

# for repo in repos:
#     button = tkinter.Button(frame, 
#         text=repo.name, 
#         fg="green",
#         command=addCollaborator(repo.name))
#     button.pack(side=tkinter.LEFT)
# root.mainloop()