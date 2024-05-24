CREATE TABLE Oteller(
    OtelID VARCHAR(15) NOT NULL,
    OtelAdi VARCHAR(50) NOT NULL ,
    OtelAdres VARCHAR(50) NOT NULL ,
    OtelSiralama VARCHAR(5) NOT NULL,
    PRIMARY KEY(OtelID)
    
);
CREATE TABLE Odalar(
    OtelID VARCHAR(15) NOT NULL,
    OdaNo VARCHAR(200) NOT NULL,
    Fiyat int NOT NULL ,
    OdaTuru VARCHAR(50) NOT NULL ,
	DolulukOrani BIT  NOT NULL ,
	PRIMARY KEY (OdaNo),
	Foreign KEY (OtelID) REFERENCES Oteller(OtelID)
);
CREATE TABLE Musteri(
    MusteriTC VARCHAR(50) NOT NULL ,
    AD VARCHAR(255) NOT NULL,
	SOYAD VARCHAR(255) NOT NULL,
    ADRES VARCHAR(255) NOT NULL ,
    TELEFON VARCHAR(20) NOT NULL ,
    PRIMARY KEY (MusteriTC)
);

CREATE TABLE Konaklama(
    OdaNo VARCHAR(200) NOT NULL,
    Giris date NOT NULL,
    Ayrilma date NOT NULL ,
    Ucret int NOT NULL ,
	MusteriTC VARCHAR(50) NOT NULL ,
	
	Foreign KEY (OdaNo) REFERENCES Odalar(OdaNo),
	Foreign KEY (MusteriTC) REFERENCES Musteri(MusteriTC) 
	

);
CREATE TABLE Tesisler(
    TesisID VARCHAR(15) NOT NULL,
    Spor_Salonu VARCHAR(11) NOT NULL,
    Cafe VARCHAR(15) NOT NULL,
    Restoran VARCHAR(50) NOT NULL ,
	PRIMARY KEY (TesisID),
	Foreign KEY (TesisID) REFERENCES Oteller(OtelID)
	

);





CREATE TABLE Calisanlar(

    YoneticiTC VARCHAR(11),
	OtelID VARCHAR(15) not null,
	CalisanTC VARCHAR(11) UNIQUE NOT NULL,
    CalisanAdi VARCHAR(50) NOT NULL,
	CalisanSoyadi VARCHAR(50) NOT NULL,
    Baslama_tarihi date  NOT NULL ,
	PRIMARY KEY (CalisanTC),
	Foreign KEY (YoneticiTC) REFERENCES Calisanlar(CalisanTC),
	Foreign KEY (OtelID) REFERENCES Oteller(OtelID)
);







CREATE TABLE Kullanim(
    KullanimSuresi TIME NOT NULL,
    TesisID VARCHAR(15) NOT NULL,
    MusteriTC VARCHAR(50) NOT NULL,
    Foreign KEY (TesisID) REFERENCES Tesisler(TesisID) , 
    Foreign KEY (MusteriTC) REFERENCES Musteri(MusteriTC)
    
);


select * from Calisanlar 
SELECT YoneticiTC FROM Calisanlar where OtelID=1
SELECT YoneticiTC,CalisanAdi,Calisanlar.OtelID,Oteller.OtelAdi FROM Calisanlar,Oteller where YoneticiTC=CalisanTC and Calisanlar.OtelID=Oteller.OtelID
select YoneticiTC from Calisanlar where YoneticiTC=CalisanTC 
select CalisanAdi,CalisanSoyadi,CalisanTC,Baslama_tarihi,Calisanlar.OtelID from Calisanlar where YoneticiTC=CalisanTC
select YoneticiTC from Calisanlar where CalisanTC!='40218277382' and OtelID=1
select CalisanAdi,CalisanSoyadi,CalisanTC,Baslama_tarihi,Calisanlar.OtelID from Calisanlar where YoneticiTC!=CalisanTC

select CalisanTC,CalisanAdi,Oteller.OtelID from Calisanlar,Oteller where YoneticiTC=CalisanTC and Oteller.OtelID=Calisanlar.OtelID

select CalisanAdi,OtelAdi from Calisanlar,Oteller where YoneticiTC='40218277382' and Calisanlar.OtelID=Oteller.OtelID

select YoneticiTC from Calisanlar,Oteller where Oteller.OtelID=3

select CalisanAdi,CalisanSoyadi,OtelAdi from Oteller,Calisanlar where Calisanlar.OtelID=Oteller.OtelID

