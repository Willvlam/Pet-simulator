import random
import time
def main():
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':,.<>/?~"

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
    elif pet_type == 'gio':
        pet_base_name = 'gio'
        pet = '𓀡'
    if not pet:
        print('No pet selected.')
        return
    quit
    def run_glitch():
        try:
            while True:
            # Pick a random character
                char = random.choice(glitch_chars)
                print(char, end='', flush=True)
                time.sleep(0.1)  # Add a small delay for visual effect
        except KeyboardInterrupt:  # Allow exit on Ctrl+C:
            print('\nGlitch effect ended.')
            
    if pet_type != 'gio':
        print('this is your pet', pet)
    elif pet_type == 'gio':
        while True:
            glitch_string = ''.join(random.choice(glitch_chars) for _ in range(3))
            print('this is', glitch_string,'he is your pet')
            time.sleep(0.1)
            if random.random() < 0.05:  # 5% chance to break the loop each iteration
                break
    # Initialize pet status
    pet_happyness = 5
    pet_hunger = 3
    pet_satisfaction = 2
    if pet_satisfaction <= 0:
        pet_satisfaction = 0
    amount_of_food = 3
    if pet_hunger <= 0:
        pet_hunger = 0
    if pet_type != 'gio' and amount_of_food <= 0:
        amount_of_food = 0
    
    

    # Interactive action loop
    while True:
        # Death / runaway checks
        if pet_hunger >= 10:
            print('your ',pet,' died of starvation')
            break
        if pet_happyness <= 0:
            print('your ',pet,' is too sad and ran away')
            break
        if pet_type == 'gio' and amount_of_food <= 0:
            print(  glitch_string,'doent like not having food...')
            print('gio ate you...')
            break
        while pet_type == 'gio' and pet_satisfaction <= 0:
            print( glitch_string, 'is angry at you...')
            if satisfaction_death_counter <= 0:
                print(glitch_string, 'killed you for not taking care of him...')
                break
            break
            
            # this is unfinished code please revise and fix soon thx its about if satisfaction is 0 for gio you get one day to fix it or you lose
        satisfaction_death_counter = 2
            
        
        active_choice = input('would you like to feed, pet, walk, play, buy food, quit or kill your ' + pet_base_name + '? ')
        satisfaction_death_counter -= 1 
        if pet_type != 'gio' and active_choice in ('quit', 'q', 'exit'):
            print('goodbye!')
            break
        elif pet_type == 'gio' and active_choice in ('quit', 'q', 'exit'):
            print('gio never lets you leave...')
            continue 

        if active_choice == 'feed':
            if amount_of_food <= 0:
                print('you have no food to feed your pet')
                print('you chose to do nothing today')
            else:
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
        elif active_choice == 'kill':
            print('you killed your pet')
            print('you are a horrible person')
        elif pet_type == 'gio':
            print(glitch_string,'blocked your attack...')
            print(glitch_string, 'is displeased with your actions...')
            #this is where i want the new code for the boss fight in a different window 
            
            break
        else:
            print('Unknown action. Try: feed, pet, walk, play, buy food, quit, or kill')
            continue
            
            
        # Clamp values and display status
        pet_hunger = max(pet_hunger, 0)
        pet_happyness = max(pet_happyness, 0)
        print('happiness:', pet_happyness, 'hunger:', pet_hunger, 'satisfaction:', pet_satisfaction)
        print('satisfaction death counter:', satisfaction_death_counter)
        


if __name__ == '__main__':
    main()



