import requests



response = requests.get("https://gitlab.com/api/v4/users/princekwes/projects")
out_put = response.json()

# print(out_put)

for items in out_put:
    print(f" Project Name: {items['name']} Project Url: {items['web_url']}")
