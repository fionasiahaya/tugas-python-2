import numpy as np
#input dua array
x=np.array([1,2,3,4,5])
h=np.array([2,3,4,5,6])
#dikonvolusi kedua array
y=np.zeros(len(x)+len(h)-1)
for i in range(len(x)):
    for j in range (len(h)):
        y[i+j]+=x[i]*h[j]
#print hasil
    print(y)
#validasi hasing dengan numpy.convolve
    y_numpy=np.convolve(x,h)
    print(y_numpy)
#cek jika hasil sama
    if np.array_equal(y,y_numpy):
        print("Hasil yang sama")
    else:
        print("Hasil yang tidak sama")
