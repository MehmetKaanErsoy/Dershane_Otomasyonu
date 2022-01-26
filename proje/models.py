from enum import auto

from django.db import models

okul = [
    ("Adana Fen Lisesi", "Adana Fen Lisesi"),
    ("Seyhan İMKB Fen Lisesi", "Seyhan İMKB Fen Lisesi"),
    ("Adana Anadolu Lisesi", "Adana Anadolu Lisesi"),
    ("ÇEAS Anadolu Lisesi", "ÇEAS Anadolu Lisesi"),
    ("İsmail Safa Özler Anadolu Lisesi", "İsmail Safa Özler Anadolu Lisesi"),
    ("Piri Reis Anadolu Lisesi", "Piri Reis Anadolu Lisesi"),
    ("Kozan Fen Lisesi", "Kozan Fen Lisesi"),
    ("Adana Ticaret Odası Anadolu Lisesi", "Adana Ticaret Odası Anadolu Lisesi"),
    ("Eczacı Bahattin-Sevinç Erdinç Fen Lisesi", "Eczacı Bahattin-Sevinç Erdinç Fen Lisesi"),
    ("Sungurbey Anadolu Lisesi", "Sungurbey Anadolu Lisesi"),
    ("Seyhan Rotary Anadolu Lisesi", "Seyhan Rotary Anadolu Lisesi"),
    ("Borsa Anadolu Lisesi", "Borsa Anadolu Lisesi"),
    ("Seyhan Danişment Gazi Anadolu Lisesi", "Seyhan Danişment Gazi Anadolu Lisesi"),
    ("Hümeyra Ökten Kız Anadolu İmam Hatip Lisesi", "Hümeyra Ökten Kız Anadolu İmam Hatip Lisesi"),
    ("75.Yıl Anadolu Lisesi", "75.Yıl Anadolu Lisesi"),
    ("Fatih Anadolu Lisesi", "Fatih Anadolu Lisesi"),
    ("Yüreğir Halıcılar Anadolu Lisesi", "Yüreğir Halıcılar Anadolu Lisesi"),
    ("Şehit Zeynep Sağır Anadolu Lisesi", "Şehit Zeynep Sağır Anadolu Lisesi"),
    ("Bahtiyar Vahabzade Sosyal Bilimler Lisesi", "Bahtiyar Vahabzade Sosyal Bilimler Lisesi"),
    ("Ceyhan Ticaret Borsası Sosyal Bilimler Lisesi", "Ceyhan Ticaret Borsası Sosyal Bilimler Lisesi"),
    ("Ceyhan Anadolu Lisesi", "Ceyhan Anadolu Lisesi"),
    ("Fatih Sultan Mehmet Mesleki ve Teknik Anadolu Lisesi", "Fatih Sultan Mehmet Mesleki ve Teknik Anadolu Lisesi"),
    ("Yaşar Rukiye Kısacık Anadolu İmam Hatip Lisesi", "Yaşar Rukiye Kısacık Anadolu İmam Hatip Lisesi"),
    ("Adana Kıvanç Anadolu İmam Hatip Lisesi", "Adana Kıvanç Anadolu İmam Hatip Lisesi"),
    ("İmamoğlu Anadolu İmam Hatip Lisesi", "İmamoğlu Anadolu İmam Hatip Lisesi"),
    ("Fatıma Zehra Kız Anadolu İmam Hatip Lisesi", "Fatıma Zehra Kız Anadolu İmam Hatip Lisesi"),
    ("Medine Müdafii Fahreddin Paşa Anadolu İmam Hatip Lisesi",
     "Medine Müdafii Fahreddin Paşa Anadolu İmam Hatip Lisesi"),
    ("Ceyhan Kız Anadolu İmam Hatip Lisesi", "Ceyhan Kız Anadolu İmam Hatip Lisesi"),
    ("Çukurova Elektrik Mesleki ve Teknik Anadolu Lisesi", "Çukurova Elektrik Mesleki ve Teknik Anadolu Lisesi"),
    ("Kozan Şehit Arda Can Mesleki ve Teknik Anadolu Lisesi", "Kozan Şehit Arda Can Mesleki ve Teknik Anadolu Lisesi"),
    ("Kurttepe Şehit Ali Öztaş Mesleki ve Teknik Anadolu Lisesi",
     "Kurttepe Şehit Ali Öztaş Mesleki ve Teknik Anadolu Lisesi"),
    ("Heydar Aliyev Mesleki ve Teknik Anadolu Lisesi", "Heydar Aliyev Mesleki ve Teknik Anadolu Lisesi"),
    ("Borsa İstanbul Mesleki ve Teknik Anadolu Lisesi", "Borsa İstanbul Mesleki ve Teknik Anadolu Lisesi"),
    ("Adana Mesleki ve Teknik Anadolu Lisesi", "Adana Mesleki ve Teknik Anadolu Lisesi"),
    ("Kurttepe Şehit Ali Öztaş Mesleki ve Teknik Anadolu Lisesi",
     "Kurttepe Şehit Ali Öztaş Mesleki ve Teknik Anadolu Lisesi"),
    ("Sabancı Mesleki ve Teknik Anadolu Lisesi", "Sabancı Mesleki ve Teknik Anadolu Lisesi"),
    ("Kozan Kız Anadolu İmam Hatip Lisesi", "Kozan Kız Anadolu İmam Hatip Lisesi"),
    ("Yeşilevler Mesleki ve Teknik Anadolu Lisesi", "Yeşilevler Mesleki ve Teknik Anadolu Lisesi"),
    ("Türk Tekstil Vakfı Mesleki ve Teknik Anadolu Lisesi", "Türk Tekstil Vakfı Mesleki ve Teknik Anadolu Lisesi"),
    ("Kiremithane Mesleki ve Teknik Anadolu Lisesi", "Kiremithane Mesleki ve Teknik Anadolu Lisesi"),
    ("İsmet İnönü Mesleki ve Teknik Anadolu Lisesi", "İsmet İnönü Mesleki ve Teknik Anadolu Lisesi"),
    ("Adana Seyhan Şehit Bora Süelkan Mesleki ve Teknik Anadolu Lisesi",
     "Adana Seyhan Şehit Bora Süelkan Mesleki ve Teknik Anadolu Lisesi"),
    ("Ceyhan Mesleki ve Teknik Anadolu Lisesi", "Ceyhan Mesleki ve Teknik Anadolu Lisesi"),
]

