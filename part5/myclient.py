import mymod

print(mymod.test('myclient.py'))

from mymod import test

print(test('myclient.py'))
