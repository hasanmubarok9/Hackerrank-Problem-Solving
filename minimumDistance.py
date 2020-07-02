# Ini adalah soal dari hackkerank
# deskripsi soal adalah sebagai berikut

# jarak antara dua element yang sama dalam sebuah list atau array adalah selisih index antara dua element itu
# di soal ini kita diminta untuk menemukan jarak minimum yang bisa ditemukan dalam sebuah array atau list
# dan menurut saya ini adalah salah satu solusi yang paling keren, di hackerrank bahasa pemrograman yang paling ampuh untuk digunakan
# menyelesaikan soal2 nya adalah python, fleksibilitas, kesederhanaan dan melimpahnya library yang ada membuat solusi yang ditulis dengan python selalu bisa melewati hampir semua test case
# di file ini juga saya belajar untuk mengetik tanpa melihat keyboard
# di majelis lucu indonesia, saya melihat itu adalah forum yang mengumpulkan komika dan artist untuk melakukan roasting dan stand up comedy
# di situ saya baru mengetahui tentang stand up comedy yang tdak ditutup2i, semuanya serba terbuka dan terjadi secara alami


def minimumDistances(a):
    n = len(a)
    for d in range(1, n):
        for i in range(n-d):
            if a[i] == a[i+d]:
                return d
    return -1
print(minimumDistances([3, 2, 1, 2, 3]))

