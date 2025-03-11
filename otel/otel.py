import random
from datetime import datetime

from flask import Flask, render_template, request, url_for, redirect
import pyodbc

app= Flask(__name__)
conn = pyodbc.connect('Driver={SQL Server};Server=LAPTOP-servername\SQLEXPRESS;Database=otelrezervasyon;Trusted_Connection=True')



@app.route("/")
def Index():
    return render_template('index.html')


@app.route("/views")
def views():
    cursor = conn.cursor()
    sql_query1 = "SELECT * FROM HotelCalisan"
    cursor.execute(sql_query1)
    hotelcalisan = cursor.fetchall()
    cursor.close()

    cursor = conn.cursor()
    sql_query1 = "SELECT * FROM MusteriKonaklamaBilgileriView"
    cursor.execute(sql_query1)
    musterikonaklama = cursor.fetchall()
    cursor.close()

    cursor = conn.cursor()
    sql_query1 = "SELECT * FROM MusteriTesisKullanımBilgileri"
    cursor.execute(sql_query1)
    musteritesis = cursor.fetchall()
    cursor.close()

    return render_template('Views.html',hotelcalisan=hotelcalisan,musterikonaklama=musterikonaklama,musteritesis=musteritesis)

@app.route("/triggers")
def triggers():
    return render_template('Triggers.html')

@app.route("/musteri")
def MusteriEkleme():

    return render_template('MusteriEkleme.html')

@app.route("/musteri_ekle",methods=['POST'])
def MusteriEkle():
  try:
    cursor = conn.cursor()
    # Örnek kullanıcı verileri
    MusteriTC = request.form['MusteriTC']
    AD = request.form['AD']
    SOYAD = request.form['SOYAD']
    ADRES = request.form['ADRES']
    TELEFON = request.form['TELEFON']

    # SQL sorgusu
    sql_query = "INSERT INTO Musteri (MusteriTC, AD,SOYAD,ADRES,TELEFON) VALUES (?, ?,?,?,?)"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, (MusteriTC, AD,SOYAD,ADRES,TELEFON))
    # Değişiklikleri kaydet
    conn.commit()

    cursor=conn.cursor()
    cursor.execute('SELECT * FROM Oteller')
    oteller = cursor.fetchall()
    cursor.close()

    return render_template('Rezervasyon.html',oteller=oteller,MusteriTC=MusteriTC)
  except pyodbc.IntegrityError as e:
      # Duplicate hatası olduğunda
      return 'Hata: Bu kullanıcı zaten var.'
  except Exception as e:
      # Diğer hataları yakala
      return 'Hata oluştu: {}'.format(str(e))

@app.route("/Giris")
def GirisSayfa():

    return render_template("Giris.html")


@app.route("/musterigiris",methods=['POST'])
def Giris():
 try:
    MusteriTC = request.form['MusteriTC']
    if not MusteriTC:
        raise ValueError("Boş input gönderemezsiniz.")
    cursor = conn.cursor()
    sql_query='SELECT * FROM Musteri WHERE MusteriTC=?'

    cursor.execute(sql_query,(MusteriTC,))
    musteri = cursor.fetchall()
    cursor.close()
    if not musteri:
        raise ValueError("Sistemde böyle bir müşteri yok.")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Oteller')
    oteller = cursor.fetchall()
    cursor.close()

    return render_template('Rezervasyon2.html',oteller=oteller,MusteriTC=musteri)
 except ValueError as e:
   return 'Hata oluştu: {}'.format(str(e))


@app.route("/Panel")
def Panel():

    return render_template('Panel.html')

@app.route("/Konaklamalar")
def Konaklamalar():
    cursor = conn.cursor()
    sql_query1 = "SELECT * FROM Konaklama"
    cursor.execute(sql_query1)
    konaklamalar = cursor.fetchall()
    cursor.close()

    return render_template('Konaklamalar.html', konaklamalar=konaklamalar)

