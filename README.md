# api-theater


api-teater adalah API sedderhana untuk sistem untuk jadwal theater bioskop di bangun menggunakan django(rest_framework, JWT,decorator chache, Redis ,serialezer)

saya menggunakan pattern ini karena lebih cepat dan mundah untuk handle erore, handle methot (GET, POST, PUT, PATCH, DELETE), CACHE (redis).

menggunakan JWT unutuk aut supaya aplikasi tidak sembarangnan di akses. kelebihan JWT mudah di buat dan cepat

unutk modull sebagai berikut


1 geenre 
	modul ini sebagai kategori genre film
2 film
	modul ini berupa list film yang akan tayang ataupun yang belum tayang
3 theater
	modul ini berupa list theater diman film ini di akan tayang

4 schedule
	modul ini   berupa jadwal film yang akan tayang maupun yang tayang di sebuah theater 

