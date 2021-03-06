import requests

from plotly.graph_objs import Bar
from plotly import offline
def github_python_reponse():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    # Store API response in a variable.
    response_dict = r.json()
    # Process results.
    print(response_dict.keys())
    print(f"Total repositories: {response_dict['total_count']}")
    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    repo_links, stars, labels = [], [], []
    print(f"Repositories returned: {len(repo_dicts)}")
    # Examine the first repository.
    repo_dict = repo_dicts[0]
    print(f"\nKeys: {len(repo_dict)}")
    for key in sorted(repo_dict.keys()):
        print(key)
    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)
        stars.append(repo_dict['stargazers_count'])
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        print(f"Name: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")
        print('')
    data = [Bar(x=repo_links, y=stars, text=labels, marker={
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
                opacity=0.6)]
    my_layout = {
        'title': 'Most-Starred Python Projects on GitHub',
        'xaxis': {'title': 'Repository'},
        'yaxis': {'title': 'Stars'},
    }
    fig = {'data': data, 'layout': my_layout}
    return offline.plot(fig, filename='python_repos.html')
github_python_reponse()