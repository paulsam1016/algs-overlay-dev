var text;

async function getALGSData() {
    var url = config['matchUrl'];
    let response = await new Promise(resolve => {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("GET", url, true);
        xmlHttp.onload = function (e) {
            resolve(xmlHttp.response);
        };
        xmlHttp.onerror = function () {
            resolve(undefined);
            console.error("** An error occurred during the XMLHttpRequest");
        };
        xmlHttp.send();
    });
    if (response)
        processRequest(response);
};

function processRequest(responseText) {
    text = responseText;
    titleText = responseText.split('-')[0].trim().replace(":", " |");
    points = responseText.split('---')[1].split('----')[0];
    game = responseText.split('----')[1].trim();

    const regex = /(\S+ [0-9]+)(,|\Z| )/g;
    const matches = points.match(regex);

    var title = document.getElementById("marquee-sibling-text");
    title.style = '';
    title.innerHTML = titleText + ' | ' + game;

    $(".marquee-sibling-cover").css({
        'width': ($(".marquee-sibling-text").width() + 56 + 'px')
    });

    var contentElements = document.getElementsByClassName("marquee-content-items");
    for (var j = 0; j < contentElements.length; j++) {
        contentElements[j].innerHTML = '';

        for (var i = 0; i < matches.length; i++) {
            var match = matches[i];
            if (match[match.length - 1] == ',' || match[match.length - 1] == ' ') {
                match = match.slice(0, -1);
            }
            var shortName = match.split(' ')[0];
            var score = match.split(' ')[1];
            var team = getTeam(shortName);

            var innerli = document.createElement('li');

            if (config['showLogo']) {
                var innerImg = document.createElement('img');
                innerImg.className = 'item-img';
                innerImg.src = team.path;
                innerli.appendChild(innerImg);
            }

            var innerText = document.createElement('div');
            innerText.className = 'item-text';
            if (config['isShort']) {
                innerText.innerHTML = match;
            }
            else {
                innerText.innerHTML = team.teamName + ' ' + score;
            }
            if (config['showLogo']) {
                innerText.style = 'left: 76px;';
            }

            innerli.appendChild(innerText);
            contentElements[j].appendChild(innerli);
            var extraWidth = innerText.offsetWidth + 56;
            if (config['showLogo']) {
                extraWidth = extraWidth + 48;
            }
            innerli.style.width = extraWidth + 'px';
        }
    }
}

function getTeam(shortName) {
    for (var i = 0; i < teamData.length; i++) {
        if (teamData[i].shortName == shortName) {
            return teamData[i];
        }
    }
}