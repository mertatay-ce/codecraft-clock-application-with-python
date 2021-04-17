Merhabalar!

Projeyi baþka bir bilgisayarda çalýþtýrmak için 
1- python 3.* kurulmalýdýr.
2- pyhton kurulduktan sonra pip install virtualenv ile virtualenv modulu kurulmalýdýr.
3- bir virtualenv ortamý yani sanal ortam kurarken yapmanýz gerekenler ise 
    - proje klasörüne girin 
    - python -m venv "proje klasorunun adý" þeklinde komut istemine(cmd) ye yazýn (örnek: python -m venv sanalortam)
    - ilgili klasörün içinde verdiðiniz ad olarak klasör oluþacaktýr.
    - daha sonra bu sanal ortama cmd den girmek için 
      bulundugunuz proje klasöründe \verdiðiniz ad\scripts\activate yazýn
    - Sanal ortamýnýz aktif olacaktýr.

Sanal ortam aktif etme  komutu = codecraft_sanalortam\scripts\Activate

4- projede kullandýðýmýz modüllerin kurulumu için 
     - Sanal ortamý aktif hale getirin
     - (codecraft_sanalortam) c:\\....\\\.\\.\\ -> þeklinde olmasý aktif oldugunu gösterir
     
     - modullerý yuklemek için
       pip install -r moduller.txt
       yazýp direk kurabilirsiniz.
5- Sanal ortamý kapatmak için 
   -deactivate komutunu sanal ortam acýkken yazmanýz yeterli