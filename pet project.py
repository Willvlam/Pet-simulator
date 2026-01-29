def main():
    print('hello welcome to my pet shop')
    pet = None
    pet_type = input('what type of pet do you want, a dog, a cat, a spider, or a bird ').strip().lower()
    pet_base_name = pet_type
    if pet_type == 'dog':
        dog_type = input('what type of dog do you want a sleepy dog or an awake dog ').strip().lower()
        if dog_type == 'sleepy':
            pet = '(U‾ᴥ‾U)'
        elif dog_type == 'awake':
            pet = 'U・ᴥ・U'
    elif pet_type == 'cat':
        pet_base_name = 'cat'
        cat_type = input('what type of cat do you want a sleepy cat or an awake cat ').strip().lower()
        if cat_type == 'sleepy':
            pet = 'ฅ(ﾐᵕᆽ ᵕﾐ)∫'
        elif cat_type == 'awake':
            pet = '=(^._.^)=∫'
    elif pet_type == 'spider':
        pet_base_name = 'spider'
        spider_choice = input('we only have one spider left, do you still want it ').strip().lower()
        if spider_choice in ('yes', 'y'):
            pet = '/\\/\\( •̀ ω •́ )/\\/\\'
    elif pet_type == 'bird':
        pet_base_name = 'bird'
        bird_type = input('what type of bird do you want a small bird or a big bird ').strip().lower()
        if bird_type == 'small':
            pet = '<(`O ◇O)>'
        elif bird_type == 'big':
            pet = '⋘(•`⊖´•)⋙'

    if not pet:
        print('No pet selected.')
        return

    print('this is your pet', pet)

    # Initialize pet status
    pet_happyness = 5
    pet_hunger = 3
    pet_satisfaction = 2
    amount_of_food = 3
    if pet_hunger <= 0:
        pet_hunger = 0
    if amount_of_food <= 0:
        amount_of_food = 0
    # Interactive action loop
    while True:
        # Death / runaway checks
        if pet_hunger >= 10:
            print('your pet died of starvation')
            break
        if pet_happyness <= 0:
            print('your pet is too sad and ran away')
            break

        active_choice = input('would you like to feed, pet, walk, play, buy food, or quit with your ' + pet_base_name + '? ')

        if active_choice in ('quit', 'q', 'exit'):
            print('goodbye!')
            break

        if active_choice == 'feed':
            pet_hunger -= 2
            pet_satisfaction -= 2
            amount_of_food -= 1
            print('you fed your pet')
        elif active_choice == 'pet':
            pet_happyness += 1
            pet_satisfaction += 1
            pet_hunger += 1
            print('you petted your pet')
        elif active_choice == 'walk':
            pet_happyness += 2
            pet_satisfaction += 2
            pet_hunger += 2
            print('you walked your pet')
        elif active_choice == 'play':
            pet_happyness += 3
            pet_satisfaction += 1
            pet_hunger += 2
            print('you played with your pet')
        elif active_choice == 'buy food':
            print('you bought food for your pet')
            amount_of_food += 3
            pet_satisfaction -= 3
            pet_hunger += 2
            pet_happyness -= 3
        else:
            print('Unknown action. Try: feed, pet, walk, play, buy food, or quit')
            continue

        # Clamp values and display status
        pet_hunger = max(pet_hunger, 0)
        pet_happyness = max(pet_happyness, 0)
        print('happiness:', pet_happyness, 'hunger:', pet_hunger, 'satisfaction:', pet_satisfaction)




if __name__ == '__main__':
    main()



