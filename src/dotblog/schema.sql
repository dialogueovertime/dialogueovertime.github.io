DROP TABLE IF EXISTS episodes;
DROP TABLE IF EXISTS hosts;
DROP TABLE IF EXISTS episodeHosts;

CREATE TABLE episodes (
    episodeNumber INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    releaseDate TEXT NOT NULL,
    runTimeMinutes INTEGER NOT NULL,
    segment TEXT NOT NULL,
    oneLastThing TEXT NOT NULL
);

CREATE TABLE hosts (
    hostID INTEGER PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT,
    email TEXT,
    twitter TEXT,
    bio TEXT
);

CREATE TABLE episodeHosts (
    episode INTEGER NOT NULL,
    host INTEGER NOT NULL,
    leadHost INTEGER NOT NULL,
    FOREIGN KEY (episode) REFERENCES episodes(episodeNumber),
    FOREIGN KEY (host) REFERENCES hosts(hostID)
);