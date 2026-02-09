let bossHp = 5000;
let playerHp = 100;
const log = document.getElementById('log');
const glitchName = document.title.split(": ")[1] || "THE VOID";

function addLog(msg, color) {
    const entry = document.createElement('div');
    entry.style.color = color || "#00ff00";
    entry.innerText = ">> " + msg;
    if (log) log.prepend(entry);
}

function attack() {
    if(playerHp <= 0 || bossHp <= 0) return;

    let dmg = Math.floor(Math.random() * 300) + 150;
    bossHp -= dmg;
    const hpText = document.getElementById('hp-text');
    const hpFill = document.getElementById('hp-fill');
    if (hpText) hpText.innerText = bossHp <= 0 ? 0 : bossHp;
    if (hpFill) hpFill.style.width = (Math.max(0, bossHp) / 5000 * 100) + "%";
    addLog("DEALT " + dmg + " DAMAGE TO " + glitchName, "white");

    if (Math.random() < 0.4) {
        let pDmg = Math.floor(Math.random() * 15) + 5;
        playerHp -= pDmg;
        const pText = document.getElementById('p-text');
        const pFill = document.getElementById('player-fill');
        if (pText) pText.innerText = playerHp <= 0 ? 0 : playerHp;
        if (pFill) pFill.style.width = Math.max(0, playerHp) + "%";
        
        const flash = document.getElementById('flash');
        if (flash) {
            flash.style.display = 'block';
            setTimeout(() => { flash.style.display = 'none'; }, 100);
        }
        
        addLog(glitchName + " CORRUPTED YOUR FILES! -" + pDmg + "% INTEGRITY", "red");
    }

    if (bossHp <= 0) {
        alert("SYSTEM RECOVERED: " + glitchName + " PURGED.");
        document.body.innerHTML = "<h1 style='color:white; font-size:50px;'>VOID NEUTRALIZED.</h1>";
        setTimeout(() => { try { window.close(); } catch(e){} }, 3000);
    } else if (playerHp <= 0) {
        alert("FATAL ERROR: PLAYER TERMINATED.");
        document.body.style.background = "red";
        document.body.innerHTML = "<h1 style='color:black; font-size:100px;'>GAME OVER</h1>";
    }
}

/* ---------- Glitch text effect ---------- */
const bossEl = document.getElementById('boss');

function randomChar() {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;':,.<>/?~𓀡";
    return chars.charAt(Math.floor(Math.random() * chars.length));
}

function glitchOnce(duration = 150) {
    if (!bossEl) return;
    const orig = bossEl.dataset.orig ?? bossEl.innerText;
    bossEl.dataset.orig = orig;
    const len = Math.max(1, orig.length);
    let ticks = Math.ceil(duration / 40);
    const iv = setInterval(() => {
        let out = '';
        for (let i = 0; i < len; i++) {
            out += Math.random() < 0.6 ? randomChar() : (orig[i] || randomChar());
        }
        bossEl.innerText = out;
        if (--ticks <= 0) {
            clearInterval(iv);
            bossEl.innerText = orig;
        }
    }, 40);
}

// intermittent glitches
setInterval(() => {
    if (Math.random() < 0.25) {
        glitchOnce(120 + Math.random() * 300);
    }
}, 350);

// make boss clickable to glitch + attack
if (bossEl) {
    bossEl.style.cursor = 'pointer';
    bossEl.addEventListener('click', () => {
        glitchOnce(220);
        attack();
    });
}