@app.route("/Calisanlar")
def Calisanlar():
    cursor = conn.cursor()
    sql_query1 = "SELECT CalisanAdi,CalisanSoyadi,CalisanTC,Baslama_tarihi,Calisanlar.OtelID FROM Calisanlar WHERE YoneticiTC!=CalisanTC"
    cursor.execute(sql_query1)
    calisanlar = cursor.fetchall()
    cursor.close()

    cursor = conn.cursor()
    sql_query2 = "select CalisanTC,CalisanAdi,Oteller.OtelID from Calisanlar,Oteller where YoneticiTC=CalisanTC and Oteller.OtelID=Calisanlar.OtelID"
    cursor.execute(sql_query2)
    calisanlar2 = cursor.fetchall()
    cursor.close()

    cursor = conn.cursor()
    sql_query3 = "select Oteller.OtelID,Oteller.OtelAdi from Oteller"
    cursor.execute(sql_query3)
    oteller = cursor.fetchall()
    cursor.close()

    cursor = conn.cursor()
    sql_query1 = "SELECT YoneticiTC,CalisanAdi,Calisanlar.OtelID,Oteller.OtelAdi FROM Calisanlar,Oteller where YoneticiTC=CalisanTC and Calisanlar.OtelID=Oteller.OtelID"
    cursor.execute(sql_query1)
    yoneticiler = cursor.fetchall()
    cursor.close()

    return render_template('Calisanlar.html' , calisanlar=calisanlar,calisanlar2=calisanlar2,oteller=oteller,yoneticiler=yoneticiler)

@app.route("/Kullanimlar")
def Kullanimlar():
    cursor = conn.cursor()
    sql_query1 = "SELECT * FROM Kullanim"
    cursor.execute(sql_query1)
    kullanimlar = cursor.fetchall()
    cursor.close()

    return render_template('Kullanimlar.html', kullanimlar=kullanimlar)

@app.route("/Musteriler")
def Musteriler():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Musteri')
    users = cursor.fetchall()
    cursor.close()

    # HTML şablonuna verileri aktarma
    return render_template('Musteriler.html', users=users)

@app.route("/Odalar")
def Odalar():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Odalar')
    odalar = cursor.fetchall()
    cursor.close()

    # HTML şablonuna verileri aktarma
    return render_template('Odalar.html', odalar=odalar)

    return render_template('Odalar.html')

@app.route("/Oteller")
def Oteller():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Oteller')
    oteller = cursor.fetchall()
    cursor.close()

    # HTML şablonuna verileri aktarma
    return render_template('Oteller.html', oteller=oteller)

    return render_template('Oteller.html')

@app.route("/Tesisler")
def Tesisler():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Tesisler')
    tesisler = cursor.fetchall()
    cursor.close()

    # HTML şablonuna verileri aktarma
    return render_template('Tesisler.html', tesisler=tesisler)


@app.route("/Yoneticiler")
def Yoneticiler():
    cursor = conn.cursor()
    cursor.execute('select CalisanAdi,CalisanSoyadi,CalisanTC,Baslama_tarihi,Calisanlar.OtelID from Calisanlar where YoneticiTC=CalisanTC')
    yoneticiler = cursor.fetchall()
    cursor.close()

    cursor = conn.cursor()
    sql_query2 = "select Oteller.OtelID,OtelAdi from Oteller"
    cursor.execute(sql_query2)
    oteller = cursor.fetchall()
    cursor.close()

    # HTML şablonuna verileri aktarma
    return render_template('Yoneticiler.html', yoneticiler=yoneticiler,oteller=oteller)





@app.route("/odasec",methods=['POST'])
def OdaSec():
    MusteriTC=request.form['MusteriTC']
    option = request.form['option']
    cursor = conn.cursor()
    sql_query="SELECT * FROM Odalar WHERE OtelID=? AND DolulukOrani=?"
    cursor.execute(sql_query, (option,0,))
    odalar = cursor.fetchall()
    cursor.close()

    # HTML şablonuna verileri aktarma
    return render_template('OdaSec.html', odalar=odalar,MusteriTC=MusteriTC,otelId=option)

@app.route("/konaklama",methods=['POST'])
def KonaklamaSec():
  try:
    option = request.form['option']
    otelId= request.form['otelId']
    MusteriTC = request.form['MusteriTC']



    cursor=conn.cursor()
    sql_query1="SELECT * FROM Odalar WHERE OdaNo=?"
    cursor.execute(sql_query1, (option,))
    oda = cursor.fetchall()
    cursor.close()

    return render_template('Konaklama.html', oda=oda, MusteriTC=MusteriTC, otelId=otelId)

  except Exception as e:
      # Diğer hataları yakala
    return 'Hata oluştu: {}'.format(str(e))









