import random
import time
import webbrowser
import os

def boss_fight_browser(glitch_name):
    """Creates an upgraded HTML file and opens a browser tab for the boss fight."""
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>CRITICAL ERROR: {glitch_name}</title>
        <style>
            body {{ 
                background: #050000; 
                color: #ff0000; 
                font-family: 'Courier New', monospace; 
                text-align: center; 
                display: flex; 
                flex-direction: column; 
                justify-content: center; 
                height: 100vh; 
                margin: 0;
                overflow: hidden;
            }}
            #boss {{ 
                font-size: 180px; 
                margin: 10px; 
                text-shadow: 5px 5px #00ffff, -5px -5px #ff00ff; 
                animation: shake 0.1s infinite;
                cursor: crosshair;
                user-select: none;
            }}
            @keyframes shake {{
                0% {{ transform: translate(1px, 1px) rotate(0deg); }}
                50% {{ transform: translate(-3px, -2px) rotate(1deg); }}
                100% {{ transform: translate(1px, -1px) rotate(-1deg); }}
            }}
            .ui-container {{
                display: flex;
                justify-content: space-around;
                width: 80%;
                margin: 0 auto 20px auto;
            }}
            .stats-box {{
                border: 2px solid #ff0000;
                padding: 10px;
                background: rgba(255, 0, 0, 0.1);
                width: 250px;
            }}
            .bar-bg {{
                width: 100%;
                height: 15px;
                background: #330000;
                border: 1px solid red;
                margin-top: 5px;
            }}
            .bar-fill {{
                height: 100%;
                transition: width 0.2s;
            }}
            #hp-fill {{ background: red; width: 100%; }}
            #player-fill {{ background: #00ff00; width: 100%; }}
            
            .btn {{ 
                background: black; 
                color: white; 
                border: 3px double red; 
                padding: 20px 40px; 
                font-size: 24px; 
                font-weight: bold;
                cursor: pointer;
                transition: 0.2s;
            }}
            .btn:hover {{ background: red; color: black; box-shadow: 0 0 30px red; }}
            .btn:active {{ transform: scale(0.95); }}

            #log {{ 
                margin-top: 20px; 
                font-size: 16px; 
                color: #00ff00; 
                height: 120px;
                overflow-y: hidden;
                opacity: 0.8;
                border-top: 1px solid #333;
                padding-top: 10px;
            }}
            .damage-flash {{
                position: fixed;
                top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(255, 0, 0, 0.3);
                pointer-events: none;
                display: none;
            }}
        </style>
    </head>
    <body>
        <div id="flash" class="damage-flash"></div>
        
        <div class="ui-container">
            <div class="stats-box">
                <div>ENTITY: {glitch_name}</div>
                <div class="bar-bg"><div id="hp-fill" class="bar-fill"></div></div>
                <div>HP: <span id="hp-text">5000</span></div>
            </div>
            <div class="stats-box" style="border-color: #00ff00; color: #00ff00;">
                <div>PLAYER.USER</div>
                <div class="bar-bg" style="border-color: #00ff00;"><div id="player-fill" class="bar-fill"></div></div>
                <div>INTEGRITY: <span id="p-text">100</span>%</div>
            </div>
        </div>

        <div id="boss">𓀡</div>
        
        <div>
            <button class="btn" onclick="attack()">DELETION_PROTOCOL.EXE</button>
        </div>

        <div id="log">>> INITIALIZING SYSTEM DEFENSES...</div>

        <script>
            let bossHp = 5000;
            let playerHp = 100;
            const log = document.getElementById('log');

            function addLog(msg, color) {{
                const entry = document.createElement('div');
                entry.style.color = color || "#00ff00";
                entry.innerText = ">> " + msg;
                log.prepend(entry);
            }}

            function attack() {{
                if(playerHp <= 0 || bossHp <= 0) return;

                // Player attacks Boss
                let dmg = Math.floor(Math.random() * 300) + 150;
                bossHp -= dmg;
                document.getElementById('hp-text').innerText = bossHp <= 0 ? 0 : bossHp;
                document.getElementById('hp-fill').style.width = (Math.max(0, bossHp) / 5000 * 100) + "%";
                addLog("DEALT " + dmg + " DAMAGE TO {glitch_name}", "white");

                // Boss counter-attacks (30% chance)
                if (Math.random() < 0.4) {{
                    let pDmg = Math.floor(Math.random() * 15) + 5;
                    playerHp -= pDmg;
                    document.getElementById('p-text').innerText = playerHp <= 0 ? 0 : playerHp;
                    document.getElementById('player-fill').style.width = Math.max(0, playerHp) + "%";
                    
                    document.getElementById('flash').style.display = 'block';
                    setTimeout(() => {{ document.getElementById('flash').style.display = 'none'; }}, 100);
                    
                    addLog("{glitch_name} CORRUPTED YOUR FILES! -" + pDmg + "% INTEGRITY", "red");
                }}

                if (bossHp <= 0) {{
                    alert("SYSTEM RECOVERED: {glitch_name} PURGED.");
                    document.body.innerHTML = "<h1 style='color:white; font-size:50px;'>VOID NEUTRALIZED.</h1>";
                    setTimeout(() => {{ window.close(); }}, 3000);
                }} else if (playerHp <= 0) {{
                    alert("FATAL ERROR: PLAYER TERMINATED.");
                    document.body.style.background = "red";
                    document.body.innerHTML = "<h1 style='color:black; font-size:100px;'>GAME OVER</h1>";
                }}
            }}
        </script>
    </body>
    </html>
    """
    
    file_path = os.path.realpath("gio_boss.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    webbrowser.open('file://' + file_path)
    print(f"\n[!!!] {glitch_name} HAS ESCAPED TO YOUR BROWSER. CLOSE THE TAB TO ESCAPE.")

def main():
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':,.<>/?~"

    print('hello welcome to my pet shop')
    pet = None
    pet_type = input('what type of pet do you want, a dog, a cat, a spider, or a bird ').strip().lower()
    pet_base_name = pet_type
    
    if pet_type == 'dog':
        dog_type = input('what type of dog do you want a sleepy dog or an awake dog ').strip().lower()
        pet = '(U‾ᴥ‾U)' if dog_type == 'sleepy' else 'U・ᴥ・U'
    elif pet_type == 'cat':
        cat_type = input('what type of cat do you want a sleepy cat or an awake cat ').strip().lower()
        pet = 'ฅ(ﾐᵕᆽ ᵕﾐ)∫' if cat_type == 'sleepy' else '=(^._.^)=∫'
    elif pet_type == 'spider':
        pet = '/\\/\\( •̀ ω •́ )/\\/\\'
    elif pet_type == 'bird':
        bird_type = input('what type of bird do you want a small bird or a big bird ').strip().lower()
        pet = '<(`O ◇O)>' if bird_type == 'small' else '⋘(•`⊖´•)⋙'
    elif pet_type == 'gio':
        pet = '𓀡'
        
    if not pet:
        print('No pet selected.')
        return

    glitch_string = "???"
    if pet_type != 'gio':
        print('this is your pet', pet)
    else:
        while True:
            glitch_string = ''.join(random.choice(glitch_chars) for _ in range(3))
            print('this is', glitch_string,'he is your pet')
            time.sleep(0.05)
            if random.random() < 0.05:
                break

    pet_happyness = 5
    pet_hunger = 3
    pet_satisfaction = 2
    amount_of_food = 3
    satisfaction_death_counter = 2 

    while True:
        if pet_hunger >= 10:
            print('your ', pet, ' died of starvation')
            break
        if pet_happyness <= 0:
            print('your ', pet, ' is too sad and ran away')
            break
            
        if pet_type == 'gio':
            if amount_of_food <= 0:
                print(glitch_string, 'doesn\'t like not having food...')
                print('gio ate you...')
                break
            
            if pet_satisfaction <= 0:
                print(f"\nWARNING: {glitch_string} IS ANGRY. YOU HAVE {satisfaction_death_counter} DAYS TO FIX THIS.")
                if satisfaction_death_counter <= 0:
                    print(glitch_string, 'killed you for not taking care of him...')
                    break
        
        print(f"\n[Status] Happiness: {pet_happyness} | Hunger: {pet_hunger} | Satisfaction: {pet_satisfaction} | Food: {amount_of_food}")
        active_choice = input(f'would you like to feed, pet, walk, play, buy food, quit or kill your {pet_base_name}? ').strip().lower()

        if active_choice in ('quit', 'q', 'exit'):
            if pet_type == 'gio':
                print('gio never lets you leave...')
                continue
            print('goodbye!')
            break

        if active_choice == 'feed':
            if amount_of_food <= 0:
                print('you have no food! You did nothing today.')
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
            if pet_type == 'gio':
                print(glitch_string, 'blocked your attack...')
                print(glitch_string, 'is displeased with your actions...')
                time.sleep(1)
                boss_fight_browser(glitch_string)
                break
            else:
                print('you killed your pet. you are a horrible person.')
                break
        else:
            print('Unknown action.')
            continue

        if pet_type == 'gio' and pet_satisfaction <= 0:
            satisfaction_death_counter -= 1
        else:
            satisfaction_death_counter = 2 

        pet_hunger = max(pet_hunger, 0)
        pet_happyness = max(pet_happyness, 0)

if __name__ == '__main__':
    main()