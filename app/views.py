from django.shortcuts import render , redirect
from .models import *
from random import randint
# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")

def SignupPage(request):
    return render(request,"app/signup.html")

def RegisterUser(request):
    if request.POST['role']=="candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        user = UserMaster.objects.filter(email=email)
        
        if user:
            context = {'message' : 'User already exists' , 'class' : 'danger' }
            return render(request,'app/signup.html' , context)
        else:
            if password == cpassword:
                otp = randint(0,1000)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
    else:
        if request.POST['role']=="company":
            role = request.POST['role']
            fname = request.POST['firstname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            
            user = UserMaster.objects.filter(email=email)
            
            if user:
                context = {'message' : 'User already exists' , 'class' : 'danger' }
                return render(request,'app/signup.html' , context)
            else:
                if password == cpassword:
                    otp = randint(0,1000)
                    newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    newcand = company.objects.create(user_id=newuser,firstname=fname,)
                    return render(request,"app/otpverify.html",{'email':email})
        
            
    


def Login(request):
    return render(request,"app/login.html")
        
def Loginuser(request):
    if request.POST['role']=="candidate":
        email = request.POST['email']
        password = request.POST['password']
        
        
        user = UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="candidate":
                can = candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname      
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('index')
            else:
                context = {'message' : 'password incorrect' , 'class' : 'danger' }
                return render(request,"app/login.html" , context)
        else:
            context = {'message' : 'User Not found' , 'class' : 'danger' }
            return render(request,"app/login.html" , context)
        
    if request.POST['role']=="company":
        email = request.POST['email']
        password = request.POST['password']
        
        
        user = UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="company":
                can = company.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname     
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('companyindex')
            else:
                context = {'message' : 'password incorrect' , 'class' : 'danger' }
                return render(request,"app/login.html" , context)
        else:
            context = {'message' : 'User Not found' , 'class' : 'danger' }
            return render(request,"app/login.html" , context)

def OTPPage(request):
    return render(request,"app/otpverify.html")

def otp(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
    
    user = UserMaster.objects.get(email=email)
    
    if user:
        if user.otp == otp:
            context = {'message' : 'OTP verify successfully' , 'class' : 'success' }
            return render(request,'app/login.html' , context)
        else:
            context = {'message' : 'OTP Not match' , 'class' : 'danger' }
            return render(request,'app/otpverify.html' , context)
    else:
        return render(request,"app/signup.html")
    


def AboutPage(request):
    return render(request,"app/about.html")

def JobPage(request):
    return render(request,"app/job_listing.html")

def Blog(request):
    return render(request,"app/blog.html")

def Job(request):
    return render(request,"app/job_details.html")

def Element(request):
    return render(request,"app/elements.html")


def BlogDetail(request):
    return render(request,"app/single-blog.html")

def Contact(request):
    return render(request,"app/contact.html")


def Profilepage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = candidate.objects.get(user_id=user)    
    return render(request,"app/profile.html",{'user':user,'can':can})

def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "candidate":
        can = candidate.objects.get(user_id=user)
        can.contact = request.POST['contact']
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.gender = request.POST['gender']
        can.dob = request.POST['dob']
        can.address = request.POST['address']
        can.save()
        url = f'/profilepage/{pk}'
        return redirect(url)
    
    


#######################  company site  #######################

def companyindexpage(request):
    return render(request,"app/company/index.html")

def companyprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = company.objects.get(user_id=user)
    return render(request,"app/company/profile.html",{'user':user,"comp":comp})


def updatecompanyprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "company":
        comp = company.objects.get(user_id=user)
        comp.firstname = request.POST['firstname']
        comp.companyname = request.POST['companyname']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.contact = request.POST['contact']
        comp.address = request.POST['address']
        comp.email = request.POST['email']
        comp.save()
        url = f"/companyprofile/{pk}"
        return redirect(url)


def jobpostpage(request):
    return render(request,"app/company/jobpost.html")

def jobdetailsubmit(request):
    user = UserMaster.objects.get(id=request.session.get('id'))
    if user.role == "company":
        comp = company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress = request.POST['companyaddress']
        jobndescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        joblocation = request.POST['joblocation']       
        companywebsite = request.POST['companywebsite']
        companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        salarypackage = request.POST['salarypackage']
        experience = request.POST['experience']
        user = JobDetail.objects.create(jobname=jobname,companyname=companyname,companyaddress=companyaddress,
                                           jobndescription=jobndescription,qualification=qualification,responsibilities=responsibilities,
                                           joblocation=joblocation,
                                           companywebsite=companywebsite,
                                           companyemail=companyemail,companycontact=companycontact,salarypackage=salarypackage,experience=experience)
        context = {'message' : 'job posted success' , 'class' : 'success'}
        return redirect('jobpostpage',context)




def companylogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')



##### https://github.com/Dubeyprince531/portal ####
