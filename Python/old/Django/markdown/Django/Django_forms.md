# `Forms 表单`

- `from django import forms`
- 自定义form表单类，需要继承forms.Form

## 为什么要使用forms表单

1. 可以很方便的自动生成HTML表单
2. 可以比较方便的校验表单中的数据
3. 当提交出错时，可以保留用户的提交过的信息，而不用自己编写视图逻辑返回

## 如何定义forms表单

- 推荐创建一个forms.py文件用来定义forms表单类

  ```python
  from django import forms
  class ContactForm(forms.Form):
      """"""
      subject = forms.CharField()
      email = forms.EmailField(required=False)
      message = forms.CharField()
  ```

- 为了校验数据，需要实例化一个`Form`对象，并传入一个与定义匹配的字典类型数据

  - .is_valid()校验数据是否合法
  - .cleaned_data，清洗数据，返回一个装有原数据的字典。

  ```python
  >>> data = {"subject": "xxx", "email": "1558255789@qq.com", "message": "bbb"}
  >>> form = ContactForm(data)
  >>> form.is_valid()
  True
  >>> form.cleaned_data
  {'subject': 'xxx', 'email': '1558255789@qq.com', 'message': 'bbb'}
  ```

  