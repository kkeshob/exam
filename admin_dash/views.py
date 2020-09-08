from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Questions,Answer,Course,Paper
from.forms import AddQFrm
from accounts.models import User
from io import BytesIO
from . import generate_result
from reportlab.pdfgen import canvas
from django.contrib.admin.views.decorators import staff_member_required
@staff_member_required
def exam_admin_home(request):
    return render(request,'exam_admin_home.html')
@staff_member_required
def new_question(request):
    msg=""
    if request.method=="POST":
        frm=AddQFrm(request.POST or None)
        if frm.is_valid():
            a=frm.save()
            if a:
                msg="Question Added Successfully"
    frm=AddQFrm()
    context={
        'frm':frm,
        'msg':msg,
    }
    return render(request,'add_question.html',context)

@staff_member_required
def view_question(request):
    qts=Questions.objects.all()
    context={
        'qts':qts,
    }
    return render(request,'view_questions.html',context)
@staff_member_required
def edit_questions(request,qid):
    qi=Questions.objects.get(id=qid)
    if request.method=='POST':
        frm=AddQFrm(request.POST,instance=qi)
        if frm.is_valid():
            frm.save()
            return redirect('view_question')
    frm=AddQFrm(instance=qi)
    context={
        'frm':frm,
    }
    return render(request,'add_question.html',context)
@staff_member_required
def delete_questions(request,qid):
    Questions.objects.filter(id=qid).delete()
    return redirect('view_question')
@staff_member_required
def students(request):
    students=User.objects.filter(is_staff=False,is_admin=False)
    context={
        'stds':students
    }
    return render(request,'student_list.html',context)
@staff_member_required
def answerd_questions(request,stdid):
    ans=Answer.objects.filter(student=stdid)
    context={
        'ans':ans
    }
    return render(request,'answers.html',context)

@staff_member_required
def result(request,stdid):
    course=Course.objects.all()
    paper=Paper.objects.all()
    qts=Answer.objects.filter(student=stdid)
   
    exam=[]
    i=0
    m=0
    for c in course:
        
        for p in paper:
            ex={}
            q=qts.filter(question__course=c.id,question__paper=p.id)
            an=[]
            for a in q:
                if a.answer==a.question.answers:
                    m=m+1
            if q:
                ex['total_marks']=30
                ex['marks']=m
                ex['answers']=q
                ex['course']=c.course
                ex['paper']=p.paper
                exam.append(ex)
               
            m=0
            i=i+1


    context={
        'exams':exam,
        
    }
    return render(request,'result.html',context)
@staff_member_required
def view_results(request):
    paper=Paper.objects.all()
    students=User.objects.filter(is_staff=False,is_admin=False)
    data=[]
    for student in students:
        std={}
        exams=Answer.objects.filter(student=student)
        std['student']=student
        pp=[]
        for p in paper:
            m=0
            for q in exams:
                if q.question.paper==p and q.answer==q.question.answers:
                    m=m+1
            pp.append(m)
            std['paper']=pp
        data.append(std)
    context={
        'datas':data

    }
    return render(request,'view_results.html',context)

def printresult(data,date):
    buffer = BytesIO()
    pdf=canvas.Canvas(buffer)
    generate_result.design(pdf,str(date))
    generate_result.results(pdf,data)

    pdf.showPage()
    pdf.save()
    pdf_buffer = buffer.getvalue()
    buffer.close()
    return pdf_buffer
@staff_member_required
def generate(request):
    msg=""
    if request.method=='POST':
        date=request.POST['date']
        qst=Answer.objects.filter(date__date=date)
        if qst:
            paper=Paper.objects.all()
            students=User.objects.filter(is_staff=False,is_admin=False)
            

            std=[]
            for s in students:
                for q in qst:
                    if q.student==s and s not in std:
                        std.append(s)
            print(std)


            data=[]
            for student in std:
                std={}
                exams=qst.filter(student=student)
                std['student']=student
                pp=[]
                for p in paper:
                    m=0
                    for q in exams:
                        if q.question.paper==p and q.answer==q.question.answers:
                            m=m+1
                    pp.append(m)
                    std['paper']=pp
                data.append(std)
            pdf=printresult(data,date)
            return HttpResponse(pdf, content_type='application/pdf')
        else:
            msg="No Exam Found On that Date"

    context={
        'msg':msg,
    }
    return render(request,'generate_report.html',context)

