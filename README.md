# Yapay Zeka Destekli Kitap ve Özelliklerini Sorgulama Uygulaması
## Proje İçeriği
Bu proje, Python ve LLM kullanarak web scraping (web kazıma) işlemi gerçekleştiren bir uygulamanın geliştirilmesi hakkında bilgi vermektedir. Bu uygulama, belirli kitap alışveriş sitelerinden kitap ürün verilerini kazıyarak kullanıcılar için  erişilebilir ve sorgulayabilmelerine uygun hale getirmektedir.
## Proje Tanımı
Proje, Python dilini ve uygun bir web kazıma kütüphanesini kullanarak, belirlenen kitap alışveriş sitelerindeki ürünlerin bilgilerini toplamaktadır. Kazınan veriler MongoDB veritabanı yönetim sistemi kullanılarak depolanmaktadır. Temel görevler şunlardır:

1. Belirli bir ürün kategorisindeki tüm kitapların bilgilerini kazıma
2. Kazılan verileri MongoDB veritabanında saklama

Ekstra Görevler:
1. Uygulama kapatıldığında kaldığı yerden devam etmektedir
2. LLM kullanarak kullanıcıların istedikleri sorguyu yapabilmelerine olanak tanınmıştır.

# Gereksinimler
Python 3>
Scrapy web kazıma kütüphanesi
MongoDB veritabanı
Streamlit kütüphanesi
Langchain kütüphanesi
## Kurulum ve Çalıştırma
1. Proje dosyalarını bilgisayarınıza indirin veya klonlayın.
2. Gerekli Python kütüphanelerini yükleyin.
3. MongoDB veritabanınızı kurun ve yapılandırın.
4. settings.py,kitapyurdu.py ve kitapsepeti.py dosyasını düzenleyerek MongoDB bağlantı bilgilerinizi girin.
5. Uygulamayı başlatmak için aşağıdaki komutu kullanın:
    scrapy  crawl kitapyurdu
    scrapy crawl kitapsepeti
6. Uygulama, belirtilen kitap alışveriş sitelerinden veri kazımaya başlayacaktır. Kazınan veriler MongoDB veritabanında saklanacaktır.
7. Daha sonra aşağıda ki komutu kullanarak uygulamayı çalıştırın:
   streamlit run app.py
8. Artık kullanıcılar sorgu atıp, merak ettikleri bilgilere çok rahat bir şekilde erişecektir.
## Dizin Açıklamaları
spiders/: Web kazıma işlemini gerçekleştiren Spider sınıflarının bulunduğu dizin.
pipelines.py: Kazınan verilerin işlendiği ve MongoDB'ye kaydedildiği işlemlerin yapıldığı pipeline.
settings.py: Proje ayarlarının yapılandırıldığı dosya.
app.py: Kullanıcı etkileşimli uygulamının gerçekleştirildiği dosya
## Örnek Çıktılar
![1](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/69ad3200-7b8e-470b-a13e-9d4ce0d81c6f)

![2](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/770352e1-e56a-4b67-8fd1-8fa37ed55625)
![3](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/c5bc5590-7378-4a92-aeb2-84c014175681)

## MongoDB Çıktıları
![kk](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/a61a6cea-f117-4f2c-9d94-2bb1f262ae46)

![kkk](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/b62d9b00-0817-42fb-b7b0-40750078d53c)

