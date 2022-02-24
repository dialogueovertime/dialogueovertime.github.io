import json

with open('./src/dotblog/static/episodes.json') as f:
    episodes = json.load(f)

def insertStatement(e):
    statement = f"""INSERT into episodes VALUES(
        {e['EpisodeNumber']},
        {e['Title']},
        {e['ReleaseDate']},
        {e['RunTime(min)']},
        {e['MiddleSegment']},
        {e['OneLastThing']};\n"""
    statement += f"""INSERT into episodeHosts"""

def insertHosts():
    "INSERT into hosts VALUES(1, 'Chris');"
    "INSERT into hosts VALUES(2, 'Cody');"
    "INSERT into hosts VALUES(3, 'Paul');"