@app.route("/tesis",methods=['POST'])
def TesisSec():
 try:
    OtelID=request.form['OtelID'].strip()
    MusteriTC = request.form['MusteriTC'].strip()
    OdaNo = request.form['OdaNo'].strip()
    Giris = request.form['Giris'].strip()
    Ayrilma = request.form['Ayrilma'].strip()
    Ucret = int(request.form['Ucret'].strip())

    if not OdaNo:
        raise ValueError("Otelimizde boş oda bulunamamıştır.Anlayışınız için teşekkürler.")
    if not Giris or not Ayrilma:
        raise ValueError("Lütfen giriş ve çıkış tarihlerinizi seçiniz!")




    result = process_dates(Giris,Ayrilma,Ucret)

    cursor = conn.cursor()
    sql_query = "INSERT INTO Konaklama (MusteriTC, OdaNo,Giris,Ayrilma,Ucret) VALUES (?, ?,?,?,?)"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, (MusteriTC, OdaNo, Giris, Ayrilma, result))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    cursor=conn.cursor()
    sql_query3="UPDATE Odalar SET DolulukOrani=1 WHERE OdaNo=?"
    cursor.execute(sql_query3, (OdaNo,))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    cursor = conn.cursor()
    sql_query1 = "SELECT TesisID,Spor_Salonu,Cafe,Restoran FROM Tesisler,Oteller WHERE Tesisler.TesisID=Oteller.OtelID AND Oteller.OtelID=?"
    cursor.execute(sql_query1, (OtelID,))
    tesisler = cursor.fetchall()
    cursor.close()

    cursor = conn.cursor()
    sql_query1 = "SELECT OtelAdi FROM Oteller Where OtelID=?"
    cursor.execute(sql_query1, (OtelID,))
    otelAdi = cursor.fetchall()[0][0]
    cursor.close()


    return render_template('Tesis.html',MusteriTC=MusteriTC,tesisler=tesisler,OtelID=OtelID,otelAdi=otelAdi)

 except Exception as e:
   return 'Hata oluştu: {}'.format(str(e))



def process_dates(date1,date2,ucret):
    date1_obj = datetime.strptime(date1, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2, '%Y-%m-%d')

    # Tarihler arasındaki farkı hesapla
    date_diff = (date2_obj - date1_obj).days

    # Farkı bir ücretle çarp ve sonucu döndür
    fee_per_day = ucret  # Günlük ücret
    result = date_diff * fee_per_day

    return result


@app.route("/tesisayar",methods=['POST'])
def TesisAyar():
    OtelID = request.form['OtelID'].strip()
    TesisID= request.form['options'].strip()
    MusteriTC=request.form['MusteriTC'].strip()
    KullanimSuresi = request.form['KullanimSuresi'].strip()

    cursor = conn.cursor()
    sql_query = "INSERT INTO Kullanim (MusteriTC, TesisID,KullanimSuresi) VALUES (?, ?,?)"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, (MusteriTC, TesisID, KullanimSuresi))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()




    return render_template("Rezerve.html")



@app.route("/otel")
def OtelEkleme():
    return render_template("OtelEkleme.html")

@app.route("/otel_ekle",methods=['POST'])
def OtelEkle():
    try:
        cursor = conn.cursor()
        # Örnek kullanıcı verileri
        OtelID = request.form['OtelID']
        OtelAdi = request.form['OtelAdi']
        OtelAdres = request.form['OtelAdres']
        OtelSiralama = request.form['OtelSiralama']

        # SQL sorgusu
        sql_query = "INSERT INTO Oteller (OtelID, OtelAdi,OtelAdres,OtelSiralama) VALUES (?, ?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (OtelID, OtelAdi, OtelAdres, OtelSiralama))
        # Değişiklikleri kaydet
        conn.commit()
        return "otel eklendi."
    except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: Bu otel zaten var.'
    except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))

@app.route("/oda")
def OdaEkleme():
    return render_template("OdaEkleme.html")

