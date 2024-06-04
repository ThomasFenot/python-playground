def select_movie(id, name):
    info  = " - The Movie Identifier is {}"
    print(info.format(id))

    if name == 'Alien':
        print('Movie Selected : Alien')
    else:
        print('Movie Select : Not Alien')
        if name == 'Apocalypto':
            print('Movie Selected : Apocalypto')
        else:
            print('Movie Selected : Not Apocalypto')
            print('Movie Selected : ' + name)

select_movie(1, 'Alien')
select_movie(2, 'Apocalypto')
select_movie(3, 'Avatar')
