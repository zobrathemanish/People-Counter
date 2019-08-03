date = '20190724100000' 

# for c in date:
yy = date[0:4]
mm = date[4:6]
dd = date[6:8]
hrs = date[8:10]
mins = date[10:12]
sec = date[12:14]

final_date = yy + '-' + mm + '-' + dd
final_time = hrs + ":" + mins + ":" + sec

print(final_date)
print(final_time)
