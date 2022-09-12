egitim = open("egitim.txt", mode = 'w')

gorselSayisi = 10#burda etiketleme yapılmış resim sayısı olur 
kosulBir = gorselSayisi*(8/10)+1
egitimSayac = 1
while(egitimSayac<kosulBir):
    egitim.write(f"veri_seti/resimler/{egitimSayac}.jpg\n" )
    #veri_seti/resimler yerine görsellerin bulunduğu konum gelir
    #örneğin resimler dataset'in içinde gorseller klasöeünde olsun dataset/gorseller/
    #direkt dosya yolunu c:/user... şeklinde yazmak daha sağlıklı
    egitimSayac=egitimSayac+1
egitim.close() 

#------------------------------------------------------------------------------

test = open("test.txt", mode = 'w')

while(egitimSayac<gorselSayisi+1):
    test.write(f"veri_seti/resimler/{egitimSayac}.jpg\n" )
    egitimSayac=egitimSayac+1
test.close() 