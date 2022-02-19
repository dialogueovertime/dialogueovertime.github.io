function getEpisodes() {
    fetch("static/episodes.json")
        .then(response => {return response.json()})
        .then(json => {
            insertTable(json)
        });
}

getEpisodes();

function insertTable(episodes) {
    console.log(episodes);

    var headerRow = document.getElementById('headerRow');
    Object.keys(episodes[0]).forEach(header => {
        let th = document.createElement('th');
        th.textContent = header;
        headerRow.append(th);
    });

    var episodeList = document.getElementById('episodeList');
    episodes.forEach(episode => {
        let r = document.createElement('tr');
        // console.log(episode);
        Object.values(episode).forEach(property => {
            let td = document.createElement('td');
            td.textContent = property;
            r.append(td);
            // console.log(property);
        })
        episodeList.append(r)
    })

}

