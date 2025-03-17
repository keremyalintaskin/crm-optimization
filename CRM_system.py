import numpy as np

def musteri_temsilci_atama(musteriler, temsilciler):
    dp = {}
    
    for m in musteriler:
        dp[m] = None
        en_iyi_eslesme = None
        for t in temsilciler:
            if t[1] == m[1] and t[2] > 0:
                if en_iyi_eslesme is None or t[2] > en_iyi_eslesme[2]:
                    en_iyi_eslesme = t
        
        if en_iyi_eslesme:
            dp[m] = en_iyi_eslesme[0]
            temsilciler[temsilciler.index(en_iyi_eslesme)] = (en_iyi_eslesme[0], en_iyi_eslesme[1], en_iyi_eslesme[2] - 1)
    
    return dp

def pazarlama_kampanya_secimi(butce, kampanyalar):
    n = len(kampanyalar)
    dp = np.zeros((n+1, butce+1))
    
    for i in range(1, n+1):
        maliyet, getiri = kampanyalar[i-1]
        for j in range(butce+1):
            if maliyet <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-maliyet] + getiri)
            else:
                dp[i][j] = dp[i-1][j]
    
    secilen_kampanyalar = []
    j = butce
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            secilen_kampanyalar.append(kampanyalar[i-1])
            j -= kampanyalar[i-1][0]
    
    return dp[n][butce], secilen_kampanyalar

musteriler = [(1, 'Istanbul', 5), (2, 'Ankara', 3), (3, 'Istanbul', 2)]
temsilciler = [(101, 'Istanbul', 2), (102, 'Ankara', 1)]
print("Müşteri Temsilcisi Atama:", musteri_temsilci_atama(musteriler, temsilciler))

kampanyalar = [(50, 100), (20, 60), (30, 90)]
butce = 50
print("En iyi pazarlama getirisi:", pazarlama_kampanya_secimi(butce, kampanyalar))
