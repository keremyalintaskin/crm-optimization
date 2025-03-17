# Müşteri ve Pazarlama Optimizasyon Algoritmaları

Bu repo, müşteri hizmetleri temsilcisi atama ve pazarlama kampanyası optimizasyonu için geliştirilen algoritmaları içermektedir. Bu algoritmalar, şirketlerin kaynaklarını en verimli şekilde kullanmalarına yardımcı olmak amacıyla tasarlanmıştır.

## İçerik

- [Genel Bakış](#genel-bakış)
- [Algoritmalar](#algoritmalar)
  - [Müşteri Temsilcisi Atama](#müşteri-temsilcisi-atama)
  - [Pazarlama Kampanyası Optimizasyonu](#pazarlama-kampanyası-optimizasyonu)
- [Kullanım](#kullanım)
- [Gereksinimler](#gereksinimler)
- [Örnekler](#örnekler)

## Genel Bakış

Bu proje, işletmelerin iki temel sorununa çözüm sunmaktadır:

1. **Müşteri Temsilcisi Atama Problemi**: Müşterilerin lokasyon bazlı olarak en uygun müşteri hizmetleri temsilcilerine atanması.
2. **Pazarlama Kampanyası Optimizasyonu**: Sınırlı bir bütçe ile en yüksek getiriyi sağlayacak pazarlama kampanyalarının seçimi.

Her iki algoritma da dinamik programlama yaklaşımını kullanarak optimal çözümler sunmaktadır.

## Algoritmalar

### Müşteri Temsilcisi Atama

Bu algoritma, müşterileri coğrafi konumlarına göre uygun müşteri temsilcilerine atar. Algoritma şu şekilde çalışır:

- Her müşteri için, aynı konumda bulunan ve kapasitesi olan temsilciler arasından en yüksek kapasiteli olanı seçilir.
- Bir temsilci atandığında, temsilcinin kapasitesi bir azaltılır.
- Eğer uygun bir temsilci bulunamazsa, müşteri atamasız kalır.

```python
def musteri_temsilci_atama(musteriler, temsilciler):
    # Algoritma kodu
```

### Pazarlama Kampanyası Optimizasyonu

Bu algoritma, klasik "Knapsack Problem" (Sırt Çantası Problemi) çözümünü kullanarak belirli bir bütçe içinde en yüksek getiriyi sağlayacak pazarlama kampanyalarını seçer:

- Her kampanyanın bir maliyeti ve beklenen getirisi vardır.
- Algoritma, belirli bir bütçe kısıtlaması altında toplam getiriyi maksimize eden kampanya kombinasyonunu bulur.
- Dinamik programlama yaklaşımı, tüm olası kombinasyonları değerlendirmek yerine optimizasyon yapar.

```python
def pazarlama_kampanya_secimi(butce, kampanyalar):
    # Algoritma kodu
```

## Kullanım

Kodu kullanmak için aşağıdaki adımları izleyin:

1. Repo'yu klonlayın: `git clone https://github.com/kullaniciadi/repo-adi.git`
2. Gerekli bağımlılıkları yükleyin: `pip install numpy`
3. Kendi veri setinizle örnek kullanımı inceleyin:

```python
import numpy as np
from optimizasyon import musteri_temsilci_atama, pazarlama_kampanya_secimi

# Örnek müşteri ve temsilci verisi
musteriler = [(1, 'Istanbul', 5), (2, 'Ankara', 3), (3, 'Istanbul', 2)]
temsilciler = [(101, 'Istanbul', 2), (102, 'Ankara', 1)]

# Müşteri temsilcisi atama fonksiyonunu çağır
atamalar = musteri_temsilci_atama(musteriler, temsilciler)
print("Müşteri Temsilcisi Atama:", atamalar)

# Örnek pazarlama kampanyaları verisi: (maliyet, getiri)
kampanyalar = [(50, 100), (20, 60), (30, 90)]
butce = 50

# Pazarlama kampanyası seçimi fonksiyonunu çağır
max_getiri, secilen_kampanyalar = pazarlama_kampanya_secimi(butce, kampanyalar)
print("En iyi pazarlama getirisi:", max_getiri)
print("Seçilen kampanyalar:", secilen_kampanyalar)
```

## Gereksinimler

- Python 3.6+
- NumPy

## Örnekler

### Müşteri Temsilcisi Atama Örneği

Verilen örnek için:
- Müşteri 1 (İstanbul): Temsilci 101'e atanır
- Müşteri 2 (Ankara): Temsilci 102'ye atanır
- Müşteri 3 (İstanbul): Temsilci 101'e atanır, ancak temsilcinin kapasitesi tükendiği için atama başarısız olur

### Pazarlama Kampanyası Örneği

50 birimlik bir bütçe ile şu kampanyalar arasından seçim yapılır:
- Kampanya 1: Maliyet 50, Getiri 100
- Kampanya 2: Maliyet 20, Getiri 60
- Kampanya 3: Maliyet 30, Getiri 90

Optimal çözüm:
- Kampanya 2 ve 3 seçilir (Toplam maliyet: 50, Toplam getiri: 150)
