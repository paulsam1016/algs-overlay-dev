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
        'width': ($(".marquee-sibling-text").width() + 48 + 'px')   // 48 padding
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


            var innerli = document.createElement('li');
            if (config['showLogo'] || config['isFullName']) {
                var team = getTeam(shortName);
            }

            if (team && config['showLogo']) {
                var innerImg = document.createElement('img');
                innerImg.className = 'item-img';
                innerImg.src = team.path;
                innerli.appendChild(innerImg);
            }
            var innerText = document.createElement('div');
            innerText.className = 'item-text';
            if (team && config['isFullName']) {
                innerText.innerHTML = team.teamName + ' ' + score;
            }
            else {
                innerText.innerHTML = match;
            }
            if (team && config['showLogo']) {
                innerText.style = 'left: 66px;';    // 40 logo width + 20 margin + 6 padding
            }

            innerli.appendChild(innerText);
            contentElements[j].appendChild(innerli);
            var extraWidth = innerText.offsetWidth + 48;    // 48 padding
            if (team && config['showLogo']) {
                extraWidth = extraWidth + 40; // 40 logo width
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