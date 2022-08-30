player = {
    'name': 'bobby',
    'age': '18',
    'alive': True,
    'food': ['🌮', '🥗']
}

print(player.get('age'))
print(player.get('food'))
print(player['food'])
print(player.pop('age'))

player['xp'] = 1000
player['food'].append('🧊')

print(player)

# key-value pair
# value 변경 가능
