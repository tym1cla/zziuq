from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm
from .models import *
import random
from login.models import Profile


@login_required
def categories(request):
    return render(request, 'categories.html')


@login_required
def quiz_geography(request):
    title = 'Geography'
    # get user
    current_user = Profile.objects.get(user=request.user)
    # get user available questions
    user_questions_list = current_user.geography.all()
    # get all not used questions
    questions_list = Geography.objects.all().exclude(id__in=user_questions_list)
    available_questions_number = len(questions_list)

    if len(questions_list) > 0:
        # get random question
        index = random.randrange(len(questions_list))
        question = questions_list[index]
    else:
        question = ''

    if request.method == 'POST':
        answer = request.POST.get('answer')
        if isinstance(question, str):
            current_user.geography.add(question)
            pass
        else:
            # collect score
            if int(answer) == question.correct_answer:
                current_user.score += 1

            current_user.geography.add(question)
            current_user.save()

        return render(request, 'quiz.html', locals())
    return render(request, 'quiz.html', locals())


@login_required
def quiz_entertainment(request):
    title = 'Entertainment'
    # get user
    current_user = Profile.objects.get(user=request.user)
    # get user available questions
    user_questions_list = current_user.entertainment.all()
    # get all not used questions
    questions_list = Entertainment.objects.all().exclude(id__in=user_questions_list)
    available_questions_number = len(questions_list)

    if len(questions_list) > 0:
        # get random question
        index = random.randrange(len(questions_list))
        question = questions_list[index]
    else:
        question = ''

    if request.method == 'POST':
        answer = request.POST.get('answer')
        if isinstance(question, str):
            pass
        else:
            # collect score
            if int(answer) == question.correct_answer:
                current_user.score += 1

            current_user.entertainment.add(question)
            current_user.save()

        return render(request, 'quiz.html', locals())
    return render(request, 'quiz.html', locals())


@login_required
def quiz_history(request):
    title = 'History'
    # get user
    current_user = Profile.objects.get(user=request.user)
    # get user available questions
    user_questions_list = current_user.history.all()
    # get all not used questions
    questions_list = History.objects.all().exclude(id__in=user_questions_list)
    available_questions_number = len(questions_list)

    if len(questions_list) > 0:
        # get random question
        index = random.randrange(len(questions_list))
        question = questions_list[index]
    else:
        question = ''

    if request.method == 'POST':
        answer = request.POST.get('answer')
        if isinstance(question, str):
            pass
        else:
            # collect score
            if int(answer) == question.correct_answer:
                current_user.score += 1

            current_user.history.add(question)
            current_user.save()

        return render(request, 'quiz.html', locals())
    return render(request, 'quiz.html', locals())


@login_required
def quiz_literature(request):
    title = 'Literature'
    # get user
    current_user = Profile.objects.get(user=request.user)
    # get user available questions
    user_questions_list = current_user.literature.all()
    # get all not used questions
    questions_list = Literature.objects.all().exclude(id__in=user_questions_list)
    available_questions_number = len(questions_list)

    if len(questions_list) > 0:
        # get random question
        index = random.randrange(len(questions_list))
        question = questions_list[index]
    else:
        question = ''

    if request.method == 'POST':
        answer = request.POST.get('answer')
        if isinstance(question, str):
            pass
        else:
            # collect score
            if int(answer) == question.correct_answer:
                current_user.score += 1

            current_user.literature.add(question)
            current_user.save()

        return render(request, 'quiz.html', locals())
    return render(request, 'quiz.html', locals())


@login_required
def quiz_science(request):
    title = 'Science'
    # get user
    current_user = Profile.objects.get(user=request.user)
    # get user available questions
    user_questions_list = current_user.science.all()
    # get all not used questions
    questions_list = Science.objects.all().exclude(id__in=user_questions_list)
    available_questions_number = len(questions_list)

    if len(questions_list) > 0:
        # get random question
        index = random.randrange(len(questions_list))
        question = questions_list[index]
    else:
        question = ''

    if request.method == 'POST':
        answer = request.POST.get('answer')
        if isinstance(question, str):
            pass
        else:
            # collect score
            if int(answer) == question.correct_answer:
                current_user.score += 1

            current_user.science.add(question)
            current_user.save()

        return render(request, 'quiz.html', locals())
    return render(request, 'quiz.html', locals())


@login_required
def quiz_sport(request):
    title = 'Sport'
    # get user
    current_user = Profile.objects.get(user=request.user)
    # get user available questions
    user_questions_list = current_user.sport.all()
    # get all not used questions
    questions_list = Sport.objects.all().exclude(id__in=user_questions_list)
    available_questions_number = len(questions_list)

    if len(questions_list) > 0:
        # get random question
        index = random.randrange(len(questions_list))
        question = questions_list[index]
    else:
        question = ''

    if request.method == 'POST':
        answer = request.POST.get('answer')
        if isinstance(question, str):
            pass
        else:
            # collect score
            if int(answer) == question.correct_answer:
                current_user.score += 1

            current_user.sport.add(question)
            current_user.save()

        return render(request, 'quiz.html', locals())
    return render(request, 'quiz.html', locals())


@login_required
def questions(request):
    form = QuestionForm()

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            # get posted data
            category = form.cleaned_data['category']
            question = form.cleaned_data['question']
            answer_1 = form.cleaned_data['answer_1']
            answer_2 = form.cleaned_data['answer_2']
            answer_3 = form.cleaned_data['answer_3']
            answer_4 = form.cleaned_data['answer_4']
            correct_answer = form.cleaned_data['correct_answer']

            # save data
            if category == 'Geography':
                question = Geography(question=question, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4, correct_answer=correct_answer)
                question.save()

            if category == 'Entertainment':
                question = Entertainment(question=question, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4, correct_answer=correct_answer)
                question.save()

            if category == 'History':
                question = History(question=question, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4, correct_answer=correct_answer)
                question.save()

            if category == 'Literature':
                question = Literature(question=question, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4, correct_answer=correct_answer)
                question.save()

            if category == 'Science':
                question = Science(question=question, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4, correct_answer=correct_answer)
                question.save()

            if category == 'Sport':
                question = Sport(question=question, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4, correct_answer=correct_answer)
                question.save()

            return render(request, 'questions.html', locals())
        else:
            return render(request, 'questions.html', locals())

    return render(request, 'questions.html', locals())
