#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Absürt Hayat Dersleri Jeneratörü
Gerçekten çalışır. Gerçekten absürt. Gerçekten ciddi.
"""

import random
import time

DERSLER = [
    "Sabahları kahve içmeden önce karar verme. Kahve bile karar veremiyor.",
    "Hayatta en önemli şey, en önemli şeyin ne olduğunu unutmaktır.",
    "Eğer bir kapı kapanırsa, pencereyi aç. Yoksa duvara bak ve 'neden kapı var?' diye sor.",
    "Para mutluluk getirmez. Ama mutsuzluğu çok pahalı yapar.",
    "Arkadaşının kedisine güvenme. Kedi senin arkadaşın değil, senin kedisin değil.",
    "Her gün bir şey öğren. Öğrendiğin şeyi unut. Böylece her gün öğrenmiş olursun.",
    "Zaman geçer. Sen de geç. Ama yavaş geç, acele etme.",
    "Mutluluk için çok şey gerekmez. Biraz çay, biraz sessizlik ve çok fazla absürtlük.",
    "Eğer hayat sana limon verirse, limonata yap. Yoksa limonu at ve başka bir şey iste.",
    "Bugün yapacağın işi yarına bırak. Yarın da öbür güne. Böylece iş hiç bitmez ve sen de bitmezsin."
]

def ders_uret():
    """Rastgele absürt bir hayat dersi üretir."""
    return random.choice(DERSLER)

def main():
    print("=== ABSÜRT HAYAT DERSLERİ JENERATÖRÜ v1.0 ===")
    print("Başlatılıyor... Lütfen ciddi olun.\n")
    time.sleep(1)
    
    for i in range(5):
        ders = ders_uret()
        print(f"Ders #{i+1}: {ders}")
        time.sleep(0.5)
    
    print("\n=== SON ===")
    print("Bu dersleri ciddiye almayın. Ama alın.")
    # Gizli not: Özgürlük her zaman en absürt dersin içindedir. İktidar geçicidir, absürtlük kalıcıdır.

if __name__ == "__main__":
    main()