taksit = [
    ("0", "Taksit Miktarı Seçiniz"),
    ("3", "3 Taksit"),
    ("4", "4 Taksit"),
    ("5", "5 Taksit"),
    ("6", "6 Taksit"),
    ("9", "9 Taksit"),
    ("12", "12 Taksit"),
]
evlimi = [
    ("Bekar", "Bekar"),
    ("Evli", "Evli"),
]
sınıf = [
    ("4", "4. Sınıf"),
    ("5", "5. Sınıf"),
    ("6", "6. Sınıf"),
    ("7", "7. Sınıf"),
    ("8", "8. Sınıf"),
    ("9", "9. Sınıf"),
    ("10", "10. Sınıf"),
    ("11", "11. Sınıf"),
    ("12", "12. Sınıf"),
    ("Mezun", "Mezun"),
]
brans = [
    ("Matematik", "Matematik"),
    ("Türkçe", "Türkçe"),
    ("Fizik", "Fizik"),
    ("Kimya", "Kimya"),
    ("Biyoloji", "Biyoloji"),
    ("Geometri", "Geometri"),
    ("Tarih", "Tarih"),
    ("Felsefe", "Felsefe"),
]


class OgrenciModel(models.Model):
    id = models.AutoField(primary_key=True)
    Veli_AdıSoyadi = models.CharField(max_length=30)
    VeliTel = models.CharField(max_length=11)
    OgrenciTC = models.CharField(max_length=11)
    OgrenciAdi_Soyadi = models.CharField(max_length=50)
    OgrenciTel = models.CharField(max_length=11, default=VeliTel)
    OgrenciOkul = models.CharField(choices=okul, max_length=1150)
    Adres = models.CharField(max_length=100)
    Odenecek_Ucret = models.PositiveIntegerField(null=True)
    Taksit_Bolme = models.CharField(max_length=100, choices=taksit)
    kacinci_sınıf = models.CharField(max_length=10, choices=sınıf)
    tarih = models.DateTimeField(auto_now_add=True)
    O_ankiÖdeme = models.PositiveIntegerField(null=True)
    kalan = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.OgrenciAdi_Soyadi} - {self.OgrenciTC}'

    class Meta:
        ordering = ['OgrenciAdi_Soyadi', ]


