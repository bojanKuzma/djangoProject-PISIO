from django.forms import ModelForm
from forum.models import Question, Answer


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ("title", "description")

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].required = False


    def save(self, commit=True):
        question = super(QuestionForm, self).save(commit=False)
        question.original_poster = self.instance.user
        if commit:
            question.save()
        return question


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ("answer",)

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        answer = super(AnswerForm, self).save(commit=False)
        answer.question.id = self.instance.question_id
        answer.author = self.instance.author
        if commit:
            answer.save()
        return answer
