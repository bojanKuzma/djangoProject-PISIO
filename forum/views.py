from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from forum.forms import QuestionForm, AnswerForm
from forum.models import Question, Answer


class HomeView(LoginRequiredMixin, ListView):
    template_name = "forum/home.html"
    model = Question
    context_object_name = "question_list"
    paginate_by = 10
    queryset = Question.objects.all().order_by('-time_asked')

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)

    def get_queryset(self):
        queryset = self.queryset
        search = self.request.GET.get('search', None)
        if search is not None:
            queryset = queryset.filter(title__contains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', None)
        return context


class MyQuestionsView(HomeView):
    template_name = "forum/my_questions.html"

    def get_queryset(self):
        queryset = super(MyQuestionsView, self).get_queryset()
        queryset = queryset.filter(original_poster=self.request.user)
        return queryset


class CreateQuestionView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'forum/create_question.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DetailQuestionView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'forum/question_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailQuestionView, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(question_id=context['question'].id)
        context['form'] = AnswerForm()
        return context


class CreateAnswerView(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerForm

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['question_id']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('question_detail', kwargs={'pk': self.object.question.id})


class DeleteQuestionView(LoginRequiredMixin, DeleteView):
    model = Question
    context_object_name = 'task'
    success_url = reverse_lazy('my_questions')

    def get_queryset(self):
        queryset = super(DeleteQuestionView, self).get_queryset()
        queryset = queryset.filter(original_poster=self.request.user, pk=self.kwargs['pk'])
        return queryset


