from django.shortcuts import render
from Login.models import UserInfo, Passage, Replies
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def loginPage(request):
    return render(request, "homePage.html")

def homePage(request):
    passages = Passage.objects.all()
    userName = request.session.get("name", None)
    return render(request, "userPage.html", {"passages": passages, "userName": userName})

def Logoff(request):
    if request.POST.get("Logoff"):
        del request.session["name"]
        return render(request, "homePage.html")
    else:
        return render(request, "userPage.html")

def login(request):
    passages = Passage.objects.all()
    userName = request.POST.get("userName")
    password = request.POST.get("password")
    result = ""
    user = UserInfo.objects.all()
    if userName != "" and password != "":
        if request.POST.get("Login"):
            for temp in user:
                if userName == temp.userName:
                    one = UserInfo.objects.get(userName=userName)
                    if one.loginTimes < 3:
                        if one.password == password:
                            one.loginTimes = 0
                            one = one.save()
                            request.session["name"] = userName
                            request.session.set_expiry(0)
                            return render(request, "userPage.html", {"userName": userName, "passages": passages})
                        else:
                            one.loginTimes += 1
                            one = one.save()
                            result = "password is error"
                            return render(request, "homePage.html", {"result": result, "userName": userName})
                    else:
                        result = "Please retrieve password"
                        return render(request, "retrievePassword.html", {"result": result})
            else:
                result = "Fail,user not exist"
                return render(request, "homePage.html", {"result": result, "userName": userName})
    else:
        result = ""
        return render(request, "homePage.html", {"result": result})

def register(request):
    userName = request.POST.get("userName")
    describe = request.POST.get("describe")
    password = request.POST.get("password")
    confirmPassword = request.POST.get("confirmPassword")
    question = request.POST.get("question")
    answer = request.POST.get("answer")
    result = ""
    user = UserInfo.objects.all()
    if userName != "" and password != "" and answer != "":
        if request.POST.get("register"):
            if len(userName) >= 3 and len(userName) <= 20:
                if len(password) >= 6 and len(password) <= 20:
                    if password != confirmPassword:
                        result = "Password inconsistent"
                        return render(request, "register.html", {"result": result})
                    else:
                        for temp in user:
                            if userName == temp.userName:
                                result = "user already exists"
                                return render(request, "register.html", {"result": result})
                        else:
                            newUser = UserInfo(describe=describe, userName=userName, password=password, question= \
                                question, answer=answer)
                            newUser.save()
                            result = "Success"
                            return render(request, "register.html", {"result": result})
                else:
                    result = "The length of the password is between 6 and 20"
                    return render(request, "register.html", {"result": result})
            else:
                result = "The length of user name is between 3 and 20"
                return render(request, "register.html", {"result": result})

        else:
            return render(request, "register.html", {"result": result})

def retrievePassword(request):
    userName = request.POST.get("userName")
    question = request.POST.get("question")
    answer = request.POST.get("answer")
    result = ""
    user = UserInfo.objects.all()
    if userName != "" and answer != "":
        if request.POST.get("retrievePassword"):
            for i in user:
                if userName == i.userName:
                    one = UserInfo.objects.get(userName=i.userName)
                    if one.question == question and one.answer == answer:
                        one.loginTimes = 0
                        one.save()
                        result = "name:{name},password:{password}".format(name=one.userName, password=one.password)
                        return render(request, "retrievePassword.html", {"result": result})
                    else:
                        result = "answer is error"
                        return render(request, "retrievePassword.html", {"result": result, "userName": userName, \
                                                                         "question": question, "answer": answer})
            else:
                result = "user not exits"
                return render(request, "retrievePassword.html", {"result": result})
        else:
            return render(request, "retrievePassword.html", {"result": result})

