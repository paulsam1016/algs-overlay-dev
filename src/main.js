// TAS Match ID
// 
var matchId = 1601;
// 
// 
// TAS URL
// 
var url = 'https://algs.tas.gg/api/match/';
// 
// 

var text;

async function getALGSData() {
    console.log(url + matchId);
    var theUrl = url + matchId;
    let response = await new Promise(resolve => {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("GET", theUrl, true);
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
    const regex = /([\w\d]+) ([0-9]+\W)/g;
    const matches = responseText.match(regex);
    console.log(matches);

    var title = document.getElementById("marquee-sibling");
    title.innerHTML = responseText.split('-')[0] + ' ' + responseText.split('----')[1];
    title.style = '';

    var contentElements = document.getElementsByClassName("marquee-content-items");
    for (var j = 0; j < contentElements.length; j++) {
        contentElements[j].innerHTML = '';

        for (var i = 0; i < matches.length - 1; i++) {
            var match = matches[i];
            if (match[match.length - 1] == ',' || match[match.length - 1] == ' ') {
                match = match.slice(0, -1);
            }
            var innerDiv = document.createElement('li');
            innerDiv.innerHTML = match;
            contentElements[j].appendChild(innerDiv);
        }
    }
}