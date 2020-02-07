from django import forms


class RegisForm(forms.Form):
    namalengkap = forms.CharField(label='Nama Lengkap', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    pilihantahun = range(1980, 2020)
    tanggallahir = forms.DateField(label='Tanggal Lahir', widget=forms.SelectDateWidget(years=pilihantahun))
    jenis_kelamin = (
        ('p', 'pria'),
        ('w', 'wanita'),
    )
    jeniskelamin = forms.ChoiceField(widget=forms.RadioSelect, choices=jenis_kelamin)
    alamat = forms.CharField(widget=forms.Textarea, required=False)
    setuju = forms.BooleanField()