def changePassword(request):
    userName = request.POST.get("userName")
    question = request.POST.get("question")
    answer = request.POST.get("answer")
    newPassword = request.POST.get("newPassword")
    confirmPassword = request.POST.get("confirmPassword")
    result = ""
    user = UserInfo.objects.all()
    if userName != "" and newPassword != "":
        if request.POST.get("changePassword"):
            if newPassword != confirmPassword:
                result = "Password inconsistent"
                return render(request, "changePassword.html", {"result": result, "userName": userName, "question": \
                    question, "answer": answer})
            else:
                for i in user:
                    if i.userName == userName:
                        one = UserInfo.objects.get(userName=i.userName)
                        if one.question == question and one.answer == answer:
                            one.password = newPassword
                            one.loginTimes = 0
                            one.save()
                            result = "Success"
                            return render(request, "changePassword.html", {"result": result})
                        else:
                            result = "answer is error"
                            return render(request, "changePassword.html", {"result": result, "userName": userName, \
                                                                           "question": question})
                else:
                    result = "user not exits"
                    return render(request, "changePassword.html", {"result": result})
        else:
            return render(request, "changePassword.html", {"result": result})

@csrf_exempt
def newPassage(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    userName = request.session.get("name", None)
    result = ""
    if userName != None:
        if request.POST.get("submit"):
            author = UserInfo.objects.get(userName=userName)
            onePassage = Passage.objects.create(author=author, title=title, content=content)
            result = "success"
            return render(request, "newPassage.html", {"result": result})
        else:
            return render(request, "newPassage.html")
    else:
        result = "please login"
        return render(request, "homePage.html", {"result": result})

@csrf_exempt
def passagePage(request, passage_id):
    allReplies = Replies.objects.filter(passage=passage_id)
    passage = Passage.objects.get(id=passage_id)
    userName = request.session.get("name", None)
    if userName != None:
        if userName == passage.author.userName:
            if request.POST.get("edit"):
                if userName == passage.author.userName:
                    return render(request, "editPassage.html", {"passage": passage, "allReplies": allReplies})
            elif request.POST.get("delete"):
                if userName == passage.author.userName:
                    Passage.objects.get(id=passage_id).delete()
                    return render(request, "success.html")
            else:
                return render(request, "passage.html", {"passage": passage, "allReplies": allReplies})
        else:
            return render(request, "passage.html", {"passage": passage, "allReplies": allReplies})
    else:
        result = "please login"
        return render(request, "homePage.html", {"result": result})


@csrf_exempt
def editPassage(request, passage_id):
    passage = Passage.objects.get(id=passage_id)
    userName = request.session.get("name", None)
    newTitle = request.POST.get("title")
    newContent = request.POST.get("content")
    result = ""
    if userName == passage.author.userName:
        if request.POST.get("finish"):
            passage = Passage.objects.filter(id=passage_id).update(title=newTitle, content=newContent)
            result = "success"
            return render(request, "success.html", {"result": result, "passage": passage})
        else:
            return render(request, "editPassage.html", {"result": result})
    else:
        result = "please login"
        return render(request, "homePage.html", {"result": result})

@csrf_exempt
def replies(request, passage_id):
    print("11111111")
    allReplies = Replies.objects.filter(passage=passage_id)
    userName = request.session.get("name", None)
    user = UserInfo.objects.get(userName=userName)
    passage = Passage.objects.get(id=passage_id)
    content = request.POST.get("replies")
    if userName != None:
        if request.POST.get("reply"):
            print("jjjjj")
            oneReplies = Replies.objects.create(author=user, content=content, passage=passage)
            return render(request, "passage.html", {"allReplies": allReplies, "passage": passage})
        else:
            return render(request, "passage.html", {"allReplies": allReplies, "passage": passage})
    else:
        result = "please login"
        return render(request, "homePage.html", {"result": result})

@csrf_exempt
def delReplies(request, replies_id):
    allReplies = Replies.objects.filter(id=replies_id)
    userName = request.session.get("name", None)
    if userName == allReplies.author.userName:
        if request.POST.get("delete"):
            Replies.objects.get(id=replies_id).delete()
            return render(request, "passage.html")
    else:
        return render(request, "passage.html", {"allReplies": allReplies})

