from django.shortcuts import render
from app.models import *
from django.http import HttpResponse 
def insert_dept(request):
    deptno=int(input("Enter the Number:"))
    dname=input("Enter the name:")
    dloc=input("Enter the loc:")
    
    DO=Dept.objects.get_or_create(deptno=deptno,dname=dname,dloc=dloc)
    if DO[1]:
        return HttpResponse('Object is created successfully')
    else:
        return HttpResponse('Sorry it is already existed')

def insert_emp(request):
    empno=int(input('Enter empno: '))
    ename=input('Enter enmae: ')
    sal=int(input('Enter salary: '))
    hiredate=input('Enter Hiredate: ')
    job=input('Enter Job: ')
    comm=input('Enter comm: ')
    deptno=int(input('Enter deptno: '))
    mgr=input('Enter mgr: ')
    DPTO=Dept.objects.filter(deptno=deptno)
    mgvr=None
    if not mgr:
        mgvr=None
        EMPO=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,hiredate=hiredate,sal=sal,comm=comm,deptno=DPTO[0],mgr=mgvr)
    else:
        mgvr=Emp.objects.get(empno=mgr)    
        EMPO=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,hiredate=hiredate,sal=sal,comm=comm,deptno=DPTO[0],mgr=mgvr)
    d = {'Emp':Emp.objects.all()}
    return render(request,'empdept.html',d)
def empdept(request):
    EDO=Emp.objects.select_related('deptno').all()
    EDO=Emp.objects.select_related('deptno').filter(job='Software')
    EDO=Emp.objects.select_related('deptno').filter(deptno__dloc='Bengalore')
    EDO=Emp.objects.select_related('deptno').filter(sal=20000)
    d={'EDO':EDO}
    return render(request,'empdept1.html',d)


def empmgr(request):
    EMPO=Emp.objects.select_related('mgr').all()
    d={'EMPO':EMPO}
    return render(request,'empmgr.html',d)

def empmgrdept(request):
    EMDO=Emp.objects.select_related('deptno','mgr').all()
    EMDO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Yaho')
    EMDO=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt=10000)
    EMDO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Parvez')
    # EMDO=Emp.objects.select_related('deptno','mgr').filter(job='Enginer')
    EMDO=Emp.objects.select_related('deptno','mgr').filter(mgr__sal=100000)
    d={'EMDO':EMDO}
    return render(request,'empmgrdept.html',d)
def deptemp(request):
    DEO=Dept.objects.prefetch_related('emp_set').all()
    DEO=Dept.objects.prefetch_related('emp_set').filter(dname='Vasavi')
    DEO=Dept.objects.prefetch_related('emp_set').filter(dloc='Bengalore')
    d={'DEO':DEO}
    return render(request,'deptemp.html',d)

def display_emp(request):
    QSW=Emp.objects.all()
    d={'Emp':QSW}
    return render(request,'empdept.html',d)

def display_dept(request):
    QSW=Dept.objects.all()  
    d={'dept':QSW}
    return render(request,'display_dept.html',d)
