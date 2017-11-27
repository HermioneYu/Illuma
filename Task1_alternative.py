from langdetect import detect


text = input('Type anything:')
detect(text)
print ('the langurage you are using is:' + detect(text))