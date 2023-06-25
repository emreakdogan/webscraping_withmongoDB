# Yapay Zeka Destekli Kitap ve Özelliklerini Sorgulama Uygulaması
## Proje İçeriği
Bu proje SmartMaple Task görevi için , Python ve LLM kullanarak web scraping (web kazıma) işlemi gerçekleştiren bir uygulamanın geliştirilmesi hakkında bilgi vermektedir. Bu uygulama, belirli kitap alışveriş sitelerinden kitap ürün verilerini kazıyarak kullanıcılar için  erişilebilir ve sorgulayabilmelerine uygun hale getirmektedir.
## Proje Tanımı
Proje, Python dilini ve uygun bir web kazıma kütüphanesini kullanarak, belirlenen kitap alışveriş sitelerindeki ürünlerin bilgilerini toplamaktadır. Kazınan veriler MongoDB veritabanı yönetim sistemi kullanılarak depolanmaktadır. Temel görevler şunlardır:

1. Belirli bir ürün kategorisindeki tüm kitapların bilgilerini kazıma
2. Kazılan verileri MongoDB veritabanında saklama

Ekstra Görevler:
1. Uygulama kapatıldığında kaldığı yerden devam etmektedir
2. LLM kullanarak kullanıcıların istedikleri sorguyu yapabilmelerine olanak tanınmıştır.

# Gereksinimler
1. Python 3>
2. Scrapy web kazıma kütüphanesi
3. MongoDB veritabanı
4. Streamlit kütüphanesi
5. Langchain kütüphanesi
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
1. spiders/: Web kazıma işlemini gerçekleştiren Spider sınıflarının bulunduğu dizin.
2. pipelines.py: Kazınan verilerin işlendiği ve MongoDB'ye kaydedildiği işlemlerin yapıldığı pipeline.
3. settings.py: Proje ayarlarının yapılandırıldığı dosya.
4. app.py: Kullanıcı etkileşimli uygulamının gerçekleştirildiği dosya
## Örnek Çıktılar
![1](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/a8dd0b9a-b328-47a3-b45a-bf5100845ef0)
![2](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/05187bf1-723d-42fb-a69e-aaa737fe2295)
![3](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/f179e1c7-e546-4790-9dee-86e004ed3629)


## MongoDB Çıktıları
![kk](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/9708ea12-be84-4c85-85ea-6e6e60703355)

![kkk](https://github.com/emreakdogan/webscraping_withmongoDB/assets/95315841/4f56a443-9c36-4be1-bc3b-6d8d22aff2d8)
