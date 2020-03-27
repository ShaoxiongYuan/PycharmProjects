from django.shortcuts import render


def test(request):
    dict1 = {
        "username": "steven",
        "age": 18
    }
    return render(request, 'test.html', dict1)