Select Calisanlar.CalisanAdi
  From Calisanlar ,Oteller
 Where Calisanlar.OtelID = '4' and Calisanlar.OtelID = Oteller.OtelID





--Müþteri Ekleme
INSERT INTO Musteri(MusteriTC, AD,SOYAD, ADRES, TELEFON) 
VALUES ('11111111111','BEYZA', 'YALÇIN', 'BURSA', '5555555555')
INSERT INTO Musteri(MusteriTC, AD,SOYAD, ADRES, TELEFON) 
VALUES('25364455600', 'Beyzanur', 'Okyar', 'Pasabayýr mahallesi','05368775046')
INSERT INTO Musteri(MusteriTC, AD,SOYAD, ADRES, TELEFON) 
VALUES('6984455800', 'Beyza', 'Atay', 'Ýstanbul','05368845041')
INSERT INTO Musteri(MusteriTC, AD,SOYAD, ADRES, TELEFON) 
VALUES('78264455600', 'Hasan', 'Yüksel', 'Sakarya','05168775098')
INSERT INTO Musteri(MusteriTC, AD,SOYAD, ADRES, TELEFON) 
VALUES('17864455600', 'Merve', 'Baðýþlar', 'Antalya','051687754859')
INSERT INTO Musteri(MusteriTC, AD,SOYAD, ADRES, TELEFON) 
VALUES('9854129602', 'Kaan', 'Çam', 'Antalya','05168774589')
Insert Into Musteri (MusteriTC,AD,SOYAD,ADRES,TELEFON)
Values('5874961254','Muhammed Ali','Öztürk','Ýstanbul','05269874158')
Insert Into Musteri (MusteriTC,AD,SOYAD,ADRES,TELEFON)
Values('8543796518','Ayþe','Demir','Ýstanbul','05234578978')
Insert Into Musteri (MusteriTC,AD,SOYAD,ADRES,TELEFON)
Values('25463547895','ibrahim','korkmaz','Ýstanbul','05234578170')

Select *from Musteri
SELECT * FROM Oteller
SELECT * FROM Odalar
SELECT * FROM Calisanlar
Select * from Tesisler
SELECT TesisID,OtelID,Cafe,Restoran,Spor_Salonu FROM Tesisler,Oteller where Tesisler.TesisID=Oteller.OtelID
--SELECT Oteller.OtelID,YoneticiID FROM Oteller,Calisanlar,Yonetici where Calisanlar.CalisanID=Yonetici.YoneticiID and Calisanlar.OtelID= Oteller.OtelID
--SELECT CalisanAdi,CalisanSoyadi from Calisanlar,Yonetici where Yonetici.YoneticiID=3 and Calisanlar.CalisanID=3
SELECT * FROM Konaklama
SELECT * FROM Kullanim


--Otel Ekleme
INSERT INTO Oteller(OtelID,OtelAdi, OtelAdres, OtelSiralama) 
    VALUES ('1', 'Perama', 'Pasabayýr mahallesi', '4')
INSERT INTO Oteller(OtelID,OtelAdi, OtelAdres, OtelSiralama)
    VALUES ('2', 'Grand Asya', 'Atatürk Caddesi',  '4');
INSERT INTO Oteller(OtelID,OtelAdi, OtelAdres, OtelSiralama)
    VALUES('3', 'Bandýrma Palas', 'Çarþý Caddesi', '5');
INSERT INTO Oteller(OtelID,OtelAdi, OtelAdres, OtelSiralama)
    VALUES('4', 'Grand Asya2', 'Atatürk Caddesi', '5');
INSERT INTO Oteller(OtelID,OtelAdi, OtelAdres, OtelSiralama)
    VALUES('5', 'Aysel Palas', 'Yeni Mahallesi', '2');
INSERT INTO Oteller(OtelID,OtelAdi, OtelAdres, OtelSiralama)
    VALUES('9', 'Kus Adasi', 'Sadýk Caddesi', '5');
INSERT INTO Oteller(OtelID,OtelAdi, OtelAdres, OtelSiralama)
    VALUES('7', 'Antalya', 'Konyaaltý', '5');
INSERT INTO Oteller(OtelID,OtelAdi, OtelAdres, OtelSiralama)
    VALUES('8', 'Karadeniz', 'zirvevaran yolu', '4');

