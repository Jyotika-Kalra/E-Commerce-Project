f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.com/s?k=laptops&i=electronics-intl-ship&ref=nb_sb_noss'
f.write(url)
f.write('\n')


for i in range(2,157):
    url = 'https://www.amazon.com/s?k=laptops&i=electronics-intl-ship&page=' + str(i) + '&qid=1611051748&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()


