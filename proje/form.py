from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import taksit, okul, sınıf, OgrenciModel, sinif_olaylari, sinifaogrenciata, OgretmenEkle, brans, evlimi, \
    OgretmenAta, Ders


class SınıfOgrenciForm(forms.ModelForm):
    sinifsec = forms.ModelChoiceField(queryset=sinif_olaylari.objects.all(), widget=forms.Select(attrs={
        'style': 'margin-left:230px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;font-size:18px',
    }))
    ogrencisec = forms.ModelChoiceField(queryset=OgrenciModel.objects.all(), widget=forms.Select(attrs={
        'style': 'margin-left:230px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;font-size:18px',
    }))

    class Meta:
        model = sinifaogrenciata
        fields = ['sinifsec', 'ogrencisec']


class Ogrenci_Billl(forms.ModelForm):
    Veli_AdıSoyadi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Veli İsim Soyisim...',
        'style': 'margin-left:230px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))
    VeliTel = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Veli Telefon Numarası...',
        'style': 'margin-top:20px;margin-left:230px;font-size:14px;;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))
    OgrenciTC = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Öğrenci T.C. kimlik numarası...',
        'style': 'margin-top:20px;margin-left:230px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))
    OgrenciAdi_Soyadi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Öğrenci isim soyisim...',
        'style': 'margin-top:20px;margin-left:230px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))
    OgrenciTel = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Öğrenci Telefon Numarası...',
        'style': 'margin-top:20px;margin-left:230px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))
    OgrenciOkul = forms.ChoiceField(choices=okul, widget=forms.Select(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Öğrenci isim soyisim...',
        'style': 'margin-top:20px;font-size:14px;margin-left:600px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;margin-top:-275px'}))
    Adres = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Adres...',
        'style': 'margin-top:20px;font-size:14px;margin-left:600px;width:250px;height:90px;border-radius:7px;border:solid 2.3px;'}))
    Odenecek_Ucret = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Ödenecek Ücret...',
        'style': 'margin-top:20px;font-size:14px;margin-left:600px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))
    Taksit_Bolme = forms.ChoiceField(choices=taksit, widget=forms.Select(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Öğrenci isim soyisim...',
        'style': 'margin-top:20px;font-size:14px;margin-left:600px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))
    kacinci_sınıf = forms.ChoiceField(choices=sınıf, widget=forms.Select(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Öğrenci isim soyisim...',
        'style': 'margin-top:20px;font-size:14px;margin-left:600px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))

    class Meta:
        model = OgrenciModel
        fields = ['Veli_AdıSoyadi', 'VeliTel', 'OgrenciTC', 'OgrenciAdi_Soyadi', 'OgrenciTel', 'OgrenciOkul',
                  'Adres', 'Odenecek_Ucret', 'Taksit_Bolme', 'kacinci_sınıf', ]


class ode(forms.ModelForm):
    O_ankiÖdeme = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Ödenecek Ücret Miktarını Giriniz...',
        'style': 'margin-top:30px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))

    class Meta:
        model = OgrenciModel
        fields = ['O_ankiÖdeme', ]


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label="Username", required=True, max_length=30,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'name': 'username',
                                   'placeholder': 'Kullanıcı adınız...',
                                   'style': 'font-family: "Segoe UI Semibold";margin-left:-220px;width:330px;height:40px;border-radius:5px;background-color:#eaeaea'}))
    password = forms.CharField(label="Password", required=True, max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'name': 'password',
                                   'placeholder': 'Parolanız...',
                                   'style': 'font-family: "Segoe UI Semibold";margin-left:-220px;width:330px;height:40px;border-radius:5px;background-color:#eaeaea'}))


class SinifForm(forms.ModelForm):
    sinifsec = forms.ChoiceField(choices=sınıf, widget=forms.Select(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Öğrenci isim soyisim...',
        'style': 'margin-top:20px;font-size:14px;margin-left:30px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))

    harf = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Sınıf Harfi Giriniz',
        'style': 'margin-top:20px;font-size:14px;margin-left:30px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;'}))

    class Meta:
        model = sinif_olaylari
        fields = ['sinifsec', 'harf', ]


