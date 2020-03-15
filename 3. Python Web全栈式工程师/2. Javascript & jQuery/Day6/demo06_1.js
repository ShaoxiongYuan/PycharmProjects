var m = prompt('请输入月份：')
switch (m) {
    case '1':
    case '3':
    case '5':
    case '7':
    case '8':
    case '10':
    case '12':
        alert('31')
        break;
    case '4':
    case '6':
    case '9':
    case '11':
        alert('30')
        break
    case '2':
        alert('28')
        break
    default:
        alert('匹配失败')
        break;
}