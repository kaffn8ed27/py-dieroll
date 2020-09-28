from randomdotorg import RandomDotOrg

r = RandomDotOrg('die roll nick.r.reeve@gmail.com')


if r.get_quota() > 0:
    print r.randint(1, 6)
else:
    print 'Somehow you\'ve exceeded 10,0000 requests today'