--Oda Ekleme
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('115', '100', 0,'Standart Oda', '4')	
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('116', '150', 1,'Suit' ,'4')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('117', '200', 0,'Deluxe Oda', '4')	
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('118', '150', 1,'Aile Odasý', '4')	
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('119', '300', 1,'Kral Dairesi', '4')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('52', '400', 0,'Standart Oda', '1')		
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('1025', '560', 1,'Deluxe Oda', '1')	
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('63', '450', 0,'Deluxe Odasý', '1')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('73', '450', 1,'Kral Odasý', '2')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('233', '450', 0,'standart Odasý', '2')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('634', '250', 0,'standart Odasý', '2')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('345', '450', 0,'Aile Odasý', '3')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('123', '450', 0,'Aile Odasý', '5')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('783', '450', 0,'standart Odasý', '7')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('1223', '450', 0,'Aile Odasý', '7')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('190', '450', 1,'Aile Odasý', '7')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('903', '900', 0,'superlux Oda', '8')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('343', '450', 1,'Aile Odasý', '8')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('933', '1000', 0,'Ultralux Odasý', '8')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('543', '450', 1,'Aile Odasý', '9')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('255', '500', 0,'Aile Odasý', '9')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('155', '675', 0,'Aile Odasý', '9')
INSERT INTO Odalar(OdaNo,Fiyat, DolulukOrani, OdaTuru,OtelID) 
    VALUES ('107', '875', 0,'Aile Odasý', '9')



Insert Into Calisanlar(YoneticiTC,OtelID,CalisanTC,CalisanAdi,CalisanSoyadi,Baslama_tarihi)
Values('40218277382','1','40218277382','Ali','Atay','2023-01-15')
Insert Into Calisanlar(YoneticiTC,OtelID,CalisanTC,CalisanAdi,CalisanSoyadi,Baslama_tarihi)
Values('12321332423','2','12321332423','mehmet','kero','2023-01-15')
Insert Into Calisanlar(YoneticiTC,OtelID,CalisanTC,CalisanAdi,CalisanSoyadi,Baslama_tarihi)
Values('40218277382','3','43534231231','beyza','okyar','2023-01-15')
Insert Into Calisanlar(YoneticiTC,OtelID,CalisanTC,CalisanAdi,CalisanSoyadi,Baslama_tarihi)
Values('40218277382','4','2536455600','ayþe','hayriye','2023-01-15')
Insert Into Calisanlar(YoneticiTC,OtelID,CalisanTC,CalisanAdi,CalisanSoyadi,Baslama_tarihi)
Values('40218277382','5','22336655400','humeyra','öztürk','2023-01-15')
Insert Into Calisanlar(YoneticiTC,OtelID,CalisanTC,CalisanAdi,CalisanSoyadi,Baslama_tarihi)
Values('2536455600','7','99663355200','merve','baðýþlar','2023-01-15')








Insert Into Tesisler(TesisID,Restoran,Cafe,Spor_Salonu)
Values('1','PeramaRes','Perama Cafe','PeramaSS')
Insert Into Tesisler(TesisID,Restoran,Cafe,Spor_Salonu)
Values('2','GrandRes','Grand Cafe','GrandSS ')
Insert Into Tesisler(TesisID,Restoran,Cafe,Spor_Salonu)
Values('3','PalasRes','Palas Cafe','PalasSS ')
Insert Into Tesisler(TesisID,Restoran,Cafe,Spor_Salonu)
Values('4','Asya2Res','Asya2 Cafe','Asya2SS ')
Insert Into Tesisler(TesisID,Restoran,Cafe,Spor_Salonu)
Values('5','Ayselrestoran','aysel Cafe','ayselss ')
Insert Into Tesisler(TesisID,Restoran,Cafe,Spor_Salonu)
Values('9','kuþRestoran','ada Cafe','adaSS ')
Insert Into Tesisler(TesisID,Restoran,Cafe,Spor_Salonu)
Values('7','konyaaltýRes','konyaaltý Cafe','antalyaSS ')
Insert Into Tesisler(TesisID,Restoran,Cafe,Spor_Salonu)
Values('8','KaradenizRes','karadeniz Cafe','karadenizSS')


Insert Into Kullanim(KullanimSuresi,TesisID,MusteriTC)
Values('02:30:00','1','11111111111')
Insert Into Kullanim(KullanimSuresi,TesisID,MusteriTC)
Values('01:45:00','2','25364455600')
Insert Into Kullanim(KullanimSuresi,TesisID,MusteriTC)
Values('00:30:00','3','6984455800')
Insert Into Kullanim(KullanimSuresi,TesisID,MusteriTC)
Values('02:50:00','4','78264455600')

