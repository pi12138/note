from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=150)
    body = forms.CharField(widget=forms.Textarea(attr={'row': 3, 'cols': 60}))
    timestamp = forms.DateTimeField()
