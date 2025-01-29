const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Configuración del jugador
const player = {
    x: canvas.width / 2 - 30,
    y: canvas.height - 70,
    width: 60,
    height: 60,
    speed: 15,
    img: new Image()
};
player.img.src = "imgs/dou.png";

// Balas y enemigos
let bullets = [];
let enemies = [];

const bulletSpeed = 10;
const enemySpeed = 5;

// Cargar imágenes
const bulletImg = new Image();
bulletImg.src = "imgs/remasterbesos.png";

const enemyImg = new Image();
enemyImg.src = "imgs/baby.png";

// Dibujar jugador
function drawPlayer() {
    ctx.drawImage(player.img, player.x, player.y, player.width, player.height);
}

// Dibujar balas
function drawBullets() {
    bullets.forEach(bullet => {
        ctx.drawImage(bulletImg, bullet.x, bullet.y, bullet.width, bullet.height);
    });
}

// Dibujar enemigos
function drawEnemies() {
    enemies.forEach(enemy => {
        ctx.drawImage(enemyImg, enemy.x, enemy.y, enemy.width, enemy.height);
    });
}

// Actualizar lógica del juego
function update() {
    bullets.forEach((bullet, i) => {
        bullet.y -= bulletSpeed;
        if (bullet.y < 0) bullets.splice(i, 1);
    });

    if (Math.random() < 0.05) {
        enemies.push({
            x: Math.random() * (canvas.width - 60),
            y: 0,
            width: 60,
            height: 60
        });
    }

    enemies.forEach((enemy, i) => {
        enemy.y += enemySpeed;
        if (enemy.y > canvas.height) enemies.splice(i, 1);
    });

    bullets.forEach((bullet, i) => {
        enemies.forEach((enemy, j) => {
            if (
                bullet.x < enemy.x + enemy.width &&
                bullet.x + bullet.width > enemy.x &&
                bullet.y < enemy.y + enemy.height &&
                bullet.y + bullet.height > enemy.y
            ) {
                bullets.splice(i, 1);
                enemies.splice(j, 1);
            }
        });
    });
}

// Dibujar todo
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPlayer();
    drawBullets();
    drawEnemies();
}

// Manejo de teclas
const keys = new Set();

document.addEventListener("keydown", (event) => keys.add(event.key));
document.addEventListener("keyup", (event) => keys.delete(event.key));

// Bucle principal
function gameLoop() {
    if (keys.has("ArrowLeft") && player.x > 0) player.x -= player.speed;
    if (keys.has("ArrowRight") && player.x < canvas.width - player.width) player.x += player.speed;
    if (keys.has(" ") && bullets.length < 10) {
        bullets.push({ x: player.x + player.width / 2 - 25, y: player.y, width: 50, height: 50 });
    }

    update();
    draw();
    requestAnimationFrame(gameLoop);
}

// Iniciar el juego
gameLoop();
