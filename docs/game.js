// Browser port of the text game (simplified)
(() => {
  const petSelect = document.getElementById('pet-select');
  const startBtn = document.getElementById('start-btn');
  const selector = document.getElementById('selector');
  const game = document.getElementById('game');
  const petDisplay = document.getElementById('pet-display');
  const status = document.getElementById('status');
  const log = document.getElementById('log');

  const btnFeed = document.getElementById('feed');
  const btnPet = document.getElementById('pet');
  const btnWalk = document.getElementById('walk');
  const btnPlay = document.getElementById('play');
  const btnBuy = document.getElementById('buy');
  const btnKill = document.getElementById('kill');
  const btnQuit = document.getElementById('quit');

  let petType, petChar, glitchString;
  let pet_happyness, pet_hunger, amount_of_food, pet_satisfaction, satisfaction_death_counter;

  function addLog(msg) {
    if (!log) return;
    const el = document.createElement('div');
    el.textContent = ">> " + msg;
    log.prepend(el);
  }

  function setStatus() {
    if (!status) return;
    status.textContent = `Happiness: ${pet_happyness} | Hunger: ${pet_hunger} | Food: ${amount_of_food}`;
  }

  function initFor(type) {
    petType = type;
    if (type === 'dog') petChar = 'U・ᴥ・U';
    else if (type === 'cat') petChar = '=(^._.^)=∫';
    else if (type === 'spider') petChar = '/\\/\\( •̀ ω •́ )/\\/\\';
    else if (type === 'bird') petChar = '⋘(•`⊖´•)⋙';
    else if (type === 'gio') petChar = '𓀡';
    else petChar = '???';

    pet_happyness = 5;
    pet_hunger = 3;
    amount_of_food = 3;
    pet_satisfaction = 2;
    satisfaction_death_counter = 2;
    glitchString = '???';

    if (petDisplay) petDisplay.textContent = petChar;
    addLog(`This is your pet: ${petChar}`);
    setStatus();

    if (petType === 'gio') {
      // quick visual stabilizer
      let steps = 10;
      const chars = "!@#$%^&*()_+-=[]{}|;':,.<>/?~";
      const iv = setInterval(() => {
        glitchString = Array.from({length:3}, ()=>chars.charAt(Math.floor(Math.random()*chars.length))).join('');
        if (petDisplay) petDisplay.textContent = glitchString;
        if (--steps <= 0) {
          clearInterval(iv);
          if (petDisplay) petDisplay.textContent = petChar;
          addLog(`${glitchString} is stabilized. Good luck.`);
        }
      }, 60);
    }
  }

  function checkDeaths() {
    if (pet_hunger >= 10) { addLog(`Your ${petType} died of starvation. Game Over.`); endGame(); return true; }
    if (pet_happyness <= 0) { addLog(`Your ${petType} got too sad and disappeared. Game Over.`); endGame(); return true; }
    if (petType === 'gio') {
      if (amount_of_food <= 0) { addLog(`${glitchString} got hungry... he ate you instead.`); endGame(); return true; }
      if (pet_satisfaction <= 0) {
        addLog(`[WARNING] ${glitchString} IS UNSTABLE. Days remaining: ${satisfaction_death_counter}`);
        if (satisfaction_death_counter <= 0) { addLog(`${glitchString} deleted your consciousness.`); endGame(); return true; }
      }
    }
    return false;
  }

  function endGame() {
    [btnFeed,btnPet,btnWalk,btnPlay,btnBuy,btnKill].forEach(b=>{ if (b) b.disabled=true; });
  }

  function dailyDecay() {
    pet_hunger += 1;
    pet_happyness -= 1;
    if (petType === 'gio' && pet_satisfaction <= 0) satisfaction_death_counter -= 1;
    else satisfaction_death_counter = 2;
    pet_hunger = Math.max(0, pet_hunger);
    pet_happyness = Math.max(0, pet_happyness);
  }

  // Action handlers
  if (btnFeed) btnFeed.addEventListener('click', () => {
    if (amount_of_food > 0) {
      pet_hunger = Math.max(0, pet_hunger - 2);
      amount_of_food -= 1;
      pet_satisfaction = Math.max(0, pet_satisfaction - 1);
      addLog("You fed your pet.");
    } else addLog("You are out of food!");
    dailyDecay(); setStatus(); checkDeaths();
  });

  if (btnPet) btnPet.addEventListener('click', () => {
    pet_happyness += 1; pet_satisfaction += 1;
    addLog("You petted your pet.");
    dailyDecay(); setStatus(); checkDeaths();
  });

  if (btnBuy) btnBuy.addEventListener('click', () => {
    amount_of_food += 3; pet_happyness -= 1;
    addLog("You bought more food.");
    dailyDecay(); setStatus(); checkDeaths();
  });

  if (btnKill) btnKill.addEventListener('click', () => {
    if (petType === 'gio') {
      addLog(`[!] ERROR: ATTEMPTING TO DELETE ${glitchString}...`);
      // open boss fight (uses the existing active_boss_fight.html)
      window.open('active_boss_fight.html', '_blank');
      addLog("Boss fight opened in a new tab.");
      endGame();
    } else {
      addLog('You killed your pet. You monster.');
      endGame();
    }
  });

  if (btnQuit) btnQuit.addEventListener('click', () => {
    if (petType === 'gio') {
      addLog(`${glitchString} says: NO EXIT.`);
      return;
    }
    addLog('Goodbye.');
    endGame();
  });

  if (btnWalk) btnWalk.addEventListener('click', () => {
    pet_happyness += 1; pet_hunger += 1;
    addLog("You walked your pet.");
    dailyDecay(); setStatus(); checkDeaths();
  });

  if (btnPlay) btnPlay.addEventListener('click', () => {
    pet_happyness += 2; pet_satisfaction += 1; pet_hunger += 1;
    addLog("You played with your pet.");
    dailyDecay(); setStatus(); checkDeaths();
  });

  startBtn.addEventListener('click', () => {
    const selection = petSelect.value;
    selector.classList.add('hidden');
    game.classList.remove('hidden');
    initFor(selection);
    if (log) log.innerHTML = ">> Welcome to the browser pet shop.";
  });

})();
