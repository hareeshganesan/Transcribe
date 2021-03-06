$(document).ready(function () {});

//Model
function Word(word, time) {
    this.word = word;
    this.time = time;
}

//Controller
function wordToLink(wordObj) {
    return "<a" + " onclick=seekTo(" + wordObj.time + ")" + " href=#" + ">" + wordObj.word + "<\a>";
}

//View
function seekTo(secs) {
    player.seekTo(secs, true);
    player.playVideo();
}

var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '390',
        width: '640',
        videoId: 'tlxfwPqB9dw',
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {}

function onPlayerStateChange(event) {}

//BUttons
$("#getvideo")
    .button()
    .click(function (event) {
    url = $("#vidurl").val()
    player.loadVideoById(url.substring(url.search("v=") + 2));
});

$("#save")
    .button()
    .click(function (event) {
    $("#save-note").submit(function () {
        alert("saved!");
        $("#notetext").val($("#notebox").html());
        $("#video_url").val(player.getVideoUrl());
        return true;
    });
});

function setEndOfContenteditable(contentEditableElement) {
    var range, selection;
    if (document.createRange) //Firefox, Chrome, Opera, Safari, IE 9+
    {
        range = document.createRange(); //Create a range (a range is a like the selection but invisible)
        range.selectNodeContents(contentEditableElement); //Select the entire contents of the element with the range
        range.collapse(false); //collapse the range to the end point. false means collapse to end rather than the start
        selection = window.getSelection(); //get the selection object (allows you to change selection)
        selection.removeAllRanges(); //remove any selections already made
        selection.addRange(range); //make the range you have just created the visible selection
    } else if (document.selection) //IE 8 and lower
    {
        range = document.body.createTextRange(); //Create a range (a range is a like the selection but invisible)
        range.moveToElementText(contentEditableElement); //Select the entire contents of the element with the range
        range.collapse(false); //collapse the range to the end point. false means collapse to end rather than the start
        range.select(); //Select the range (make it the visible selection
    }
}

lastWord = new Word("", 0.0);
wordSet = [];
beginning = false;

$('#notebox').keypress(function (event) {
    if (beginning) {
        beginning = true;
        lastWord.time = player.getCurrentTime();
    }

    character = String.fromCharCode(event.charCode);
    lastWord.word = lastWord.word + character;

    if (event.keyCode == 32) {
        wordSet.push(jQuery.extend(deep = true, {}, lastWord)); //deep copy the old word into the wordset
        lastWord = new Word("", player.getCurrentTime());
    }
    if (wordSet.length % 10 == 0 && wordSet.length > 0) {
        displayLinks();
    }

});

function displayLinks() {
    fulltext = "";
    for (j = 0; j < wordSet.length; j++) {
        fulltext = fulltext.concat(wordToLink(wordSet[j]) + " ");
    }
    $("#notebox").html(fulltext);
    setEndOfContenteditable($("#notebox").get(0));
    wordSet.push(new Word("", player.getCurrentTime()));
}