$('#btn').on('click', function () {
    var xhr = new XMLHttpRequest()
    xhr.open('GET', '/exer_server?uname=' + $('#uname').val(), true)
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            $('#show').html(xhr.responseText)
        }
    }
    xhr.send(null)
})