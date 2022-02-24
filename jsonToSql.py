import json

with open('./src/dotblog/static/episodes.json') as f:
    episodes = json.load(f)

hostMap = {
    "Chris": 1,
    "Cody": 2,
    "Paul": 3,
    "Eliza (guest)": 4
}

statements = []

for h in hostMap:
    statements.append(f"INSERT into hosts (hostID, firstName) VALUES({hostMap[h]}, '{h}');\n")

for e in episodes:
    statements.append(f"""INSERT into episodes VALUES(
        {e['EpisodeNumber']},
        "{e['Title']}",
        "{e['ReleaseDate']}",
        {e['RunTime(min)']},
        "{e['MiddleSegment']}",
        "{e['OneLastThing']}");\n""")
    for h in e['Hosts']:
        statements.append(f"""INSERT into episodeHosts VALUES(
            {e['EpisodeNumber']},
            '{hostMap[h]}',
            0);\n""")

with open('./src/dotblog/seed.sql', 'w') as f:
    f.writelines(statements)

