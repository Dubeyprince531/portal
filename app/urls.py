from django.urls import path,include
from . import views

urlpatterns = [
  path("",views.IndexPage,name="index"),
  path("about/",views.AboutPage,name="about"),
  path("job_listing/",views.JobPage,name="job_listing"),
  path("signup/",views.SignupPage,name="signup"),
  path("register/",views.RegisterUser,name="register"),
  path("otppage/",views.OTPPage,name="otppage"),
  path("login/",views.Login,name="login"),
  path("loginuser/",views.Loginuser,name="loginuser"),
  path("otp/",views.otp,name="otp"),
  path("blog/",views.Blog,name="blog"),
  path("job_details/",views.Job,name="job_detail"),
  path("elements/",views.Element,name="elements"),
  path("single-blog/",views.BlogDetail,name="single-blog"),
  path("contact/",views.Contact,name="contact"),
  path("profilepage/<int:pk>",views.Profilepage,name="profilepage"),
  path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
  
  
  
  
  ############################ company site #########################
  
  path("companyindex/",views.companyindexpage,name="companyindex"),
  path("companyprofile/<int:pk>",views.companyprofile,name="companyprofile"),
  path("updatecompanyprofile/<int:pk>",views.updatecompanyprofile,name="updatecompanyprofile"),
  path("jobpostpage/",views.jobpostpage,name="jobpostpage"),
  path("jobdetailsubmit/",views.jobdetailsubmit,name='jobdetailsubmit'),
  path("companylogout/",views.companylogout,name="companylogout"),
]



