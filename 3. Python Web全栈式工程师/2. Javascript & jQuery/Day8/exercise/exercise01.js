timer = setInterval(left, 1000)

function left() {
    for (i = 0; i < img.length; i++) {
        if (img[i].id != '') {
            img[i].id = ''
            if (i != 0) {
                img[i - 1].id = 'first'
                return
            } else {
                img[4].id = 'first'
                return
            }
        }
    }
}

function right() {
    for (i = img.length - 1; i >= 0; i--) {
        if (img[i].id != '') {
            img[i].id = ''
            if (i != 4) {
                console.log(i)
                img[i + 1].id = 'first'
                return
            } else {
                img[0].id = 'first'
                return
            }
        }
    }
}

var d1 = document.getElementById('d1');
var img = document.getElementsByClassName('image');
var i1 = document.getElementById('i1')
var i2 = document.getElementById('i2')

i1.onclick = function () {
    left()
}
i2.onclick = function () {
    right()
}
i1.onmouseout = function () {
    timer = setInterval(left, 1000)
}
i2.onmouseout = function () {
    timer = setInterval(left, 1000)
}
d1.onmouseout = function () {
    timer = setInterval(left, 1000)
}
i1.onmouseover = function () {
    clearInterval(timer)
}
i2.onmouseover = function () {
    clearInterval(timer)
}
d1.onmouseover = function () {
    clearInterval(timer)
}