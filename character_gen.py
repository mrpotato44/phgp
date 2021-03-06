import random

def town_gen(town_dict, climate='plains', count=0):
    town_list = []
    for town in town_dict:
        town_list.append(town_dict[town])
    name_based_on_climate = random.randint(0, 3)
    if name_based_on_climate <= 2:
        name = ''
        syllables = ['mor', 'del', 'gol', 'bel', 'com', 'ere', 'gon', 'an', 'bar', 'es', 'crag']
        x = 0
        while x < 3:
            a = syllables[random.randint(0, (len(syllables) - 1))]
            if a not in name:
                name += a
                x += 1
        name = name.capitalize()
        return name
    else:
        name = ''
        gen_adjectives = ['roaring', 'winding', 'windy', 'firey', 'flaming', 'shady']
        if climate == 'plains':
            prefix = []
            suffix = ['plains', 'land']
        elif climate == 'mountains':
            prefix = ['mount']
            suffix = ['mountains', 'mountain']
        elif climate == 'hills':
            prefix = []
            suffix = ['hills', 'highlands']
        elif climate == 'coast':
            prefix = []
            suffix = ['coast', 'coasts']
        if random.randint(0, 1) == 0 and len(prefix) != 0:
            name += prefix[random.randint(0, (len(prefix) - 1))]
            syllables = ['mor', 'del', 'gol', 'bel', 'com', 'ere', 'gon', 'an', 'bar', 'es', 'crag']
            x = 0
            while x < 3:
                a = syllables[random.randint(0, (len(syllables) - 1))]
                if a not in name:
                    name += a
                    x += 1
        else:
            name += gen_adjectives[random.randint(0, (len(gen_adjectives) - 1))]
            suf = suffix[random.randint(0, (len(suffix) - 1))]
            if suf[-1] == 's':    
                name += suf
            else:
                name += '-'
                suf = suf.capitalize()
                name += suf
        name = name.capitalize()
        if count == 5:
            return name
        elif name not in town_list:
            return name
        else:
            count += 1
            town_gen(town_dict, climate, count)

def firstname():
    name = ''
    syllables = ['mor', 'sha', 'an', 'ann', 'rash', 'izen', 'alo', 'var', 'oros', 'golo', 'ale']
    num = random.randint(2, 3)
    x = 0
    while x < num:
        a = syllables[random.randint(0, (len(syllables) - 1))]
        if a not in name:
            name += a
            x += 1
    if random.randint(0, 1) == 1 and name[len(name) - 1] != 'a' and name[len(name) - 1] != 'e' and name[len(name) - 1] != 'i' and name[len(name) - 1] != 'o' and name[len(name) - 1] != 'u':
        letter = random.randint(0, 4)
        if letter == 0:
            name += 'a'
        elif letter == 1:
            name += 'e'
        elif letter == 2:
            name += 'i'
        elif letter == 3:
            name += 'o'
        else:
            name += 'u'
    name = name.capitalize()
    return name
#last name - syllables = ['for', 'al', 'blo', 'fle', 'fa', 'gor']
#race name - syllables = ['der', 'ol', 'om', 'mol', 'rol', 'ger']
def name(syllables, mins=1, maxs=2):
    name = ''
    num = random.randint(mins, maxs)
    x = 0
    while x < num:
        a = syllables[random.randint(0, (len(syllables) - 1))]
        if a not in name:
            name += a
            x += 1
    name = name.capitalize()
    return name
    
def char_gen(age_day=0, age_month=0, start_age=20, race='race', location='location'):
    personality_traits = ['imaginative', 'creative', 'original', 'curious', 'conscientious', 'hard-working', 'organized', 'punctual', 'conformist', 'talkative', 'active', 'affectionate', 'trusting', 'lenient', 'soft-hearted', 'good-natured', 'worried', 'temperamental', 'self-conscious', 'emotional']
    if age_day == 0 and age_month == 0:
        age_month = random.randint(1, 12)
        if age_month == 2:
            age = [random.randint(1, 28), age_month, start_age]
        elif age_month % 2 == 0 and age_month <= 7:
            age = [random.randint(1, 30), age_month, start_age]
        elif age_month % 2 != 0 and age_month > 7:
            age = [random.randint(1, 30), age_month, start_age]
        else:
            age = [random.randint(1, 31), age_month, start_age]
    else:
        age = [age_day, age_month, start_age]
    name = firstname()
    last_char = name[-1]
    gender_roll = random.randint(0, 99)
    if(last_char == 'e' or last_char == 'a' or last_char == 'i' or last_char == 'u' or last_char == 'y'):
        gender = 'Female'
    else:
        gender = 'Male'
    if gender == 'Female' and gender_roll == 1:
        gender = 'Male'
    elif gender == 'Male' and gender_roll == 1:
        gender = 'Female'
    
    for x in range(20):
        personality_traits[x] = random.randint(0, 1)
        
    if(personality_traits[1] >= personality_traits[2]):
        personality_traits[2] = personality_traits[1]
    else:
        personality_traits[1] = personality_traits[2]
    if(personality_traits[6] >= personality_traits[7]):
        personality_traits[7] = personality_traits[6]
    else:
        personality_traits[6] = personality_traits[7]
    if(personality_traits[19] == 1):
        personality_traits[18] = 1
        personality_traits[17] = 1
        personality_traits[16] = 1
    else:
        personality_traits[18] = 0
        personality_traits[17] = 0
        personality_traits[16] = 0

    return [name, age, gender, race, personality_traits, location, 'Alive']

def birth(day, month, race_mother, race_father, location):
    if race_mother != race_father and '-' not in [char for char in race_mother] and '-' not in [chare for chare in race_father]:
        new_race = race_mother + '-' + race_father
        return char_gen(day, month, 0, new_race, location)
    elif '-' not in [chara for chara in race_mother] and '-' in [charr for charr in race_father]:
        return char_gen(day, month, 0, race_mother, location)
    elif '-' in [cha for cha in race_mother] and '-' not in [ch for ch in race_father]:
        return char_gen(day, month, 0, race_father, location)
    else:
        return char_gen(day, month, 0, race_mother, location)

if __name__ == "__main__":
    people = []
    amount_of_characters = int(input("Amount of Characters: "))
    for x in range(amount_of_characters):
        people.append(char_gen())
    
    with open('character_data.json', 'w') as f:
        for s in people:
            f.write(str(s) + '\n')
    with open('character_data.json', 'r') as f:
        people = [line.rstrip('\n').rstrip('"') for line in f]
    
    print(people)
