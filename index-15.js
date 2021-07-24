function shuffle(array) {
    var currentIndex = array.length, randomIndex;

    while (0 !== currentIndex) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }

    return array;
}

var index = 4;
var randomSeed = '1062155580';
Math.seedrandom(randomSeed);

var choosenerOptions = shuffle([
    "Drew",
    "Jeff",
    "Matt",
    "Mike"
]);

var foodOptions = shuffle([
    "Ezells",
    "Arbys",
    "Five Guys",
    "Mod Pizza",
    "Wibbleys"
]);

window.onload = init;

function init() {
    if (index == choosenerOptions.length) {
        document.getElementById("choosener").innerHTML = "Y'ALL GOIN TO MOX!";
    } else {
        document.getElementById("choosener").innerHTML = "Choosener: " + choosenerOptions[index];
        document.getElementById("food").innerHTML = "Food: " + foodOptions[index];
    }

}
