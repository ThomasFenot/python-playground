def show_variables(id,name):
    info = "Identifier is {}"
    print(info.format(id))

    info = "Identifier is {}"
    print(info.format(name))

    domestic = 187705427
    international = 272878533
    info = "The total is {:.2f} dollars"
    print(info.format(domestic + international))

    name = 'Thomas'
    last_name = 'Fenot'

    print(name + ' ' + last_name)

show_variables(1, 'Jérome')