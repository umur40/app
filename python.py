# Hesap Makinesi Uygulaması
def hesap_makinesi():
    print("Basit Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    
    secim = input("İşlem seçin (1-4): ")
    sayi1 = float(input("İlk sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    
    if secim == '1':
        print(f"Sonuç: {sayi1 + sayi2}")
    elif secim == '2':
        print(f"Sonuç: {sayi1 - sayi2}")
    elif secim == '3':
        print(f"Sonuç: {sayi1 * sayi2}")
    elif secim == '4':
        if sayi2 != 0:
            print(f"Sonuç: {sayi1 / sayi2}")
        else:
            print("Sıfıra bölünemez!")

# Not Hesaplama Uygulaması
def not_hesapla():
    vize = float(input("Vize notunu girin: "))
    final = float(input("Final notunu girin: "))
    ortalama = (vize * 0.4) + (final * 0.6)
    
    print(f"Ortalamanız: {ortalama}")
    if ortalama >= 50 and final >= 50:
        print("Tebrikler, dersi geçtiniz!")
    else:
        print("Üzgünüm, dersten kaldınız.")

# Sayı Tahmin Oyunu
def sayi_tahmin():
    import random
    hedef = random.randint(1, 100)
    tahmin_hakki = 5
    
    print("1-100 arası bir sayı tuttum!")
    
    while tahmin_hakki > 0:
        tahmin = int(input(f"Tahmininiz (kalan hak: {tahmin_hakki}): "))
        
        if tahmin == hedef:
            print("Tebrikler, bildiniz!")
            return
        elif tahmin < hedef:
            print("Daha yüksek bir sayı söyleyin.")
        else:
            print("Daha düşük bir sayı söyleyin.")
        
        tahmin_hakki -= 1
    
    print(f"Oyun bitti! Tuttuğum sayı: {hedef}")

# Ana menü
while True:
    print("\nUygulamalar:")
    print("1. Hesap Makinesi")
    print("2. Not Hesaplama")
    print("3. Sayı Tahmin Oyunu")
    print("4. Çıkış")
    
    secim = input("Hangi uygulamayı çalıştırmak istersiniz? (1-4): ")
    
    if secim == '1':
        hesap_makinesi()
    elif secim == '2':
        not_hesapla()
    elif secim == '3':
        sayi_tahmin()
    elif secim == '4':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")
1
