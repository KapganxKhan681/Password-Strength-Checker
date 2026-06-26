# --- STEP 1: Start the main infinite loop for continuous testing ---
# --- ADIM 1: Kesintisiz test için ana sonsuz döngüyü başlatıyoruz ---
while True:

    # Get the password input from the user
    # Kullanıcıdan test edilecek parola girdisini alıyoruz
    password = input("Please enter a password to test: ")
    

    # Initialize/Reset boolean flags for each new password evaluation
    # Her yeni parola değerlendirmesi için kontrol bayraklarını tanımlıyor/sıfırlıyoruz
    has_length = False
    has_upper = False 
    has_lower = False
    has_digit = False 
    has_special = False 


    # Defined list of special characters for security policy compliance
    # Güvenlik politikasına uygunluk için özel karakter listesini tanımlıyoruz
    special_characters = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|"


    # Check the minimum length requirement (NIST Standard: >= 8 characters)
    # Minimum uzunluk şartını kontrol ediyoruz (NIST Standardı: >= 8 karakter)
    if len(password) >= 8 :
        has_length = True


    # --- STEP 2: Loop through each character to analyze properties ---
    # --- ADIM 2: Özellikleri analiz etmek için her karakteri döngüyle geziyoruz ---
    for char in password:
        if char.isupper():
            has_upper = True
    
        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True
    
        elif char in special_characters:
            has_special = True


    # --- STEP 3: Calculate the final security score ---
    # --- ADIM 3: Nihai güvenlik skorunu hesaplıyoruz ---
    score = 0
    if has_length: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1


    # Determine the strength status text based on the total score
    # Toplam skora göre güç durumu metnini belirliyoruz
    if score == 5:
        strength = "Your password is very strong. / Parolan çok güçlü."

    elif score == 4:
        strength = "Your password is strong. / Parolan güçlü."

    elif score == 3:
        strength = "Your password is medium. / Paralon orta zorlukta."

    else:
        strength = "Your password is weak. / Parolan zayıf."


    # --- STEP 4: Generate and print the visual security report ---
    # --- ADIM 4: Görsel güvenlik raporunu oluşturup ekrana basıyoruz ---
    print("\n" + "="*30)
    print("🔐 PASSWORD SECURITY REPORT / PAROLA GÜVENLİK RAPORU")
    print("="*30)
    print(f"Total Score / Toplam Skor: {score}/5")
    print(f"Strength Status / Güç Durumu: {strength}")
    print("-"*30)


    # Print structural checklist results using conditional expressions
    # Koşullu ifadeler kullanarak yapısal kontrol listesi sonuçlarını basıyoruz
    print(f"1. At least 8 characters / En az 8 karakter: {'✅ PASSED' if has_length else '❌ FAILED'}")
    print(f"2. Uppercase letter / Büyük harf: {'✅ PASSED' if has_upper else '❌ FAILED'}")
    print(f"3. Lowercase letter / Küçük harf: {'✅ PASSED' if has_lower else '❌ FAILED'}")
    print(f"4. Number (Digit) / Rakam: {'✅ PASSED' if has_digit else '❌ FAILED'}")
    print(f"5. Special character / Özel karakter: {'✅ PASSED' if has_special else '❌ FAILED'}")
    print("="*30)


    # --- STEP 5: Input Validation Loop for replay/exit choice ---
    # --- ADIM 5: Tekrar deneme veya çıkış seçimi için Girdi Doğrulama Döngüsü ---
    should_exit = False

    while True:
        choice = input("\nDo you want to test another password? (Y/N) / Yeni bir parola denemek ister misiniz? (E/H): ").upper()


        # If choice is valid for continuation, break the inner loop
        # Seçim devam etmek için geçerliyse iç döngüyü kır
        if choice == 'Y' or choice == 'E':
            print("="*30)
            break
        

        # If choice is valid for exit, flag the shutdown and break the inner loop
        # Seçim çıkış için geçerliyse kapanışı işaretle ve iç döngüyü kır
        elif choice == 'N' or choice == 'H':
            print("\nExiting program... Goodbye! / Programdan çıkılıyor... Görüşürüz!")
            should_exit = True
            break
        

        # Trap invalid inputs and ask the question again without crashing
        # Geçersiz girdileri yakala ve çökmeden soruyu tekrar sor
        else:
            print("❌ Invalid choice! Please enter (Y/N) or (E/H).")
            print("❌ Geçersiz seçim! Lütfen (E/H) veya (Y/N) giriniz.")
    

    # If the exit flag is triggered, break the outer main loop to terminate the script
    # Eğer çıkış bayrağı tetiklendiyse, script'i sonlandırmak için dış ana döngüyü kır
    if should_exit:
        break



