# AlgoritmaAnaliziveTasarimi
# Kruskal Algoritması Görselleştirici (PyQt5)

Bu proje, **Kruskal algoritmasını** kullanarak bir grafın **Minimum Örtücü Ağacı (MST)**'nı adım adım oluşturan ve süreci **görsel olarak animasyonla** gösteren bir uygulamadır.

## ✨ Özellikler

- PyQt5 arayüzü ile etkileşimli kullanıcı deneyimi
- 1000+ düğüm ve 3000+ kenarlık grafik desteği
- Kruskal algoritmasının doğru ve verimli uygulanışı
- `Union-Find` veri yapısı ile döngü kontrolü
- Adım adım kenar çizimi ve animasyon
- Daire veya grid yerleşim düzeni seçimi
- Çizim hızı kontrolü (slider ile)
- Başlat/Durdur ve Sıfırla seçenekleri

## 📸 Arayüz

- **Düğüm ve Kenar Sayısı Girişi**  
- **Düzen Seçimi:** Daire veya Grid  
- **Hız Ayarı:** Kenar çizim hızı (ms)  
- **Bilgi Kutusu:** İşlem durumu, MST tamamlandı mesajı

## 🧠 Kullanılan Algoritmalar

- **Kruskal Algoritması**  
  Graf kenarlarını ağırlıklarına göre sıralar, `Union-Find` yapısı ile döngü oluşturmayacak şekilde en küçük ağırlıklı kenarları seçerek MST'yi oluşturur.

## 🛠 Kurulum

Python 3.7+ yüklü olmalıdır.

pip install PyQt5

## Kullanım

python main.py


Açılan arayüzde:

Düğüm ve kenar sayılarını girin.

Düzen seçin (Daire/Grid).

"Graf Oluştur" ile grafiği oluşturun.

"Başlat" ile adım adım çizimi izleyin.

"Durdur" veya "Sıfırla" ile işlemi kontrol edin.
