from django import forms
from .models import Article, Advertisement

class SearchForm(forms.Form):
    query = forms.CharField(required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    min_rating = forms.IntegerField(required=False, min_value=0)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'content', 'image_filename', 'video_filename', 'pokemon', 'city']

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['headline', 'file_url', 'file_type', 'article']