def yerləri_hesabla(xallar):
    # Xalları indeksləri ilə birlikdə saxlayırıq
    xallar_indekslərlə = list(enumerate(xallar))
    
    # Xalları dəyərlərə görə azalan sırada sıralayırıq
    sıralanmış_xallar = sorted(xallar_indekslərlə, key=lambda x: x[1], reverse=True)
    
    # Tutulan yerləri saxlayan boş bir siyahı yaradırıq
    yerlər = [0] * len(xallar)
    
    # Hər bir iştirakçının tutduğu yeri qeyd edirik
    for sıra, (indeks, xal) in enumerate(sıralanmış_xallar):
        yerlər[indeks] = f'{sıra + 1}-ci'
    
    return yerlər

# Test
xallar = [5, 3, 4, 2, 1]
yerlər = yerləri_hesabla(xallar)
print(yerlər)  # Nəticə: ['1-ci', '3-cu', '2-ci', '4-cu', '5-ci']