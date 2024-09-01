import jageocoder
#https://pypi.org/project/jageocoder/1.4.1/
spot = input('ランドマーク:')
jageocoder.init()
result=jageocoder.search(spot)
print(result)
print(result['x'],result['y'])