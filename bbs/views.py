from django.shortcuts import render,redirect

from django.views import View
from .models import Topic
from .forms import TopicForm,TimeForm


class IndexView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["topics"]   = Topic.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        copied  = request.POST.copy()

        #timeの指定が無い時、hours minutes secondsを計算してtimeを作る。
        if "time" not in copied:
            form    = TimeForm(copied)
            if form.is_valid():
                cleaned         = form.clean()
                copied["time"]  = cleaned["time"]


        #ここで保存
        form    = TopicForm(copied)
        if form.is_valid():
            print("保存")
            form.save()

        return redirect("bbs:index")

index   = IndexView.as_view()
