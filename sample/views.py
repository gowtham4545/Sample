from django.shortcuts import render


def homepage(request):
    b={1:'one',2:'two',3:'three'}
    a={'heading':'hi','b':b}
    a.update(b)
    print(a)
    return render(request,'home.html',a)
    pass