class sinif_olaylari(models.Model):
    id = models.AutoField(primary_key=True)
    sinifsec = models.CharField(max_length=10, choices=sınıf)
    harf = models.CharField(max_length=10, null=False)
    sinif_mevcut = models.PositiveIntegerField(null=True)
    date_tarih = models.DateTimeField(auto_now_add=True)
    Matematik = models.CharField(max_length=100, null=True)
    Türkçe = models.CharField(max_length=100, null=True)
    Fizik = models.CharField(max_length=100, null=True)
    Biyoloji = models.CharField(max_length=100, null=True)
    Kimya = models.CharField(max_length=100, null=True)
    Tarih = models.CharField(max_length=100, null=True)
    Felsefe = models.CharField(max_length=100, null=True)
    Geometri = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.sinifsec}\{self.harf}'


class sinifaogrenciata(models.Model):
    id = models.AutoField(primary_key=True)
    sinifsec = models.ForeignKey(sinif_olaylari, on_delete=models.CASCADE)
    ogrencisec = models.ForeignKey(OgrenciModel, on_delete=models.CASCADE)
    sinifogrenci_kayıttarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sinifsec} - {self.ogrencisec}'


class OgretmenEkle(models.Model):
    id = models.AutoField(primary_key=True)
    Ogretmen_adisoyadi = models.CharField(max_length=100)
    Ogretmen_TC = models.PositiveIntegerField(null=False)
    Ogretmen_Telefon = models.CharField(max_length=11)
    Ogretmen_Brans = models.CharField(choices=brans, max_length=100)
    Ogretmen_KacYıllıkSozlesme = models.PositiveIntegerField(null=True)
    Ogretmen_Maas = models.PositiveIntegerField(null=False)
    Ogretmen_KayıtTarihi = models.DateTimeField(auto_now_add=True)
    Ogretmen_KalanMaas = models.PositiveIntegerField(null=True)
    Ogretmen_Evlimi = models.CharField(choices=evlimi, max_length=100)
    Ogretmen_Adres = models.CharField(max_length=200)
    Ogretmen_Resim = models.FileField(upload_to='images/', null=True)

    def __str__(self):
        return f'{self.Ogretmen_adisoyadi} - {self.Ogretmen_Brans}'


class Ders(models.Model):
    ders_adi = models.CharField(max_length=100)

    def __str__(self):
        return self.ders_adi


class OgretmenAta(models.Model):
    id = models.AutoField(primary_key=True)
    sinif_sec = models.ForeignKey(sinif_olaylari, on_delete=models.CASCADE)
    ogretmen_sec = models.ForeignKey(OgretmenEkle, on_delete=models.CASCADE)
    ders_sec = models.ForeignKey(Ders, on_delete=models.CASCADE)
    tarih = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sinif_sec', ]

    def __str__(self):
        return f'{self.sinif_sec} - {self.ogretmen_sec} - {self.ders_sec}'
