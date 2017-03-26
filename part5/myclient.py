import mypkg.mymod as mymod

print(mymod.test('myclient.py'))

from mypkg.mymod import countLines

print(countLines('myclient.py'))
