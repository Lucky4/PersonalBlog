from django import forms
from PersonalBlog_app.models import Post

# To search posts through the title.
class SearchForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the tilte")

    class Meta:
        model = Post
        fields = ('title',)

    def clean_title(self):
        title = self.cleaned_data['title']
        num_words = len(title.split())

        if num_words > 20:
            raise forms.ValidationError("Not enough words!")
        return title
