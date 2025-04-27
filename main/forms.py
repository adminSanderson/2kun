from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ["author_name", "title", "content", "parent"]
        widgets = {
            "parent": forms.HiddenInput(),
        }

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and image.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Размер файла не должен превышать 5 MB.")
        return image
