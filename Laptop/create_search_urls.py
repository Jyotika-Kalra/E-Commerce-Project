f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=Laptops&i=computers-intl-ship&ref=nb_sb_noss_2'
f.write(url)
f.write('\n')


for i in range(2,300):
    url = 'https://www.amazon.com/s?k=Laptops&i=computers-intl-ship&page=' + str(i) + '&qid=1611307097&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()


