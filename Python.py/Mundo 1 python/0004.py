d=float(input('Digite uma distância em metros: '))
km=d/1000
hcm=d/100
dam=d/10
dm=d*10
cm=d*100
mm=d*1000
print('A medida corresponde a \n {:.3f}km \n {:.2f}hcm \n {:.1f}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(km,hcm,dam,dm,cm,mm) )