@app.route("/oda_ekle",methods=['POST'])
def OdaEkle():
    try:
        cursor = conn.cursor()
        # Örnek kullanıcı verileri
        OdaNo = request.form['OdaNo']
        Fiyat = request.form['Fiyat']
        DolulukOrani = request.form['DolulukOrani']
        OdaTuru = request.form['OdaTuru']
        OtelID = request.form['OtelID']

        # SQL sorgusu
        sql_query = "INSERT INTO Odalar (OdaNo, Fiyat,DolulukOrani,OdaTuru,OtelID) VALUES (?, ?,?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (OdaNo, Fiyat, DolulukOrani, OdaTuru,OtelID))
        # Değişiklikleri kaydet
        conn.commit()
        return "oda eklendi."
    except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: Bu oda zaten var.'
    except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))
@app.route("/calisan_ekle")
def CalisanEkle():
    try:
        cursor = conn.cursor()
        # Örnek kullanıcı verileri
        CalisanID = '112'
        OtelID = '1112'
        CalisanAdi = 'Aliko'
        CalisanSoyadi = 'öztürk'
        Baslama_tarihi= '2023-04-11 10:15:00'

        # SQL sorgusu
        sql_query = "INSERT INTO Calisanlar (CalisanID, OtelID,CalisanAdi,CalisanSoyadi,Baslama_tarihi) VALUES (?, ?,?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (CalisanID, OtelID, CalisanAdi, CalisanSoyadi,Baslama_tarihi))
        # Değişiklikleri kaydet
        conn.commit()
        return "çalışan eklendi."
    except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: Bu çalışan zaten var.'
    except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))

###################KULLANIMLAR#########################

@app.route('/insertkullanimlar', methods=['POST'])
def insertkullanimlar():
 try:

    MusteriTC = request.form['MusteriTC']
    TesisID = request.form['TesisID']
    KullanimSuresi = request.form['KullanimSuresi']

    cursor=conn.cursor()
    # SQL sorgusu
    sql_query = "INSERT INTO Kullanim (MusteriTC, TesisID,KullanimSuresi) VALUES (?,?,?)"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, (MusteriTC, TesisID, KullanimSuresi))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Kullanimlar'))
 except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: otel sisteminde böyle bir müşteri veya tesis olmadığından işleminiz gerçekleşemedi..'
 except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))

@app.route('/updatekullanimlar', methods=['POST'])
def updatekullanimlar():

    KullanimSuresi = request.form['KullanimSuresi']
    MusteriTC = request.form['MusteriTC']
    TesisID=request.form['TesisID']

    cursor=conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("UPDATE Kullanim SET KullanimSuresi = ? WHERE TesisID = ? AND MusteriTC=?", (KullanimSuresi,TesisID,MusteriTC))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Kullanimlar'))


@app.route('/deletekullanimlar', methods=['POST'])
def deletekullanimlar():
    MusteriTC = request.form['MusteriTC']
    TesisID = request.form['TesisID']


    cursor = conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("DELETE FROM Kullanim WHERE TesisID = ? AND MusteriTC=?",(TesisID, MusteriTC))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Kullanimlar'))


################MUSTERİLER##########################


@app.route('/insertmusteriler', methods=['POST'])
def insertmusteriler():
    try:
        cursor = conn.cursor()
        # Örnek kullanıcı verileri
        MusteriTC = request.form['MusteriTC']
        AD = request.form['AD']
        SOYAD = request.form['SOYAD']
        ADRES = request.form['ADRES']
        TELEFON = request.form['TELEFON']

        # SQL sorgusu
        sql_query = "INSERT INTO Musteri (MusteriTC, AD,SOYAD,ADRES,TELEFON) VALUES (?, ?,?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (MusteriTC, AD, SOYAD, ADRES, TELEFON))
        # Değişiklikleri kaydet
        conn.commit()

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Oteller')
        oteller = cursor.fetchall()
        cursor.close()

        return redirect(url_for('Musteriler'))
    except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: Bu kullanıcı zaten var.'
    except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))


@app.route('/updatemusteriler', methods=['POST'])
def updatemusteriler():
    cursor = conn.cursor()
    # Örnek kullanıcı verileri
    MusteriTC = request.form['MusteriTC']
    AD = request.form['AD']
    SOYAD = request.form['SOYAD']
    ADRES = request.form['ADRES']
    TELEFON = request.form['TELEFON']

    # SQL sorgusu
    sql_query = "UPDATE Musteri SET AD=?,SOYAD=?,ADRES=?,TELEFON=? WHERE MusteriTC=?"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, ( AD, SOYAD, ADRES, TELEFON,MusteriTC,))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Musteriler'))


