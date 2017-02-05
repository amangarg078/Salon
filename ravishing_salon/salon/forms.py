from django import forms

from .models import SalonStore,Photo
class QueryForm(forms.Form):
    by_name=forms.CharField(max_length=200)
    by_locality=forms.CharField(max_length=256)

class UploadForm(forms.ModelForm):
	"""name = forms.CharField(max_length=256)
	address_1 = forms.CharField(max_length=128)
	address_2 = forms.CharField(max_length=128)
	address_3 = forms.CharField(max_length=128)
	state=forms.CharField(max_length=128)
	country= forms.CharField(max_length=128)
	contact_number= forms.CharField(max_length=12)
	email=forms.EmailField()
"""
	def __init__(self, *args, **kwargs):
		super(UploadForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
                'class': 'form-control col-lg-8 '
        })
	class Meta:
		model=SalonStore
		fields = ['name', 'address_1', 'address_2','address_3','state','country','contact_number','email']

class UploadFileForm(forms.ModelForm):

	class Meta:
		model=Photo
		fields=['title','image','is_cover_photo']
	def __init__(self, *args, **kwargs):
		super(UploadFileForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
                'class': 'form-control col-lg-6'
        })