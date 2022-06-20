import mimetypes,os
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import employee,rem,leave,att
from django.contrib import messages
from datetime import date, datetime
from fpdf import FPDF
import pandas
from datetime import date, timedelta

today = date.today()

def genpdf(f,t):
    f=datetime.strptime(f, '%Y-%m-%d')
    t=datetime.strptime(t, '%Y-%m-%d')
    dr=pandas.date_range(f,t-timedelta(days=1),freq='d')
    for d in dr:
        print(d)
    pdf = FPDF()
    # Add a page
    pdf.add_page()
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    # create a cell
    pdf.cell(200, 10, txt = "GeeksforGeeks",ln = 1, align = 'C')
    # add another cell
    pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",ln = 2, align = 'C')
    # save the pdf with name .pdf
    pdf.output("GFG.pdf")  

def handellogin(request):
    flag=0
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']   
        emp=employee.objects.values_list('username','password','role','id','reportingmanager')
        for e in emp:
            if e[0]==username:
                if e[1]==password:
                    global role,user,id,rm
                    role=e[2]
                    user=e[0]
                    id=e[3]
                    rm=e[4]
                    flag=1
                    return redirect('index') 
        if flag==0:
            messages.error(request,"Invalid Credentials, Please try again")                    
    return render(request,'omnidash/login.html')  

def remb(request):
    re=rem.objects.all()
    em=employee.objects.all()
    tempn=temp['name']
    tempid=temp['id']
    if request.method=='POST': 
        if 'file' in request.FILES:
            file2=request.FILES["file"]
            df=request.POST['minad']
            l=request.POST['loc']
            c=request.POST['cato']
            pn=request.POST['Proj']
            v=request.POST['val']
            ad=request.POST['adv']
            m=request.POST['mof']
            di=request.POST['dis']
            data=rem.objects.create(username_id=temp['id'],file=file2,reportingmanager=rm,dadded=df,dis=di,value=v,loc=l,cat=c,pname=pn,adv=ad,mof=m)
            data.save()
            return HttpResponse("upload ok")
        if 'abox' in request.POST or 'rbox' in request.POST or 'pay' in request.POST :
            abox=request.POST.getlist('abox')
            rbox=request.POST.getlist('rbox')
            pay=request.POST.getlist('pay')
            for a in abox:
                rem.objects.filter(pk=int(a)).update(approve=True)
            for r in rbox:     
                rem.objects.filter(pk=int(r)).update(reject=True) 
            for p in pay:
                rem.objects.filter(pk=int(p)).update(pay=True)    
            for a in abox:
                for r in rbox:
                    if a==r:
                        rem.objects.filter(pk=int(r)).update(approve=False)
                        rem.objects.filter(pk=int(r)).update(reject=False) 
                        messages.error(request,"Invalid Credentials, Please try again") 
                        return redirect('rem')
    return render(request,'omnidash/remb.html',{'re':re,'em':em,'tempn':tempn,'role':role,'tempid':tempid,'today':today})

def leaves(request):
    lea=leave.objects.all()
    em=employee.objects.all()
    tempn=temp['name']
    if request.method=='POST': 
        if 'body' in request.POST:
            body=request.POST["body"]
            df=request.POST['minad']
            dt=request.POST['maxad']
            data=leave.objects.create(username_id=temp['id'],reason=body,reportingmanager=rm,dfrom=df,dto=dt)
            data.save()
            return HttpResponse("upload ok") 
        if 'abox' in request.POST or 'rbox' in request.POST:
            abox=request.POST.getlist('abox')
            rbox=request.POST.getlist('rbox')
            for a in abox:
                leave.objects.filter(pk=int(a)).update(approve=True)
            for r in rbox:     
                leave.objects.filter(pk=int(r)).update(reject=True)        
            for a in abox:
                for r in rbox:
                    if a==r:
                        leave.objects.filter(pk=int(a)).update(approve=False)
                        leave.objects.filter(pk=int(r)).update(reject=False)
                        messages.error(request,"Invalid Credentials, Please try again") 
                        return redirect('leave') 
    return render(request,'omnidash/leave.html',{'lea':lea,'em':em,'tempn':tempn,'role':role,})  
    
def atten(request):
    em=employee.objects.all()
    at=att.objects.all()
    tempn=temp['name']
    return render(request,'omnidash/att.html',{'em':em,'at':at,'tempn':tempn,'role':role,})

def req(request):
    if request.method=='POST':
        if 'lfrom' in request.POST:
            lf=request.POST['lfrom']
            lt=request.POST['lto']
        elif 'afrom' in request.POST:
            af=request.POST['afrom']
            at=request.POST['ato']        
        elif 'rfrom' in request.POST:
            rf=request.POST['rfrom']
            rt=request.POST['rto']
            genpdf(rf,rt)
    return render(request,'omnidash/req.html',{'temp':temp})

def download_pdf_file(filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    # Define the full file path
    filepath = BASE_DIR +'\\'+ filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    os.remove(filename)
    return response
        
def index(request):
    emp=employee.objects.values()
    em=employee.objects.all()
    le=leave.objects.all()
    for e in emp:
        if e['id']==id:
            global temp
            temp=e        
            if request.method == 'POST':
                stat = request.POST['status']
                employee.objects.filter(pk=id).update(status=stat)
    return render(request,'omnidash/index.html',{'temp':temp,'em':em,'le':le,'user':user,'role':role,'today':today})

def logout(request):
    global temp,id
    temp={'name':'','id':0}
    id=0
    print(temp)
    return redirect('handellogin')    