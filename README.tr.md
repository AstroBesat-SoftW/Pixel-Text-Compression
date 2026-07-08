<div align="center">

# 🖼️ Pixel-to-Text Sıkıştırma Motoru
### Piksel verisini herhangi bir sıkıştırma kütüphanesi kullanmadan metne dönüştüren özgün bir görüntü sıkıştırma sistemi.

[🇬🇧 Read in English](README.md) · **🇹🇷 Türkçe**

</div>

---

## 📌 Bu proje nedir?

Bu proje, standart bir JPEG/PNG görselini **sıfırdan geliştirilmiş bir algoritma** ile düz bir **metin dosyasına** dönüştüren ve ardından bu metinden görseli yeniden oluşturabilen deneysel bir sıkıştırma sistemidir. Süreç boyunca hiçbir hazır sıkıştırma kütüphanesi (zlib, PNG codec'leri, hazır LZW paketleri vb.) kullanılmamıştır.

Amaç basit ama iddialıydı: **bir piksel matrisi metin olarak temsil edilip orijinal sıkıştırılmış görsele yakın bir boyuta indirilebilir mi, sonra tekrar görsele dönüştürülebilir mi?**

Cevap evet — dört aşamalı, giderek daha akıllı hale gelen bir kodlama süreciyle.

## 🧠 Nasıl çalışıyor? (genel bakış)

Süreç aşamalı olarak ilerler. Her aşama, bir öncekinin çıktısını alıp daha da küçültür.

| Aşama | Teknik | Mantık |
|---|---|---|
| 1 | **Izgara Ortalaması** | Görsel bir ızgaraya (grid) bölünür; her blok tek bir ortalama gri tonlama değerine (0–255) indirgenir ve görsel bir sayı matrisine dönüşür. |
| 1.5 | **Aralık Küçültme** | 0–255 aralığındaki gri ton değerleri 0–25 aralığına ölçeklenir, böylece her değer çok daha az karakterle ifade edilir. |
| 2 | **Özel RLE (Run-Length Encoding)** | Yan yana tekrar eden değerler (gökyüzü, duvar gibi düz alanlarda sık görülür) `adet + değer` biçiminde sıkıştırılır. |
| 3 | **Alfasayısal Eşleme** | Küçültülmüş 0–25 değerleri tek harflere (`A`–`Z`) eşlenerek karakter sayısı bir kez daha yarıya iner. |
| 4 | **Sözlük Tabanlı Sıkıştırma (LZW mantığı)** | Lempel-Ziv-Welch mantığına benzer bir sözlük katmanı, harf dizisindeki tekrar eden desenleri bulup tek bir Unicode sembolüne dönüştürür. |
| 5 | **Yeniden Oluşturma (Reconstruction)** | Tüm süreç tersine işletilir: sembol → harf → tekrar sayısı → gri ton matrisi → görsel; bloklar tuval üzerine yeniden çizilir. |

### 📉 Sonuçlar

| Adım | Dosya Boyutu |
|---|---|
| Orijinal `.jpg` | **13 KB** |
| 1. Aşama — ham ızgara değerleri | 210 KB |
| 1.5 Aşama — aralık küçültme | 118 KB |
| 2. Aşama — RLE sıkıştırma | 99 KB |
| 3. Aşama — alfasayısal eşleme | 46 KB |
| 4. Aşama — sözlük tabanlı sıkıştırma | **~16 KB** 🚀 |

210 KB'lık ara temsilden başlayan süreç, birden fazla noktada tamamen insan tarafından okunabilir bir metin formatından geçerek orijinal JPEG boyutuna sadece birkaç KB kala bir sonuca ulaşıyor.

## 🖼️ Önce & Sonra

<table>
<tr>
<td align="center"><b>Orijinal</b></td>
<td align="center"><b>Metin tabanlı sıkıştırmadan yeniden oluşturulan</b></td>
</tr>
<tr>
<td><img src="assets/original.jpg" width="300"/></td>
<td><img src="assets/reconstructed.jpg" width="300"/></td>
</tr>
</table>

Yeniden oluşturulan görsel kasıtlı olarak gri tonlama ve blok bazlı kalitede — projenin amacı kayıpsız bir sıkıştırma değil, bir piksel matrisinin metin tabanlı bir hattan geçip hala tanınabilir şekilde geri gelebildiğini kanıtlamak.

## 📄 Detaylı anlatım

Her optimizasyon adımının arkasındaki mantığı, ara çıktıları ve ekran görüntülerini içeren detaylı teknik anlatım PDF olarak eklenmiştir:

📎 [`docs/Pixel-Text-Compression-Whitepaper.pdf`](docs/Pixel-Text-Compression-Whitepaper.pdf)

## 💻 Kod

Bu repoda her aşamanın mantığını takip edebilmeniz için **örnek/kısmi kod parçaları** bulunmaktadır. Bunlar bilinçli olarak sadeleştirilmiş/kısaltılmıştır — bu kişisel bir Ar-Ge projesidir ve tam çalışan implementasyon özel tutulmaktadır.

- [`src/01_grid_analysis.py`](src/01_grid_analysis.py) — blok ortalama mantığı
- [`src/02_rle_pass.py`](src/02_rle_pass.py) — RLE mantığı
- [`src/03_alpha_mapping.py`](src/03_alpha_mapping.py) — sayı → harf eşleme mantığı
- [`src/04_lzw_layer.py`](src/04_lzw_layer.py) — sözlük tabanlı sıkıştırma mantığı

## 🚧 Durum

Bu bir üretim seviyesinde sıkıştırma kütüphanesi değil, aktif bir deneydir. Bilinen sınırlamalar:

- Şu an için sadece gri tonlama destekleniyor (renk kanalı henüz yok)
- Blok bazlı kalite kaybı kasıtlı ve ızgara boyutuyla ayarlanabilir
- Standart codec'lerle (JPEG/PNG/WebP) sistematik bir kıyaslama yapılmadı — 13 KB karşılaştırması tek bir test görseline dayanıyor

## ⭐ Beğendiyseniz

Bu proje kişisel bir merak sonucu başladı — fikri beğendiyseniz bir yıldız daha fazla kişiye ulaşmasını sağlar ve projeyi geliştirmeye (renk desteği, adaptif ızgara boyutu, daha iyi sözlük sıkıştırması vb.) devam etmem için motive eder.

## 📜 Lisans

Bkz. [LICENSE](LICENSE).
