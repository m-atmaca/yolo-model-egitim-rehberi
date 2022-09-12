# darkneti hazırlama
<pre>	
darknet'i github'dan indir<br>
darkneti indirdikten sonra Makefile dosyasını açıp:<br>
	gpu=1<br>
	cudnn=1<br>
	opencv=1 konumuna getirilir<br>
sonra alttaki linklerdeki 2 dosya indirilir<br>
- https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137<br>
- https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights<br>
<br>
<br>
darknetin içindeki cfg klasöründen yolov4.cfg dosyasını darknetin içine çıkarılır<br>
burada yapılan işlemleri koyacağım cfg klasöründe açıkladım<br>
- cfg dosyasını açıp subdivision 8'den 64 yapılır<br>
- width ve height 416 yapılır<br>
- max_batches=2000 ama bunu araştır<br>
- yine aynı bloktaki steps max_batches'in %80-%90 arası bir değer alır<br>
- classes'ların eğitilecek sınıf sayısı kadar olacak şekilde düzenle<br>
- classes'ların hemen üst bloğunda bulunan filters'ları classes'ların 5 fazlasının 3 katı olarak düzenle [filters=(classes+5)*3]<br>
- bu klasörü başka bir adla kaydedip kapatabiliriz.(örn: demoYolov4.cfg)<br>




</pre>

# veri setini hazırlama<br>
</pre>
-darknetin olduğu dizinde klasör aç(darknetin içinde değil) (örneğin adı veri_seti klasörü olsun)<br>
-veri_seti klasörünün içinde bir klasör daha açılıp klasöre görseller koyulur (bunun da adı resimler olsun)<br>
-resimler klasörüne toplanan görseller koyulur (1 2 3 şeklinde kaydet)<br>
-görsellerin hepsi jpg türünde olmalı (ekleyeceğim python koduyla hızlıca yapılabilir: topJPG.py)<br>
-https://www.makesense.ai/ sitesiyle etiketleme yap <br>
-etiketleme bittikten sonra action->export annotations girerek zip yolo formatında indirilir<br>
-veri seti klasörünün içinde yeni bir klasör oluştur(örn: adı etiketler olsun)<br>
-etiketlerin olduğu txt dosyalarını etiketler ve resimler klasörlerine kopyalanır<br>
-veri_seti klasöründe eğitim ve test olmak üzere 2 tane txt oluşturulur<br>
-eğitim txt dosyasına görsellerin %80'inin adresi satır satır yazılır<br>
-test klasörüne ise kalan %20 görselin adresi satır satır yazılır.<br>
-ekleyeceğim kodla hızlıca ve kolayca yapabilirsiniz: txtIslemleri.py  (görsel sayısını girmeyi unutmayın. küsüratlı sayıda görselde sıkıntı çıkabilir mümkünse %80'i tam sayı olsun)<br>
<br>
-bir txt dosyası daha açarak etiketin adını gireriz bunu da .name şeklinde kaydet (orn: sinif.name)<br>
-bir txt dosyası daha açarak veri.data koyalım ve aşağıdaki parametreleri girelim<br>
	veri.data: <br>
		classes = sınıf sayısı<br>
		train = eğitim txt adresi<br>
		valid = test txt adresi<br>
		names = name klasörü adresi<br>
		backup = weight dosyasının kaydolacağı yer<br>

bu işlemler bittikten sonra veri_seti klasörünü kesip veya kopyalayıp darknet klasörünün içine atılır. (bu klasör direkt darknetin içinde de oluşturulup tüm işlemler içeride de yapılabilir).<br>





</pre>

# eğitim
<pre>
collab'dan eğitim için:<br>
darknet dosyasını drive yüklüyoruz<br>
yeni notebook açın veya ekleyeceğim notebook'u collaba ekleyin<br>
notebook'la drive bağlantısı kurun<br>
drive'da yeni klasör oluşturup onun içinde backup klasörü oluşturun, eğitim sürecindeki ağırlık dosyaları buraya kaydolur.<br>
sonra notebook satırlarını gpu'da çalıştırın<br>
kodlardaki dosya yollarını kendi klasör adlarına göre ayarlamayı unutmayın. bundan kaynaklı hata verebilir.  <br>
<br>
yerel eğitim için:<br>
daha bu kısmı öğrenmedim :)<br>
öğrenince devamı gelecek
</pre>