Insert Into Konaklama(MusteriTC,OdaNo,Giris,Ayrilma,Ucret)
Values('11111111111','115','2023-03-10','2023-03-15','50')
Insert Into Konaklama(MusteriTC,OdaNo,Giris,Ayrilma,Ucret)
Values('25364455600','116','2023-08-03','2023-08-05','300')
Insert Into Konaklama(MusteriTC,OdaNo,Giris,Ayrilma,Ucret)
Values('6984455800','52','2023-11-17','2023-11-20','400')
Insert Into Konaklama(MusteriTC,OdaNo,Giris,Ayrilma,Ucret)
Values('78264455600','1025','2023-02-10','2023-02-18','500')
Insert Into Konaklama(MusteriTC,OdaNo,Giris,Ayrilma,Ucret)
Values('8541796518','63','2023-02-10','2023-02-18','250')

--YÖNETÝCÝ ÝDSÝ 1 OLAN ÇYÖNETÝCÝNÝN YÖNETTÝÐÝ ÇALIÞANLARIN ADI VE ÇALIÞTIKLARI OTELERÝN ADLARI
--select CalisanAdi,OtelAdi from Calisanlar,Oteller where YoneticiID=1 and Calisanlar.OtelID=Oteller.OtelID
----YÖNETÝCÝ LÝSTESÝ
--select CalisanAdi,CalisanSoyadi,CalisanTC,Baslama_tarihi from Calisanlar where YoneticiID=CalisanID
-----ÇALIÞAN LÝSTESÝ
--select CalisanAdi,CalisanSoyadi,CalisanTC,Baslama_tarihi from Calisanlar where YoneticiID!=CalisanID



--HAngi müþteri hangi odada kalýyor
Select Musteri.MusteriTC,Odalar.OdaNo,Musteri.AD
From Konaklama ,Musteri,Odalar
Where Konaklama.MusteriTC=Musteri.MusteriTC And Konaklama.OdaNo=Odalar.OdaNo 

--Beyza atay hangi odada kalýyor
Select Musteri.AD AS MüþteriAdi, Musteri.SOYAD As MusteriSoyadi,Odalar.OdaNo
From Konaklama,Musteri,Odalar
Where  Konaklama.MusteriTC=Musteri.MusteriTC And Konaklama.OdaNo=Odalar.OdaNo And Musteri.Ad='Beyza' And Musteri.SOYAD='Atay'

--Beyza Atay hangi tesisi kullandý
Select DISTINCT  Musteri.Ad,Musteri.SOYAD,Tesisler.TesisID
From Kullanim,Musteri,Tesisler
Where Tesisler.TesisID=Kullanim.TesisID and Musteri.MusteriTC=Kullanim.MusteriTC and Musteri.AD='Beyza ' and Musteri.Soyad='Atay'

----4 nolu otelin yöneticisinin adý
--SELECT Yonetici.YoneticiAdi
--FROM Yonetici
--INNER JOIN Calisanlar ON Calisanlar.CalisanID = Yonetici.YoneticiID
--WHERE Calisanlar.OtelID = '4';

--Oda ücreti 100 ve 200 tl arasýnda olan otelleri sýrala
Select Odalar.Fiyat,Oteller.OtelAdi
From Odalar,Oteller
Where Oteller.OtelID=Odalar.OtelID and Odalar.Fiyat  between 100 and 200

--Müþteri ismi b ile baþlayan müþterileri sýrala
Select Musteri.AD
From Musteri
Where Musteri.AD Like 'b%'

--Oda fiyatlarýný artan sýralamaya göre sýrala
Select Odalar.Fiyat,Oteller.OtelAdi
From Odalar,Oteller
Where Odalar.OtelId=Oteller.OtelId
Order by Odalar.Fiyat Asc

--Oda fiyatlarýný azalan sýralamaya göre sýrala
Select Odalar.Fiyat,Oteller.OtelAdi
From Odalar,Oteller
Where Odalar.OtelId=Oteller.OtelId
Order by Odalar.Fiyat Desc

--Hangi müþteri adýndan kaç tane var
Select Musteri.AD, Count(*)
From Musteri
Group by Musteri.AD


----Trigger-------
delete 
from Musteri
where MusteriTC='25364455600'


--Musteri tcsi 8541796518 olan kiþiyi konaklamadan sil
Delete
From Konaklama
Where Konaklama.MusteriTC='21312323'

