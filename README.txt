Merhabalar!

Projeyi ba�ka bir bilgisayarda �al��t�rmak i�in 
1- python 3.* kurulmal�d�r.
2- pyhton kurulduktan sonra pip install virtualenv ile virtualenv modulu kurulmal�d�r.
3- bir virtualenv ortam� yani sanal ortam kurarken yapman�z gerekenler ise 
    - proje klas�r�ne girin 
    - python -m venv "proje klasorunun ad�" �eklinde komut istemine(cmd) ye yaz�n (�rnek: python -m venv sanalortam)
    - ilgili klas�r�n i�inde verdi�iniz ad olarak klas�r olu�acakt�r.
    - daha sonra bu sanal ortama cmd den girmek i�in 
      bulundugunuz proje klas�r�nde \verdi�iniz ad\scripts\activate yaz�n
    - Sanal ortam�n�z aktif olacakt�r.

Sanal ortam aktif etme  komutu = codecraft_sanalortam\scripts\Activate

4- projede kulland���m�z mod�llerin kurulumu i�in 
     - Sanal ortam� aktif hale getirin
     - (codecraft_sanalortam) c:\\....\\\.\\.\\ -> �eklinde olmas� aktif oldugunu g�sterir
     
     - moduller� yuklemek i�in
       pip install -r moduller.txt
       yaz�p direk kurabilirsiniz.
5- Sanal ortam� kapatmak i�in 
   -deactivate komutunu sanal ortam ac�kken yazman�z yeterli