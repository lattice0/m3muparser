import re
import urllib3

url=""
pattern='#EXTINF:[^\n]*\n[^\n]*'
print("downloding file...")
http = urllib3.PoolManager()
response = http.request('GET', url)
m3 = response.data.decode('utf-8')
print("parsing...")
add_these = ['Variedades', 'Filmes']

def should_add(element):
    for this in add_these:
        return element.find(this)

m = re.findall(pattern, m3, re.M|re.S)
f = open('canais.m3mu','w')
f.write('#EXTM3U\n')
i=0
if m:
    for element in m:
        i+=1
        if should_add(element)>0:
            #print(element.find('Variedades'))
            f.write(element)
        #if i>10:
        #    break

print("done")