--Tesis kullaným süresi 01:30:00 saat olan müþterileri listele
select distinct Kullanim.TesisID,Kullanim.MusteriTC,Musteri.AD
From Kullanim,Musteri,Tesisler
WHERE Tesisler.TesisID=Kullanim.TesisID And Musteri.MusteriTC=Kullanim.MusteriTC And Kullanim.KullanimSuresi<'01:30:00'

----1 numaralý oteldeki tesisleri listele
--Select Oteller.OtelID,Tesisler.Cafe,Tesisler.Restoran,Tesisler.Spor_Salonu
--From Tesisler
--Inner Join Oteller On  Tesisler.OtelID = Oteller.OtelID
--WHERE Oteller.OtelID = '1';

--SELECT Tesisler.*
--FROM Tesisler
--JOIN Oteller ON Tesisler.OtelID = Oteller.OtelID
--WHERE Oteller.OtelID = '1';

--Musteri tcsi 6984455800 olan kiþinin ayrýlma tarihini deðiþtir
Update Calisanlar
Set Baslama_tarihi='08-08-2023'
Where CalisanTC='40216533824'



Update Oteller
Set OtelAdi='Kus Adasi Sunset Paradise'
Where OtelID='9'

--Odalarýn doluluk oranýný listele
SELECT OdaNo, DolulukOrani
FROM Odalar;

--Otel Id si 4 olan oteldeki odalarýn fiyatlarýnýn toplamý
SELECT SUM(Fiyat) AS ToplamFiyat
FROM Odalar
WHERE OtelID = '4';


----------------------------------------TRÝGGERS----------------------------------------------

CREATE TRIGGER YeniMüsteri
  ON Musteri
  AFTER INSERT
  AS
  BEGIN
    DECLARE @MusteriTC VARCHAR(50);
    SET @MusteriTC = (SELECT MusteriTC FROM inserted);
    PRINT 'Yeni müþteri eklendi: MüþteriTC: ' + @MusteriTC + '.';
END;



CREATE TRIGGER MüsteriSil
ON Musteri
AFTER DELETE
AS
BEGIN
    DECLARE @DeletedMusteriTC VARCHAR(50);
    SET @DeletedMusteriTC = (SELECT MusteriTC FROM deleted);
    PRINT 'Müþteri silindi: MüþteriTC: ' + @DeletedMusteriTC + '.';
END;

CREATE TRIGGER ÝseBaslamaTarihGuncelle
ON Calisanlar
AFTER UPDATE
AS
BEGIN
    IF UPDATE(Baslama_tarihi)
    BEGIN
        DECLARE CalisanTC VARCHAR(11);
        SET CalisanTC = (SELECT CalisanTC FROM inserted);
        DECLARE @NewStartDate DATETIME;
        SET @NewStartDate = (SELECT Baslama_tarihi FROM inserted);
        
        PRINT 'Çalýþanýn iþe baþlama tarihi güncellendi: CalisanTC: ' + CalisanTC + ', Yeni Baþlama Tarihi: ' + CONVERT(VARCHAR(20), @NewStartDate, 120) + '.';
    END;
END;


----------------------------------------VÝEWS----------------------------------------------

  CREATE VIEW HotelCalisan AS
  SELECT o.OtelID, o.OtelAdi, o.OtelAdres, o.OtelSiralama, 
  c.CalisanTC, c.CalisanAdi, c.CalisanSoyadi, c.Baslama_tarihi
  FROM Oteller o
  JOIN Calisanlar c ON o.OtelID = c.OtelID;


  CREATE VIEW MusteriKonaklamaBilgileriView AS
  SELECT m.MusteriTC, m.AD, m.SOYAD, m.ADRES, m.TELEFON,
  k.Giris, k.Ayrilma, k.Ucret, k.OdaNo
  FROM Musteri m
  JOIN Konaklama k ON m.MusteriTC = k.MusteriTC;


  CREATE VIEW MusteriTesisKullanýmBilgileri AS
  SELECT k.MusteriTC, t.Restoran, t.Cafe, t.Spor_Salonu, k.KullanimSuresi
  FROM Kullanim k
  JOIN Tesisler t ON k.TesisID = t.TesisID;


  CREATE VIEW KonaklamaOdaBilgileri AS
  SELECT m.MusteriTC, m.AD, m.SOYAD, m.ADRES, m.TELEFON,
  k.Giris, k.Ayrilma, k.Ucret, k.OdaNo,
  o.OdaTuru, o.Fiyat, o.DolulukOrani
  FROM Musteri m
  JOIN Konaklama k ON m.MusteriTC = k.MusteriTC
  JOIN Odalar o ON k.OdaNo = o.OdaNo;


  

