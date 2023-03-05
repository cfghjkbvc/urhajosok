def bekeres():
    adatok = []
    with open('astronauts.csv', 'r', encoding='utf-8') as forrasfajl:
        for sor in forrasfajl:
            adatok.append(sor.split(','))
    del adatok[0]
    urhajosok = []
    for adat in adatok:
        if adat[4][1] != '/':
            urhajosok.append(adat[4][:2])
        else:
            urhajosok.append(adat[4][0])

    tulajdonsagok = []
    for urhajos in urhajosok:
        if urhajos not in [i['honap'] for i in tulajdonsagok]:
            tulajdonsag = {
                'gyakorisag': urhajosok.count(urhajos),
                'honap': urhajos
            }
            tulajdonsagok.append(tulajdonsag)
    return urhajosok, tulajdonsagok


def main():
    # A függvény listát hoz létre amit gyakoriság szerint csökkenő sorrendben állít fel
    leggyakoribb = lambda sorszam, ertek: sorted(bekeres()[1], key=lambda gyakorisag: gyakorisag['gyakorisag'], reverse=True)[sorszam][ertek]
    for i in range(3):
        print(f"{leggyakoribb(i,'honap')}. hónap, {'{0:.1%}'.format(leggyakoribb(i,'gyakorisag') / len(bekeres()[0]))}-os gyakoriság")


main()
