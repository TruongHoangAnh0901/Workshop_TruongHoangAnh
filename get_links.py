import urllib.request, re
html = urllib.request.urlopen("https://nhattien21.github.io/AWS/").read().decode("utf-8")
links = set(re.findall(r"href=[\'\"]?(https://nhattien21.github.io/AWS/[^\'\"> ]*)", html))
for l in links: print(l)
