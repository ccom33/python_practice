def line():
    print("#","-"*40)
line()
#-------------------------------------------------------
dic = {'boy' : '소년', 'school' : '학교', 'book' : ' 책' }
print(dic)
line()
#-----------------------------------------------------------
dic = {'boy' : '소년', 'school' : '학교', 'book' : ' 책' }
print(dic.get('student'))
print(dic.get('student', '사전에 없는 단어입니다.'))
#-----------------------------------------------------------
line()
dic = {'boy' : '소년', 'school' : '학교', 'book' : ' 책' }
if 'student' in dic:
    print("사전에 있는 단어입니다.")
else:
    print("이 단어는 사전에 없습니다.")
#-----------------------------------------------------------
line()
print(dic.keys())
print(dic['boy'])
print(dic.get('water', '사전에 없는 단어 입니다.'))

a = input("단어를 입력하세요.")
dic = {'boy' : '소년', 'school' : '학교', 'book' : ' 책' }
if a in dic:
    print('사전에 있는 단어 입니다.')
else:
    print('사전에 없는 단어 입니다.')
#-----------------------------------------------------------
line()
dic['boy'] = '남자'
dic['girl'] = '소녀'
print(dic)
#-----------------------------------------------------------
line()

song = """ by the rivers of babylon, there we sat down yeah we wept, when
we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1
print()
print(alphabet)
alphabet.sort()
print(alphabet)
