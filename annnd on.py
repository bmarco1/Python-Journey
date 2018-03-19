def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
print("\n")


describe_pet(pet_name='willie')

print("\n")
def get_formatted_name (first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print("\n")

def get_formatted_name(first_name, middle_name, last_name):
        """Return a full name, neatly formatted"""
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
