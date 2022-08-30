player = {
    'name': 'bobby',
    'age': '18',
    'alive': True,
    'food': ['🌮', '🥗'],
    "country": {
        'main': "suwon",
        'sub': 'yongin'
    }
}

print(player.get('age'))
print(player.get('food'))
print(player['food'])
print(player.pop('age'))

player['xp'] = 1000
player['food'].append('🧊')

print(player)
print(player["country"]["main"])

# key-value pair
# value 변경 가능 (mutable)
