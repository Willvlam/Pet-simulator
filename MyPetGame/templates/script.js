let bossHp = 5000;
let playerHp = 100;
const log = document.getElementById('log');
const glitchName = document.title.split(": ")[1] || "THE VOID";

function addLog(msg, color) {
    const entry = document.createElement('div');
    entry.style.color = color || "#00ff00";
    entry.innerText = ">> " + msg;
    log.prepend(entry);
}

function attack() {
    if(playerHp <= 0 || bossHp <= 0) return;

    let dmg = Math.floor(Math.random() * 300) + 150;
    bossHp -= dmg;
    document.getElementById('hp-text').innerText = bossHp <= 0 ? 0 : bossHp;
    document.getElementById('hp-fill').style.width = (Math.max(0, bossHp) / 5000 * 100) + "%";
    addLog("DEALT " + dmg + " DAMAGE TO " + glitchName, "white");

    if (Math.random() < 0.4) {
        let pDmg = Math.floor(Math.random() * 15) + 5;
        playerHp -= pDmg;
        document.getElementById('p-text').innerText = playerHp <= 0 ? 0 : playerHp;
        document.getElementById('player-fill').style.width = Math.max(0, playerHp) + "%";
        
        document.getElementById('flash').style.display = 'block';
        setTimeout(() => { document.getElementById('flash').style.display = 'none'; }, 100);
        
        addLog(glitchName + " CORRUPTED YOUR FILES! -" + pDmg + "% INTEGRITY", "red");
    }

    if (bossHp <= 0) {
        alert("SYSTEM RECOVERED: " + glitchName + " PURGED.");
        document.body.innerHTML = "<h1 style='color:white; font-size:50px;'>VOID NEUTRALIZED.</h1>";
        setTimeout(() => { window.close(); }, 3000);
    } else if (playerHp <= 0) {
        alert("FATAL ERROR: PLAYER TERMINATED.");
        document.body.style.background = "red";
        document.body.innerHTML = "<h1 style='color:black; font-size:100px;'>GAME OVER</h1>";
    }
}