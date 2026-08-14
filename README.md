# Basic System Dashboard

Windows masaüstünde CPU ve RAM kullanımını küçük, sürekli üstte kalan bir widget olarak gösteren basit sistem izleme uygulaması.

## Windows için doğrudan çalıştırma

Python kurmak istemiyorsanız repository içindeki aşağıdaki dosyayı indirip çalıştırabilirsiniz:

`release/SystemResourceWidget.exe`

Bu `.exe` dosyası GitHub Actions tarafından Windows üzerinde otomatik olarak oluşturulur ve kaynak kod güncellendiğinde yeniden derlenir.

> Not: Proje kişisel olarak imzalanmış bir Windows kod imzalama sertifikasına sahip değildir. Bu nedenle Windows SmartScreen ilk çalıştırmada "Bilinmeyen yayıncı" uyarısı gösterebilir.

## Özellikler

- CPU kullanım yüzdesi
- RAM kullanım yüzdesi
- Kullanılan / toplam RAM miktarı
- 1 saniyede bir otomatik güncelleme
- Çerçevesiz ve her zaman üstte pencere
- Fareyle sürükleyerek taşıma

## Kaynak koddan çalıştırma

Geliştiriciler için kaynak kod da repository içinde tutulmaktadır.

```powershell
python -m pip install -r requirements.txt
python main.py
```

## Otomatik Windows build

`.github/workflows/build-windows-exe.yml` workflow'u Windows runner üzerinde PyInstaller kullanarak `SystemResourceWidget.exe` üretir. Oluşan dosya hem GitHub Actions artifact'ı olarak saklanır hem de `release/SystemResourceWidget.exe` yoluna commit edilir.

## Lisans

MIT