@app.route('/deletemusteriler', methods=['POST'])
def deletemusteriler():
    MusteriTC = request.form['MusteriTC']


    cursor = conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("DELETE FROM Musteri WHERE MusteriTC=?",(MusteriTC))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Musteriler'))


#############################ODALAR####################################

@app.route('/insertodalar', methods=['POST'])
def insertodalar():
    try:
        cursor = conn.cursor()
        # Örnek kullanıcı verileri
        OdaNo = request.form['OdaNo']
        OtelID = request.form['OtelID']
        Fiyat = request.form['Fiyat']
        OdaTuru = request.form['OdaTuru']
        DolulukOrani = 0

        # SQL sorgusu
        sql_query = "INSERT INTO Odalar (OdaNo, OtelID,Fiyat,OdaTuru,DolulukOrani) VALUES (?, ?,?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (OdaNo, OtelID, Fiyat, OdaTuru, DolulukOrani))
        # Değişiklikleri kaydet
        conn.commit()




        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Odalar')
        tesisler = cursor.fetchall()
        cursor.close()

        return redirect(url_for('Odalar'))
    except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: Böyle oda zaten var.'
    except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))


@app.route('/updateodalar', methods=['POST'])
def updateodalar():

    # Örnek kullanıcı verileri
    OdaNo = request.form['OdaNo']
    OtelID = request.form['OtelID']
    Fiyat = request.form['Fiyat']
    OdaTuru = request.form['OdaTuru']
    DolulukOrani = request.form['DolulukOrani']
    cursor = conn.cursor()
    # SQL sorgusu
    sql_query = "UPDATE Odalar SET Fiyat=?,OdaTuru=?,DolulukOrani=? WHERE OdaNo=? AND OtelID=?"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, ( Fiyat, OdaTuru, DolulukOrani, OdaNo,OtelID,))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    #cursor = conn.cursor()

    #sql_query = "INSERT INTO Konaklama (MusteriTC, OdaNo,Giris,Ayrilma,Ucret) VALUES (?, ?,?,?,?)"

    #cursor.execute(sql_query, (MusteriTC, OdaNo, Giris, Ayrilma, Ucret))

    #conn.commit()
    #cursor.close()



    return redirect(url_for('Odalar'))


@app.route('/deleteodalar', methods=['POST'])
def deleteodalar():
    OdaNo = request.form['OdaNo']
    OtelID = request.form['OtelID']

    cursor = conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("DELETE FROM Odalar WHERE OdaNo=? AND OtelID=?",(OdaNo,OtelID))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Odalar'))


#####################Oteller###############################


@app.route('/insertoteller', methods=['POST'])
def insertoteller():
    try:
        cursor = conn.cursor()
        # Örnek kullanıcı verileri
        OtelID = request.form['OtelID']
        OtelAdi = request.form['OtelAdi']
        OtelAdres = request.form['OtelAdres']
        OtelSiralama = request.form['OtelSiralama']

        # SQL sorgusu
        sql_query = "INSERT INTO Oteller (OtelID, OtelAdi,OtelAdres,OtelSiralama) VALUES (?, ?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (OtelID, OtelAdi, OtelAdres, OtelSiralama))
        # Değişiklikleri kaydet
        conn.commit()

        cursor.close()

        return redirect(url_for('Oteller'))
    except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: Bu otel zaten var.'
    except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))


@app.route('/updateoteller', methods=['POST'])
def updateoteller():
    cursor = conn.cursor()

    OtelID = request.form['OtelID']
    OtelAdi = request.form['OtelAdi']
    OtelAdres = request.form['OtelAdres']
    OtelSiralama = request.form['OtelSiralama']

    # SQL sorgusu
    sql_query = "UPDATE Oteller SET OtelAdi=?,OtelAdres=?,OtelSiralama=? WHERE OtelID=?"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, ( OtelAdi, OtelAdres, OtelSiralama,OtelID,))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Oteller'))


@app.route('/deleteoteller', methods=['POST'])
def deleteoteller():

    OtelID = request.form['OtelID']

    cursor = conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("DELETE FROM Oteller WHERE OtelID=?",(OtelID))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Oteller'))

####################KONAKLAMALAR############################

