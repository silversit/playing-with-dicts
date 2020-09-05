import webbrowser


sap = {
    'location' : ['2.887308, 24.714599']

}
rep = {
    'hometown': {
        'name': ('troyan'),
        'country': ('BG')

                 }
}

def main():
    k = wrapper_1(sap, rep)
    request = str(input('hello, would you like to know where i live? :')).lower()
    location_1 = input('Would you like to see the location of my town in your browser: ')
    try:
    #maybe here is an easy way with while function ...
        if request == 'yes' and location_1 == 'yes':
            location_2(k)
            fun_url()

        elif request == 'no' and location_1 == 'yes':
            print('Ok, have a nice day', fun_url())
        elif request == 'no' and location_1 == 'no':
            print('exiting')
        elif request == 'yes' and location_1 == 'no':
            location_2(k)
        else:
            print(' not a valid answer')
    except TypeError as ve:
        print(ve)
def town(k):
    t = []
    for x, items in enumerate(k):

        n = x
        z = str(k[n])
        z = z.strip("{,(,',),}")
        t.append(z)
    return t


def location_2(k):
    r = list(town(k))
    o = sap.values()
    o = str(o).strip(",[,]{,(,',),},)dict_values([['")
    print(f'the locatin of my town is {o}')
    print(f'I am from', str(r[0]).strip("{,(,',),}"), 'situated in', str(r[1]).strip("{,(,',),})"))
def wrapper_1(sap, rep):

    rep = list(rep.values())

    for  m in (rep):

        k = zip(m.values())

    k = zip(k)

    return list(k)




def fun_url():




    webbrowser.open_new_tab('https://www.google.com/maps/place/Troyan/@42.8873364,24.7137596,19.5z/data=!4m5!3m4!1s0x40a97ece30c3f267:0xd2276ef7cabdece!8m2!3d42.8903751!4d24.7129702')

if __name__ == '__main__':
    main()
