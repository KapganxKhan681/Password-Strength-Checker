# 🔐 Password Strength Checker / Parola Gücü Kontrol Programı

## 🌍 English
A Python-based security automation tool designed to evaluate password strength against standard cryptographic guidelines (NIST). The application implements robust input validation, character property analysis using string manipulation, and recursive loop structures to provide a continuous user experience.

### 🚀 Technical Features
* **Granular Character Analysis:** Inspects length, uppercase, lowercase, digits, and explicit special character matrices.
* **Input Validation (Robustness):** Traps invalid control characters during the exit decision loop, preventing script exceptions.
* **State Management:** Employs boolean flags that dynamically reset on each iteration within a `while` loop structure.
* **Dual-Language Infrastructure:** Fully documented with bilingual comments (EN/TR) for cross-team code readability.

### 💻 How to Run
```bash
python password_checker.py
```

---

## 🇹🇷 Türkçe
Standart kriptografik kılavuzlara (NIST) uygun olarak parola gücünü değerlendirmek için tasarlanmış Python tabanlı bir Micro-Güvenlik otomasyon aracıdır. Uygulama; kesintisiz bir kullanıcı deneyimi sunmak adına sağlam girdi doğrulama, string manipülasyonu ile karakter analizi ve döngü yapıları içerir.

### 🚀 Teknik Özellikler
* **Kapsamlı Karakter Analizi:** Uzunluk, büyük harf, küçük harf, rakam ve özel karakter matrislerini denetler.
* **Girdi Doğrulama (Dayanıklılık):** Çıkış karar döngüsü sırasında geçersiz kontrol karakterlerini yakalayarak script'in çökmesini engeller.
* **Durum Yönetimi:** `while` döngüsü yapısı içinde her yinelemede dinamik olarak sıfırlanan boolean bayraklar kullanır.
* **Çift Dilli Altyapı:** Takımlar arası kod okunabilirliği için tamamen çift dilli (EN/TR) yorum satırlarıyla belgelenmiştir.

### 💻 Nasıl Çalıştırılır
```bash
python password_checker.py
```
