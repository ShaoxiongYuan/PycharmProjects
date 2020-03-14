function getRandom(max, len, zero, top) {
    var _arr = []
    while (_arr.length < len) {
        console.log(_arr.length)
        if (!top) {
            var n = Math.floor(Math.random * max)
        } else {
            var n = Math.ceil(Math.random * max)
        }

        if (n < 10 && zero) {
            n = '0' + n
        }

        var reg = new RegExp(n, 'g')
        if (!reg.test(_arr.toString())) {
            _arr.push(n)
        }
    }
    return _arr
}

var btnChange = document.getElementById('btnChange')
btnChange.onclick = function () {
    var lists = document.getElementsByTagName('li')
    var arr = getRandom(32, 6, true, true)
    for (var i = 0; i < lists.length - 1; i++) {
        lists[i].innerText = arr[i]
    }
}