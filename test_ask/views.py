from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from test_ask.forms import ContactForm
from test_ask.models import WinQuestion, WinAnswer


def index(request):
    result = render_to_response('templates/index.html', {'data': '', 'admin': 'zhangsan'})
    return result


def eysenck_index(request):
    '''
    艾森克人格问卷首页
    :param request:
    :return:
    '''
    questions = WinQuestion.objects.filter(question_lib_id=1).values('question_id', 'question_order',
                                                                     'question_content').order_by('question_order')
    c = csrf(request)
    c.update({'questions': questions})
    print(456)
    return render_to_response('templates/eysenck_index.html', c)


def eysenck_save(request):
    '''
    艾森克人格问卷保存
    :param request:
    :return:
    '''
    qustion_options = request.POST.dict()
    qustion_options.pop('csrfmiddlewaretoken')
    answers = []
    for k, v in qustion_options.items():
        answers.append(WinAnswer(question_id=k, option_value=v, stu_id=15))
    WinAnswer.objects.bulk_create(answers)
    return HttpResponseRedirect('success')


def eysenck_success(request):
    '''
    成功页面
    :param request:
    :return:
    '''
    return render_to_response('templates/success.html')

