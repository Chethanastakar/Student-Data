from django.shortcuts import render
from percentageapp.models import Student4
# Create your views here.
def input(request):
    return render(request,'base.html')
def input2(request):
    sid=int(request.GET['t1'])
    sname=request.GET['t2']
    sbranch=request.GET['t3']
    telugu=int(request.GET['t4'])
    hindi = int(request.GET['t5'])
    english = int(request.GET['t6'])
    mathes = int(request.GET['t7'])
    science = int(request.GET['t8'])
    social = int(request.GET['t9'])
    if(telugu<35 and hindi<35 and english<35 and mathes<35 and science<35 and social<35):
        result='PASS'
    total=telugu+hindi+english+mathes+science+social
    sperc=total/600*100
    if sperc>90:
        result=' GOT FIRST RANK IN THE COLLEGE'
    elif sperc>80:
        result='GOT SECOND RANK IN THE COLLEGE'
    elif sperc>70:
        result='GOT THIRD RANK IN THE COLLEGE'
    elif sperc<=70:
        result=' WITH AVEREAGE MARKS'
    else:
        result='FAIL'
    recs=Student4(sid=sid,sname=sname,sbranch=sbranch,
                  telugu=telugu,hindi=hindi,english=english,
                  mathes=mathes,science=science,social=social,
                  total=total,sperc=sperc,result=result)
    recs.save()
    raju=Student4.objects.all()
    return render(request,'base2.html',{'raj':raju})
