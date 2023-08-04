import math

# Fungsi untuk menghitung jarak antara dua titik dengan rumus Euclidean
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Fungsi untuk menyelesaikan TSP dengan algoritma Greedy
def tsp_greedy(points):
    # Inisiasi variabel awal
    n = len(points) # Banyaknya titik
    visited = [False] * n # Untuk menandai titik
    visited[0] = True # Titik awal selalu dikunjungi
    tour = [0] # List untuk menyimpan urutan titik yang dikunjungi
    current = 0 # Titik awal
    total_distance = 0 # Total jarak yang ditempuh


    # Loop sampai semua titik dikunjungi
    for i in range(n - 1):
        # Mencari titik terdekat yang belum dikunjungi
        min_distance = float('inf')
        nearest = None
        for j in range(n):
            if not visited[j]:
                dist = euclidean_distance(points[current][0], points[current][1],
                                          points[j][0], points[j][1])
                if dist < min_distance:
                    min_distance = dist
                    nearest = j
        
        # Mengunjungi titik terdekat
        visited[nearest] = True # Jika dikunjungi, maka True
        tour.append(nearest) # Menambahkan titik ke list tour
        current = nearest
        total_distance += min_distance # Menambahkan jarak ke total jarak

    # Menghitung jarak total yang ditempuh untuk mendapatkan kartu 
    # (TSP tanpa kembali ke titik awal)
    all_tour = tour.copy()
    all_card_dist = total_distance

    # Menghitung jarak total yang ditempuh untuk mendapatkan kartu 
    # dan kembali ke tempat awal (TSP dengan kembali ke titik awal)
    tour.append(0)
    total_distance += euclidean_distance(points[current][0], points[current][1],
                                         points[0][0], points[0][1])
    
    return all_tour, all_card_dist, tour, total_distance


# Aplikasi pemakaian fungsi

# Lokasi koordinat di sekolah dan asrama
points1 = [(-0.6823566285177947,0.6931773185769998),(-0.6908306068896195,0.6560155978259274),
           (-0.7102114982045293,0.6902874963907095),(-0.7224923632054185,0.6691401304319555),
           (-0.7190979803525010,0.6374005055338330),(-0.6546365231392883,0.6602412600027776),
           (-0.6813123348844101,0.6243960869202425),(-0.6922242824752516,0.6102020773937937),
           (-0.6647455880106747,0.6119472177570486),(-0.6314288212711290,0.5906712389110140)]

# Lokasi kooridnat di Old Bullworth Vale
points2 = [(-0.7339770057955377,0.7171200748019544),(-0.7515039527407907,0.7113837913199461),
           (-0.7881380380868279,0.7213568759748625),(-0.8245620953786954,0.7436009994076045),
           (-0.8832699860243451,0.7492174281678672),(-0.7718367662567971,0.8130983761912773),
           (-0.8213324752495055,0.6789928549708435),(-0.7754081955933145,0.6704141049165315),
           (-0.7802472155254634,0.6105844395197124),(-0.8683130760697679,0.6803168897974672),
           (-0.8671585091240956,0.6592062510491274),(-0.8777970188348831,0.6567323421563316)]

# Lokasi koordinat di Bullworth Town dan New Coventry
points3 = [(-0.6817731649855716,0.7391365227204432),(-0.7072935342821154,0.7737503467854907),
           (-0.6976769913303258,0.7734338711894395),(-0.6976769913303258,0.7762660249021138),
           (-0.6779875513944660,0.7825735561744409),(-0.6613793131754164,0.7936875787733442),
           (-0.6754555460852316,0.8029563933302057),(-0.6463638168978321,0.7539908900649692),
           (-0.6416860443756320,0.7626590303292033),(-0.6324592453638331,0.7522315129475174),
           (-0.6124686178808645,0.7926583543359982),(-0.5668703747570589,0.7545794704131197),
           (-0.5667660638855239,0.7724180054999863),(-0.5832626161595726,0.7992810836853295)]

# Lokasi koordinat di Blue Skies Industrial Park
points4 = [(-0.5884509331891934,0.6136238695016516),(-0.5555639706745410,0.6951375334578103),
           (-0.5890773097942485,0.6966137831224444),(-0.6004452706409040,0.6868705268337578),
           (-0.5977878252479059,0.6573453876431046),(-0.5954256515628629,0.6483777724118625),
           (-0.5786061730781284,0.6409168092642545),(-0.5640090603683348,0.6406863429521081)]

# Menjalankan fungsi tsp_greedy
tourAllCards, distanceAllCards, tourTSP, distanceTSP = tsp_greedy(points4)

# Menampilkan hasil
print("Rute untuk mendapatkan semua kartu:")
print(tourAllCards)
print("")
print("Jarak untuk mendapatkan semua kartu:")
print(distanceAllCards)
print("")
print("Rute untuk mendapatkan semua kartu dan kembali ke titik awal:")
print(tourTSP)
print("")
print("Jarak untuk mendapatkan semua kartu dan kembali ke titik awal:")
print(distanceTSP)
print("")