alien_0 = {'x_position':0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position: ' + str(alien_0['x_position']))

if alien_0['speed'] =='slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

favorite_languages = {
'jen': 'Python',
'sarah': 'c',
'edaward': 'ruby',
'phil': 'pyhton'
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

if name in friends:
    print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + '.')
