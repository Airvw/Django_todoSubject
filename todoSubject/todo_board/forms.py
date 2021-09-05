from django import forms
from .models import TodoList

# __file__ : 현재 소스 파일의 이름을 가져옵니다. (전체 경로 포함)
# os.path.dirname : 현재 소스 파일의 폴더 경로만 가져옵니다.
# os.path.join : 폴더와 파일을 결합합니다.
# os.path.abspath : 절대 경로로 변경합니다.
# sys.path.append : python의 (import 가능한)경로를 추가합니다.

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('title', 'content', 'end_date')
        widgets = {
            'end_date' : DateInput()
        }