class ImageForm(forms.ModelForm):
    Ogretmen_adisoyadi = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'Ogretmen_adisoyadi',
        'placeholder': 'Öğretmenin İsmini Ve Soyismini Giriniz...',
        'style': 'margin-top:20px;font-size:14px;margin-left:150px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;'
    }))
    Ogretmen_TC = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'Ogretmen_TC',
        'placeholder': 'Öğretmenin TC Numarasını Giriniz...',
        'style': 'margin-top:20px;font-size:14px;margin-left:150px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;'
    }))
    Ogretmen_Telefon = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'Ogretmen_Telefon',
        'placeholder': 'Öğretmenin Telefon Numarasını Giriniz...',
        'style': 'margin-top:20px;font-size:14px;margin-left:150px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;'
    }))

    Ogretmen_Brans = forms.ChoiceField(choices=brans, widget=forms.Select(attrs={
        'class': 'form-control',
        'name': 'Ogretmen_Brans',
        'placeholder': 'Öğretmen Branş...',
        'style': 'margin-top:20px;font-size:14px;margin-left:150px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))

    Ogretmen_Adres = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'Ogretmen_Adres',
        'placeholder': 'Öğretmenin Adresini Giriniz...',
        'style': 'margin-top:20px;font-size:14px;margin-left:550px;width:350px;height:139px;border-radius:7px;border:solid 2.3px;'
    }))

    Ogretmen_Evlimi = forms.ChoiceField(choices=evlimi, widget=forms.Select(attrs={
        'class': 'form-control',
        'name': 'Ogretmen_Evlimi',
        'placeholder': 'Öğretmen Branş...',
        'style': 'margin-top:20px;font-size:14px;margin-left:550px;width:250px;height:39px;border-radius:7px;border:solid 2.3px'}))

    Ogretmen_Maas = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'Ogretmen_Maas',
        'placeholder': 'Öğretmenin Maaşını Giriniz...',
        'style': 'margin-top:20px;font-size:14px;margin-left:550px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;'
    }))

    Ogretmen_KacYıllıkSozlesme = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'Ogretmen_KacYıllıkSozlesme',
        'placeholder': 'Öğretmenin Kaç Yıllık Sözleşme...',
        'style': 'margin-top:-215px;font-size:14px;margin-left:550px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;'
    }))

    class Meta:
        model = OgretmenEkle
        fields = ["Ogretmen_adisoyadi", "Ogretmen_TC", "Ogretmen_Telefon", "Ogretmen_Brans", "Ogretmen_Adres",
                  "Ogretmen_Evlimi", "Ogretmen_Maas",
                  "Ogretmen_KacYıllıkSozlesme", "Ogretmen_Resim", ]


class OgretmenSınıfDers(forms.ModelForm):
    sinif_sec = forms.ModelChoiceField(queryset=sinif_olaylari.objects.all(), widget=forms.Select(attrs={
        'style': 'margin-top:30px;margin-left:50px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;font-size:18px',
        'name': 'sinif_sec'
    }))
    ogretmen_sec = forms.ModelChoiceField(queryset=OgretmenEkle.objects.all(), widget=forms.Select(attrs={
        'style': 'margin-top:30px;margin-left:50px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;font-size:18px',
        'name': 'ogretmen_sec'
    }))
    ders_sec = forms.ModelChoiceField(queryset=Ders.objects.all(), widget=forms.Select(attrs={
        'style': 'margin-top:30px;margin-left:50px;font-size:14px;width:250px;height:39px;border-radius:7px;border:solid 2.3px;font-size:18px',
        'name': 'ders_sec'
    }))

    class Meta:
        model = OgretmenAta
        fields = ['sinif_sec', 'ders_sec', 'ogretmen_sec', ]
