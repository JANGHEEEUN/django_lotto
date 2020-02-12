from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.forms import PostForm

# Create your views here.
def index(request):
    #site_1\lotto\templates\lotto\default.htm
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html',{'lottos':lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def post(request):
    print("********")
    print(request.method)
    print("********")

    if request.method == "POST":
        form = PostForm(request.POST) #양식에 사용자가제출한데이터 넣음.

        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
            # github에서의 commit에 해당~!

    else: #GET 요청일 때
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})


    form = PostForm()
    return render(request, "lotto/form.html", {"form":form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})
