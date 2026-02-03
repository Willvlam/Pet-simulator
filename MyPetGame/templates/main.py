import random
import time
import webbrowser
import os
import pathlib

def boss_fight_browser(glitch_name):
    """
    Handles the transition to the browser boss fight.
    Since main.py is inside the templates folder, we look for assets there.
    """
    try:
        # Get the folder where this script (main.py) is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # The HTML template should be in this same folder
        template_path = os.path.join(current_dir, "gio_boss.html")
        
        if not os.path.exists(template_path):
            print(f"\n[!] ERROR: Cannot find 'gio_boss.html'!")
            print(f"I am looking in: {current_dir}")
            input("Press Enter to continue (the game will end)...")
            return

        # Read the template and inject the name
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        content = content.replace("{{GLITCH_NAME}}", glitch_name)

        # Create the active fight file in the same folder so it can find style.css
        temp_file = os.path.join(current_dir, "active_boss_fight.html")
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(content)

        # Convert to a browser-friendly URL
        file_url = pathlib.Path(temp_file).as_uri()
        
        print(f"\n[SYSTEM] {glitch_name} IS OVERRIDING YOUR BROWSER...")
        print(f"CODESPACE USERS: If no tab opens, right-click 'active_boss_fight.html' and 'Open Preview'.")
        print(f"DIRECT LINK: {file_url}\n")
        
        # Attempt to open
        webbrowser.open(file_url, new=2)
        
        # Hold the terminal for a moment so the user sees the instructions
        time.sleep(3)

    except Exception as e:
        print(f"\n[CRITICAL ERROR] Failed to launch boss fight: {e}")
        input("Press Enter to exit...")

def main():
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':,.<>/?~"
    print('Hello, welcome to my pet shop!')
    
    pet_type = input('What type of pet do you want (dog, cat, spider, or a bird)? ').strip().lower()
    pet = "???"
    
    # Pet Selection Logic
    if pet_type == 'dog':
        pet = 'U・ᴥ・U'
    elif pet_type == 'cat':
        pet = '=(^._.^)=∫'
    elif pet_type == 'spider':
        pet = '/\\/\\( •̀ ω •́ )/\\/\\'
    elif pet_type == 'bird':
        pet = '⋘(•`⊖´•)⋙'
    elif pet_type == 'gio':
        pet = '𓀡'
    else:
        print("We don't have that pet. Goodbye!")
        return

    # Glitch Animation for GIO
    glitch_string = "???"
    if pet_type == 'gio':
        for _ in range(15):
            glitch_string = ''.join(random.choice(glitch_chars) for _ in range(3))
            print(f'This is {glitch_string}. He is your pet...', end="\r")
            time.sleep(0.05)
        print(f'\n{glitch_string} is stabilized. Good luck.')
    else:
        print(f'This is your pet: {pet}')

    # Game Stats
    pet_happyness = 5
    pet_hunger = 3
    amount_of_food = 3
    pet_satisfaction = 2
    satisfaction_death_counter = 2 

    # Main Game Loop
    while True:
        # Death Checks
        if pet_hunger >= 10:
            print(f'\nYour {pet_type} died of starvation. Game Over.')
            break
        if pet_happyness <= 0:
            print(f'\nYour {pet_type} got too sad and disappeared. Game Over.')
            break
            
        # GIO Specific Logic
        if pet_type == 'gio':
            if amount_of_food <= 0:
                print(f'\n{glitch_string} got hungry... he ate you instead.')
                break
            if pet_satisfaction <= 0:
                print(f"\n[WARNING] {glitch_string} IS UNSTABLE. Days remaining: {satisfaction_death_counter}")
                if satisfaction_death_counter <= 0:
                    print(f'{glitch_string} deleted your consciousness.')
                    break
        
        # Display Stats
        print(f"\n--- {pet_type.upper()} STATUS ---")
        print(f"Happiness: {pet_happyness} | Hunger: {pet_hunger} | Food: {amount_of_food}")
        
        choice = input(f'Action (feed, pet, walk, play, buy food, quit, kill): ').strip().lower()

        # Action Logic
        if choice in ('quit', 'exit'):
            if pet_type == 'gio':
                print(f"{glitch_string} says: NO EXIT.")
                continue
            break

        if choice == 'feed':
            if amount_of_food > 0:
                pet_hunger -= 2
                amount_of_food -= 1
                pet_satisfaction -= 1
                print("You fed your pet.")
            else:
                print("You are out of food!")
        elif choice == 'pet':
            pet_happyness += 1
            pet_satisfaction += 1
            print("You petted your pet.")
        elif choice == 'buy food':
            amount_of_food += 3
            pet_happyness -= 1
            print("You bought more food.")
        elif choice == 'kill':
            if pet_type == 'gio':
                print(f"\n[!] ERROR: ATTEMPTING TO DELETE {glitch_string}...")
                time.sleep(1)
                boss_fight_browser(glitch_string)
                break
            else:
                print('You killed your pet. You monster.')
                break
        
        # Daily Decay
        pet_hunger += 1
        pet_happyness -= 1
        if pet_type == 'gio' and pet_satisfaction <= 0:
            satisfaction_death_counter -= 1
        else:
            satisfaction_death_counter = 2

        # Floor stats at 0
        pet_hunger = max(pet_hunger, 0)
        pet_happyness = max(pet_happyness, 0)

if __name__ == '__main__':
    main()