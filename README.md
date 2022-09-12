<p># nesne-tespiti-icin-egitim-yonergesi
<br>
# darkneti hazırlama
darknet'i github'dan indir
darkneti indirdikten sonra Makefile dosyasını açıp:
	gpu=1
	cudnn=1
	opencv=1 konumuna getirilir
sonra alttaki linklerdeki 2 dosya indirilir
- https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137
- https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights


darknetin içindeki cfg klasöründen yolov4.cfg dosyasını darknetin içine çıkarılır
burada yapılan işlemleri koyacağım cfg klasöründe açıkladım
- cfg dosyasını açıp subdivision 8'den 64 yapılır
- width ve height 416 yapılır
- max_batches=2000 ama bunu araştır
- yine aynı bloktaki steps max_batches'in %80-%90 arası bir değer alır
- classes'ların eğitilecek sınıf sayısı kadar olacak şekilde düzenle
- classes'ların hemen üst bloğunda bulunan filters'ları classes'ların 5 fazlasının 3 katı olarak düzenle [filters=(classes+5)*3]
- bu klasörü başka bir adla kaydedip kapatabiliriz.(örn: demoYolov4.cfg)
 



# veri setini hazırlama
-darknetin olduğu dizinde klasör aç(darknetin içinde değil) (örneğin adı veri_seti klasörü olsun)
-veri_seti klasörünün içinde bir klasör daha açılıp klasöre görseller koyulur (bunun da adı resimler olsun)
-resimler klasörüne toplanan görseller koyulur (1 2 3 şeklinde kaydet)
-görsellerin hepsi jpg türünde olmalı (ekleyeceğim python koduyla hızlıca yapılabilir: topJPG.py)
-https://www.makesense.ai/ sitesiyle etiketleme yap 
-etiketleme bittikten sonra action->export annotations girerek zip yolo formatında indirilir
-veri seti klasörünün içinde yeni bir klasör oluştur(örn: adı etiketler olsun)
-etiketlerin olduğu txt dosyalarını etiketler ve resimler klasörlerine kopyalanır
-veri_seti klasöründe eğitim ve test olmak üzere 2 tane txt oluşturulur
-eğitim txt dosyasına görsellerin %80'inin adresi satır satır yazılır
-test klasörüne ise kalan %20 görselin adresi satır satır yazılır.
-ekleyeceğim kodla hızlıca ve kolayca yapabilirsiniz: txtIslemleri.py  (görsel sayısını girmeyi unutmayın. küsüratlı sayıda görselde sıkıntı çıkabilir mümkünse %80'i tam sayı olsun)

-bir txt dosyası daha açarak etiketin adını gireriz bunu da .name şeklinde kaydet (orn: sinif.name)
-bir txt dosyası daha açarak veri.data koyalım ve aşağıdaki parametreleri girelim
	veri.data: 
		classes = sınıf sayısı
		train = eğitim txt adresi
		valid = test txt adresi
		names = name klasörü adresi
		backup = weight dosyasının kaydolacağı yer

bu işlemler bittikten sonra veri_seti klasörünü kesip veya kopyalayıp darknet klasörünün içine atılır. (bu klasör direkt darknetin içinde de oluşturulup tüm işlemler içeride de yapılabilir).


# eğitim
collab'dan eğitim için:
darknet dosyasını drive yüklüyoruz
yeni notebook açın veya ekleyeceğim notebook'u collaba ekleyin
notebook'la drive bağlantısı kurun
drive'da yeni klasör oluşturup onun içinde backup klasörü oluşturun, eğitim sürecindeki ağırlık dosyaları buraya kaydolur.
sonra notebook satırlarını gpu'da çalıştırın
kodlardaki dosya yollarını kendi klasör adlarına göre ayarlamayı unutmayın. bundan kaynaklı hata verebilir.  

yerel eğitim için:
daha bu kısmı öğrenmedim :)
öğrenince devamı gelecek
<p>
