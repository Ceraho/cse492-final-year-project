Projeyi çalıştırmak için:

1- "executables" dosyasından doğru işletim sistemine ait executable dosyasını çalıştırınız.
	Not: Eğer bu yöntemle tool'u çalıştırıyorsanız, dosya gezgini üzerinden çift tıkladıktan sonra birkaç saniye beklenmesi gerekebilir. Tek dosya formatında olmasından dolayı, dosyaların extract edilmesi ve tool'un açılması birkaç saniye alabiliyor.

2- sh le çalıştırmak için:
	2a- Öncelikle, sisteminizde Python 3.x.x kurulu olduğuna emin olunuz. (Terminalde Python --version veya Python3 --version komutları ile kontrol edilebilir.)
	2b- Sonrasında, projenin olduğu yerde bir terminal açıp, "sh runTool.sh" komutunu kullanarak projeyi çalıştırabilirsiniz.
	Not: sh komutunu Windows'ta kullanmak için sisteminizde WSL (Linux Sub-System for Windows) kurulması gerekebilir.


Kullanım:

UI içerisinde 3 tane path input alanı göreceksiniz. Path'ler için: 
1- "Input Dir Path" için, dönemlere ait Excel dosyalarının bulunduğu klasörü seçmeniz gerekmektedir. 
2- "Student IDs Path" için Öğrenci numaraları ve isimlerinin bulunduğu Excel dosyasının yerini seçmeniz gerekmektedir. 
3- "Output Dir Path" için de raporların çıkarılmasını istediğiniz klasörün yerini seçmeniz gerekmektedir.

Path'lerin seçiminden sonra, eğer geçmişten kalan ve incelemek istediğiniz bir rapor yoksa:
4- "Generate Report" Butonunu kullanarak genel raporu oluşturmanız gerekmektedir.
5- Generate Report işlemi bittikten sonra alttaki butonları aracılığı ile istediğiniz sorgu için rapor oluştuabilirsiniz. Oluşturulan raporları daha önceden seçmiş olduğunuz "Output Dir Path" konumundan kontrol edebilirsiniz.
Not: Her yeni Generate Report işleminde, eski rapor silinmektedir. Eğer daha önceden oluşturulan rapora ihtiyaç olunacaksa lütfen yedeğini alınız.