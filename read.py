data = []
count = 0
with open('reviews.txt','r') as f :
	for line in f :
		data.append(line.strip())
		count += 1
		if count % 1000 == 0 :
			print(len(data))
#print(len(data))
print('檔案讀取完畢，總共有', len(data) ,'筆資料')
print('---------------------')
sumlen = 0
for d in data :
	sumlen = sumlen + len(d)

print('總長:', sumlen, ";平均長度為", sumlen/len(data))

new = []
count = 0
for d in data :
	if len(d) < 100 :
		new.append(d)

print('留言字數低於100的數量：', len(new))		