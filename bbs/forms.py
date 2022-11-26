from django import forms
from .models import Topic




#hours minutes secondsを受け取り、timeを返す
class TimeForm(forms.Form):

    hours       = forms.IntegerField()
    minutes     = forms.IntegerField()
    seconds     = forms.IntegerField()
    
    def clean(self):
        data            = self.cleaned_data
        data["time"]    = data["hours"]*3600 + data["minutes"]*60 + data["seconds"]
        return data


class TopicForm(forms.ModelForm):

    class Meta:
        model   = Topic
        fields  = ["comment","time"]



