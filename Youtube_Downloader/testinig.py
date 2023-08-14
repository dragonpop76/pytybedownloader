import pytube.contrib.search
from pytube import Search
s = Search("YouTube Rewind 2020")
print(s.results)
results = s.results

# <pytube.contrib.search.Search object at 0x0000022375FEB950>

video = (results[0])

title = video.title

print(title)
