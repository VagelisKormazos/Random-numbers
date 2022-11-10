# 13.H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς. Χρησιμοποιείστε αρχικά την
#διεύθυνση https://drand.cloudflare.com/public/latest για να πάρετε το τελευταίο randomness το οποίο θα το χωρίσετε σε
#δυάδες δεκαεξαδικών χαρακτήρων, και κάθε μια θα την μετρέψετε σε ακέραιο και θα την κάνετε modulo 80. Κρατείστε αυτούς
#τους 32 αριθμούς μοναδική φορά το καθένα και υπολογίστε πόσοι από αυτούς τους αριθμούς θα κληρονόντουσα� � στην
#τελευταία κλήρωση του ΚΙΝΟ που θα βρείτε εδώ https://api.opap.gr/draws/v3.0/1100/last-result-and-active

import requests
#save the data from cloudflare.
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
dat = r.json()
a=dat["randomness"]

bnr=[]
#split the number.
for i in range(0,len(a),2):
    bnr.append(a[i:i+2])
print(bnr)
print()
#conversion from hexadecimal to decimal.
hex=[]
for j in range(0,len(bnr)):
    hex.append(int(bnr[j], base=16)%80)
print("The numbers from cloudflare are this:")
print(hex)
print()
#save the data from opap.
r = requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
dataa = r.json()
last=dataa['last']
w=last['winningNumbers']
#print(w)
win=w['list']
print("The lasts winning kino numbers from Opap are this:")
print(win)
print()
l=[]
#save the common in a new list and print it.
for x in hex:
    for y in win:
        if x==y:
            l.append(x)
print("This numbers are common:",set(l))