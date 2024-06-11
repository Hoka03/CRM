import os

username = os.environ.get("GITHUB_USERNAME")
token = os.environ.get("GITHUB_TOKEN")

os.system("git add .")
print('git add .')
message = input('git commit -m: ')
os.system(f"git commit -m '{message}'")
print('git push')
os.system(f"git push https://{username}:{token}@github.com/Hoka03/CRM.git")
