class Repeat:

    lol = 'lolik'

    def noob(me):
        print(f'He is {me.lol}')

    def pro(me):
        print(f'he is {me.lols}')

    def again(jjj):
        print(f'Repeat {jjj.gogo}')
        
    def daya(yyy):
        if hasattr(yyy, 'bla'):
            print(f'YEAP {yyy.bla}')
        else:
            print(f'Nothing!')


asd = Repeat()
print(asd.noob)

asd.noob()

qwe = Repeat()
qwe.lols = 'pros!!!'
print(qwe.__dict__)
print(qwe.lols)


ex = Repeat()
ex.gogo = "it's okay!"
ex.again()

lg = Repeat()
#lg.bla= 'op'
lg.daya()