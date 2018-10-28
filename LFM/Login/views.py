from django.shortcuts import render
from LFM.models import userInfo, passage,replies
# -*-coding:utf-8-*-
# Create your views here.


def loginPage(request):
    return render(request, "homePage.html")

def login(request):
    userName = request.POST.get("userName")
    password = request.POST.get("password")
    result = ""
    if userName != "" and password != "":
        if request.POST.get("Login"):
            for temp in userInfo:
                if userName == temp["name"] and password == temp["pwd"]:
                    result = "Success"
                    return render(request, "userPage.html", {"name": userName,"info":userInfo,"result":result})
            result = "Fail,user not exist or pwd is error"
            return render(request, "homePage.html", {"result":result,"userName":userName})
    else:
        result = "Fail"
        return render(request, "homePage.html", {"result":result})

def register(request):
    userName = request.POST.get("userName")
    password = request.POST.get("password")
    confirmPassword = request.POST.get("confirmPassword")
    answer = request.POST.get("answer")
    result = ""
    if userName != "" and password != "" and answer != "":
        if request.POST.get("register"):
            if len(userName) > 3 and len(userName) < 20:
                if len(password) >6 and len(password) < 20:
                    if password != confirmPassword:
                        result = "Password inconsistent"
                        return render(request,"register.html",{"result":result})
                    else:
                        for temp in userInfo:
                            if temp["name"] == userName:
                                result = "user already exists"
                                return render(request,"register.html",{"result":result})
                        dic = {"name": userName, "pwd": password, "answer": answer}
                        userInfo.append(dic)
                        result = "Success"
                        return render(request, "register.html", {"result":result})
                else:
                    result = "The length of the password is between 6 and 20"
                    return render(request,"register.html",{"result":result})
            else:
                result = "The length of user name is between 3 and 20"
                return render(request,"register.html",{"result":result})

        else:
            return render(request,"register.html",{"result":result})

def retrievePassword(request):
    userName = request.POST.get("userName")
    answer = request.POST.get("answer")
    result = ""
    if userName != "" and answer != "":
        if request.POST.get("retrievePassword"):
            for i in userInfo:
                if userName == i["name"]:
                    for temp in userInfo:
                        if userName == temp["name"] and answer == temp["answer"]:
                            result = "name:{name},password:{password}".format(name=temp["name"],password=temp["pwd"])
                            return render(request,"retrievePassword.html",{"result":result})
                    else:
                        result = "answer is error"
                        return render(request,"retrievePassword.html",{"result":result})
            else:
                result = "user not exits"
                return render(request,"retrievePassword.html",{"result":result})
        else:
            return render(request,"retrievePassword.html",{"result":result})

def changePassword(request):
    userName = request.POST.get("userName")
    question = request.POST.get("question")
    answer = request.POST.get("answer")
    newPassword = request.POST.get("newPassword")
    confirmPassword = request.POST.get("confirmPassword")
    result = ""
    if userName != "" and newPassword != "":
        if request.POST.get("changePassword"):
            if newPassword != confirmPassword:
                result = "Password inconsistent"
                return render(request,"changePassword.html",{"result":result})
            else:
                for i in userInfo:
                    if i["name"] == userName:
                        for temp in userInfo:
                            if userName == temp["name"] and answer == temp["answer"]:
                                temp["pwd"] = newPassword
                                result = "Success"
                                return render(request,"changePassword.html",{"result":result})
                else:
                    result = "user not exits"
                    return render(request,"changePassword.html",{"result":result})
        else:
            return render(request,"changePassword.html",{"result":result})

