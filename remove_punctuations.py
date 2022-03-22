#take a string with punctuation and produce a string without punctuation
# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str  = input('enter the input string: ')
no_punc = ''
for i in my_str:
    if i not in punctuations:
        no_punc = no_punc+i;
print(no_punc)
