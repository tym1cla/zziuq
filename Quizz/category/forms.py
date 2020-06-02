from django import forms

category_list = (
    ('Geography', 'Geography'),
    ('Entertainment', 'Entertainment'),
    ('History', 'History'),
    ('Literature', 'Literature'),
    ('Science', 'Science'),
    ('Sport', 'Sport'),
)

number_list = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)


class QuestionForm(forms.Form):
    category = forms.ChoiceField(label='', choices=category_list)
    question = forms.CharField(max_length=200, label='', widget=forms.Textarea(attrs={'placeholder': 'Enter question'}))
    answer_1 = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter first answer', 'size':20}))
    answer_2 = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter second answer'}))
    answer_3 = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter third answer'}))
    answer_4 = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter fourth answer'}))
    correct_answer = forms.ChoiceField(label='', choices=number_list)