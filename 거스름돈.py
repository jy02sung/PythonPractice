MoneyIn=int(input('투입한 돈:',))
Price=int(input('물건값:',))
X=MoneyIn-Price 
print('거스름돈:',X,'원')
FHW=X//500
OHW=(X-FHW*500)//100
print('500원짜리:',FHW,'개')
print('100원짜리:',OHW,'개')
