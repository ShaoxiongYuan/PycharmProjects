$('#btn').on('click', function () {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/exer2_server?uname=' + $('#uname').val(), true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            if (xhr.responseText === '0') {
                $('#msg').html('用户名重复').css('color', 'red')
            } else if (xhr.responseText === '1') {
                $('#msg').html('OK').css('color', 'green')
            }
        }
    };
    xhr.send(null)
});