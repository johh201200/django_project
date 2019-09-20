from django.shortcuts import render, redirect
from .models import Question, Answer
from django.db.models import Count

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {'questions': questions,}
    return render(request, 'eithers/index.html', context)


def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        issue_a = request.POST.get('issue_a')
        issue_b = request.POST.get('issue_b')
        image_a = request.FILES.get('image_a')
        image_b = request.FILES.get('image_b')
        question = Question(title=title, issue_a=issue_a, issue_b=issue_b, image_a=image_a, image_b=image_b)
        question.save()
        return redirect(index)
    else:
        return render(request, 'eithers/create.html')


def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    answers = question.answer_set.all()
    left = len(question.answer_set.filter(pick=1))
    right = len(question.answer_set.filter(pick=2))
    per_left = (left / (left+right)) * 100
    per_right = 100 - per_left
    context = {'question': question, 'answers':answers, 'per_left':per_left, 'per_right':per_right}
    return render(request, 'eithers/detail.html', context)


def answers_create(request, question_pk):
    question = Question.objects.get(pk=question_pk)    
    if request.method == 'POST':
        pick = request.POST.get('pick')
        comment = request.POST.get('comment')
        answer = Answer(question=question, pick=pick, comment=comment)
        answer.save()
        return redirect('eithers:detail', question_pk)
    else:
        return redirect('eithers:detail', question_pk)


def answers_delete(request, question_pk, answer_pk):
    answer = Answer.objects.get(pk=question_pk)
    if request.method == 'POST':
        answer.delete()
    return redirect('eithers:detail', answer_pk)
