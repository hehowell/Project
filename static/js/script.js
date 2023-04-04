
/* javascript */


function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    if (color == "#FFFFFF") {
        for (var i = 0; i < 6; i++ ) {
            color += letters[Math.floor(Math.random() * 16)];
        }
    } else {
        return color;}
}


function makebox(titleList) {
    console.log(titleList);
    for (var i = 0; i < titleList.length; i++) {
        var element = document.getElementById(titleList[i].replace(' ', '_'));
        console.log(element);
        if (element) {
            var top=Math.random();
            top=top*300;
            var left=Math.random();
            left=left*1000;
            element.style.top=top+"px";
            element.style.left=left+"px";
            element.style.backgroundColor=getRandomColor();
            element.style.display="block";
        }
    }
    
}