@app.route('/insertkonaklamalar', methods=['POST'])
def insertkonaklamalar():
    try:

        # Örnek kullanıcı verileri
        MusteriTC = request.form['MusteriTC']
        OdaNo = request.form['OdaNo']
        Giris = request.form['Giris']
        Ayrilma = request.form['Ayrilma']
        Ucret = request.form['Ucret']

        cursor = conn.cursor()
        # SQL sorgusu
        sql_query = "INSERT INTO Konaklama (MusteriTC, OdaNo,Giris,Ayrilma,Ucret) VALUES (?, ?,?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (MusteriTC, OdaNo, Giris, Ayrilma,Ucret))
        # Değişiklikleri kaydet
        conn.commit()
        cursor.close()

        cursor = conn.cursor()
        # SQL sorgusu
        sql_query1 = "UPDATE Odalar SET DolulukOrani=? WHERE OdaNo=?"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query1, (1,OdaNo))
        # Değişiklikleri kaydet
        conn.commit()
        cursor.close()


        return redirect(url_for('Konaklamalar'))
    except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: Bu konaklama zaten var.'
    except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))


@app.route('/updatekonaklamalar', methods=['POST'])
def updatekonaklamalar():
    cursor = conn.cursor()

    MusteriTC = request.form['MusteriTC']
    OdaNo = request.form['OdaNo']
    Giris = request.form['Giris']
    Ayrilma = request.form['Ayrilma']
    Ucret = request.form['Ucret']

    # SQL sorgusu
    sql_query = "UPDATE Konaklama SET OdaNo=?,Giris=?,Ayrilma=?,Ucret=? WHERE MusteriTC=?"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, ( OdaNo, Giris, Ayrilma,Ucret,MusteriTC))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Konaklamalar'))


@app.route('/deletekonaklamalar', methods=['POST'])
def deletekonaklamalar():

    MusteriTC = request.form['MusteriTC']
    OdaNo = request.form['OdaNo']


    cursor = conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("DELETE FROM Konaklama WHERE OdaNo=? AND MusteriTC=?",(OdaNo,MusteriTC))
    # Değişiklikleri kaydet
    conn.commit()

    cursor.close()
    cursor = conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("UPDATE Odalar SET DolulukOrani=? WHERE OdaNo=?", (0,OdaNo))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Konaklamalar'))

################################CALİSANLAR#############################

@app.route('/insertcalisanlar', methods=['POST'])
def insertcalisanlar():


        # Örnek kullanıcı verileri
        OtelID = str(request.form['OtelID'].strip())
        CalisanTC = request.form['CalisanTC'].strip()
        CalisanAdi = request.form['CalisanAdi'].strip()
        CalisanSoyadi = request.form['CalisanSoyadi'].strip()
        Baslama_tarihi = request.form['Baslama_tarihi'].strip()


        cursor = conn.cursor()
        sql_query1 = "SELECT YoneticiTC FROM Calisanlar where OtelID=?"
        cursor.execute(sql_query1,(OtelID))
        YoneticiTC = cursor.fetchall()
        cursor.close()




        cursor = conn.cursor()
        # SQL sorgusu
        sql_query = "INSERT INTO Calisanlar (YoneticiTC,OtelID,CalisanTC,CalisanAdi,CalisanSoyadi,Baslama_tarihi) VALUES (?, ?,?,?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (YoneticiTC[0][0],OtelID,CalisanTC, CalisanAdi,CalisanSoyadi,Baslama_tarihi))
        # Değişiklikleri kaydet
        conn.commit()
        cursor.close()




        return redirect(url_for('Calisanlar'))


@app.route('/updatecalisanlar', methods=['POST'])
def updatecalisanlar():

    OtelID = str(request.form['OtelID']).strip()
    CalisanTC = request.form['CalisanTC'].strip()
    CalisanAdi = request.form['CalisanAdi'].strip()
    CalisanSoyadi = request.form['CalisanSoyadi'].strip()
    Baslama_tarihi = request.form['Baslama_tarihi'].strip()




    cursor = conn.cursor()
    # SQL sorgusu
    sql_query = "UPDATE Calisanlar SET OtelID=?,CalisanAdi=?,CalisanSoyadi=?,Baslama_tarihi=? WHERE CalisanTC=?"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, ( OtelID,CalisanAdi,CalisanSoyadi,Baslama_tarihi,CalisanTC))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Calisanlar'))


@app.route('/deletecalisanlar', methods=['POST'])
def deletecalisanlar():

    CalisanTC = request.form['CalisanTC']


    cursor = conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("DELETE FROM Calisanlar WHERE CalisanTC=?",(CalisanTC))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Calisanlar'))

