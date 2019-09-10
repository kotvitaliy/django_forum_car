from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Author, Article, Comment



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def save(self, *args, **kwargs):
        django_user = User.objects.create_user(username=self.cleaned_data['username'],
                                               first_name=self.cleaned_data['first_name'],
                                               last_name=self.cleaned_data['last_name'],
                                               password=self.cleaned_data['password1'],
                                               email=self.cleaned_data['email'],
                                               is_staff=True,
                                               is_active=True
                                               )
        Author.objects.create(user=django_user)
        return django_user

    def get_cleaned_data(self, *args, **kwargs):
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
                # fields = "__all__"
        exclude = ('user',)
        # widgets = {
        #     'date_birth': forms.DateInput(format=('%m/%d/%Y'),
        #                                   attrs={'class': 'form-control',
        #                                          'placeholder': 'Select a date',
        #                                          'type': 'text'}),
        # }


class ArticleForm(forms.ModelForm):

    def save(self, *args, **kwargs):
        self.instance.author = kwargs['author']
        self.instance.save()

    class Meta:
        model = Article
        exclude = ['author', 'create_at', 'comments']


class CommentForm(forms.ModelForm):

    def save(self, commit=False, *args, **kwargs):
        print(self.instance)
        self.instance.from_user = kwargs['from_user']
        print('save comment!!!!!')
        print(kwargs['from_user'])
        self.instance.save()
        return self.instance

    class Meta:
        model = Comment
        exclude = ['from_user']


