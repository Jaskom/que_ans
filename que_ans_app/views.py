# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.template import loader,Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from que_ans_app.models import Question
from que_ans_app.models import Answer
from que_ans_app.models import User
from django.core.paginator import Paginator,InvalidPage,EmptyPage
import datetime

@csrf_exempt
def addQuestion(request):
    errors=[] 
    que_owner=request.POST.get('owner')
    que_description=request.POST.get('des')
    if not que_owner:
            errors.append('the Publisher is required')
    if not que_description:
            errors.append('the Question is required')
    if not errors:
        que_publish_time=(datetime.datetime.now().strftime("%Y-%m-%d"))
        question=Question(que_owner=que_owner,que_description=que_description,que_publish_time=que_publish_time)
        question.save()
        return HttpResponseRedirect("/list/")
    else:
        return render_to_response('addQuestion.html',{'errors':errors})
        
           
def listQuestions(request):
    que_list=Question.objects.all()
    paginator = Paginator(que_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        questions = paginator.page(page)
    except (EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)
    t=loader.get_template("listQuestions.html")
    c=Context({'questions':questions})
    return HttpResponse(t.render(c))

def queryById(request):
    offset=request.GET.get('id')
   # print offset
    question=Question.objects.get(id=offset)
    #print question.id
    ans_list=Answer.objects.filter(question_id=offset)

    paginator = Paginator(ans_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        answers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        answers = paginator.page(paginator.num_pages)

    t=loader.get_template("ans_que.html")
    #c=Context({'question':question})
    c=Context({'question':question,'answers':answers})
    return HttpResponse(t.render(c))

@csrf_exempt
def saveAanswer(request):
    """

    :param request:
    :return:
    """
    errors=[]
    ans_description=request.POST.get("ans_description")
    question_id=request.POST.get("question_id")
    if not ans_description:
            errors.append('the Answer is required')
    print question_id
    ans_publish_time=(datetime.datetime.now().strftime("%Y-%m-%d"))
    answer=Answer(ans_description=ans_description,ans_publish_time=ans_publish_time,question_id=question_id)
    answer.save()
    return HttpResponseRedirect("/query/?id="+question_id)


def register(request):
    errors = []
    user_email = request.POST.get('email')
    user_password = request.POST.get('password')
    if not user_email:
        errors.append("user_email is required")
    if not user_password:
        errors.append("user_password  is required")
    if not errors:
        user=User(user_email=user_email,user_password=user_password)
        user.save();
    return


def login(request):
     errors = []
     user_email = request.POST.get('email')
     user_password = request.POST.get('password')
     if not user_email:
        errors.append("user_email is required")
     if not user_password:
        errors.append("user_password  is required")
     if not errors:
        user=User(user_email=user_email,user_password=user_password)
        user.save();


def preregister(request):
    return render_to_response("register.html")


def index(request):
    """

    :param request:
    :return:
    """
    return render_to_response("index.html")



