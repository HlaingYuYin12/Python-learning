from urllib.request import urlretrieve #urllib package ,urlretrieve function

link = input('image download link: ')

fileName = input('File Name : ')

urlretrieve(link,'image/'+fileName+'.jpg')
