from github import Github

g = Github("XXXXXXXX")

for repo in g.get_user().get_repos():
    print(repo)
    pulls = repo.get_pulls()
    pulls_numbers_list = []
    for pull in pulls:
    	pulls_numbers_list.append(pull.number)

    print(pulls_numbers_list)