########################YÖNETİCİLER#####################################

@app.route('/insertyoneticiler', methods=['POST'])
def insertyoneticiler():
    try:
        cursor = conn.cursor()
        # Örnek kullanıcı verileri

        OtelID = request.form['OtelID']
        CalisanTC = request.form['CalisanTC']
        CalisanAdi = request.form['CalisanAdi']
        CalisanSoyadi = request.form['CalisanSoyadi']
        Baslama_tarihi = request.form['Baslama_tarihi']



        # SQL sorgusu
        sql_query = "INSERT INTO Calisanlar (OtelID,YoneticiTC, CalisanTC,CalisanAdi,CalisanSoyadi,Baslama_tarihi) VALUES (?, ?,?,?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (OtelID,CalisanTC, CalisanTC, CalisanAdi, CalisanSoyadi,Baslama_tarihi))
        # Değişiklikleri kaydet
        conn.commit()

        cursor.close()

        return redirect(url_for('Yoneticiler'))
    except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: Bu yönetici zaten var.'
    except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))


@app.route('/updateyoneticiler', methods=['POST'])
def updateyoneticiler():
    cursor = conn.cursor()

    OtelID = request.form['OtelID']
    CalisanTC = request.form['CalisanTC']
    CalisanAdi = request.form['CalisanAdi']
    CalisanSoyadi = request.form['CalisanSoyadi']
    Baslama_tarihi = request.form['Baslama_tarihi']

    # SQL sorgusu
    sql_query = "UPDATE Calisanlar SET OtelID=?,CalisanAdi=?,CalisanSoyadi=?,Baslama_tarihi=? WHERE CalisanTC=?"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, (OtelID,CalisanAdi, CalisanSoyadi, Baslama_tarihi,CalisanTC))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Yoneticiler'))


@app.route('/deleteyoneticiler', methods=['POST'])
def deleteyoneticiler():
    YoneticiTC = request.form['YoneticiTC']

    cursor = conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("DELETE FROM Yonetici WHERE YoneticiTC=?", (YoneticiTC))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Yoneticiler'))


################################TESİSLER########################################


@app.route('/inserttesisler', methods=['POST'])
def inserttesisler():
    try:
        cursor = conn.cursor()
        # Örnek kullanıcı verileri

        TesisID = request.form['TesisID']
        Spor_Salonu = request.form['Spor_Salonu']
        Cafe = request.form['Cafe']
        Restoran = request.form['Restoran']

        # SQL sorgusu
        sql_query = "INSERT INTO Tesisler (TesisID,Spor_Salonu,Cafe,Restoran) VALUES (?, ?,?,?)"
        # Parametrelerle birlikte sorguyu çalıştırma
        cursor.execute(sql_query, (TesisID,Spor_Salonu,Cafe,Restoran))
        # Değişiklikleri kaydet
        conn.commit()

        cursor.close()

        return redirect(url_for('Tesisler'))
    except pyodbc.IntegrityError as e:
        # Duplicate hatası olduğunda
        return 'Hata: Bu tesis zaten var.'
    except Exception as e:
        # Diğer hataları yakala
        return 'Hata oluştu: {}'.format(str(e))


@app.route('/updatetesisler', methods=['POST'])
def updatetesisler():
    cursor = conn.cursor()

    TesisID = request.form['TesisID']
    Spor_Salonu = request.form['Spor_Salonu']
    Cafe = request.form['Cafe']
    Restoran = request.form['Restoran']

    # SQL sorgusu
    sql_query = "UPDATE Tesisler SET Spor_Salonu=?,Cafe=?,Restoran=? WHERE TesisID=?"
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute(sql_query, (Spor_Salonu, Cafe, Restoran,TesisID))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Tesisler'))


@app.route('/deletetesisler', methods=['POST'])
def deletetesisler():
    TesisID = request.form['TesisID']

    cursor = conn.cursor()
    # Parametrelerle birlikte sorguyu çalıştırma
    cursor.execute("DELETE FROM Tesisler WHERE TesisID=?", (TesisID))
    # Değişiklikleri kaydet
    conn.commit()
    cursor.close()

    return redirect(url_for('Tesisler'))


if __name__ == "__main__":
    app.run(debug=True)
