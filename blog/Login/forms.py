from django import forms
from django.forms import widgets
from django.forms import fields
from django.core.exceptions import ValidationError
from Login.models import UserInfo



class RegisterForm(forms.ModelForm):
    describ = fields.CharField(error_messages={'required': '介绍不能为空.'},
								widget=widgets.TextInput(),label="介绍")
    question = fields.CharField(error_messages={'required': '问题不能为空'},
                           widget=widgets.TextInput(), label="问题")
    answer = fields.CharField(error_messages={'required': '答案不能为空'},
                           widget=widgets.TextInput(), label="答案")
    userName = fields.CharField(max_length=20, min_length=3,
                                error_messages={'required': '用户名不能为空',
                                                'min_length': '用户名长度不能小于3',
                                                'max_length': '用户名长度不能大于20',
                                                },
                                widget=widgets.TextInput(),label="用户名"
								)
    password = fields.CharField(max_length=20, min_length=6,
								error_messages={'required': '密码不能为空.',
												'min_length': '密码长度不能小于6',
												'max_length': '密码长度不能大于20',
												},
        						widget=widgets.PasswordInput(),
        						label="密码"
        						)

    def clean_userName(self):
		result = UserInfo.objects.filter(userName=self.cleaned_data['userName'])
		if result:
			raise ValidationError('用户已经注册')
		return self.cleaned_data['userName']
