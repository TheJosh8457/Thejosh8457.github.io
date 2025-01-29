from js import document, window

# Obtener el canvas y el contexto
canvas = document.getElementById("gameCanvas")
ctx = canvas.getContext("2d")

# Configuración del jugador
player = {
    "x": canvas.width // 2 - 30,
    "y": canvas.height - 70,
    "width": 60,
    "height": 60,
    "speed": 15
}

# Balas y enemigos
bullets = []
enemies = []

# Velocidades
bullet_speed = 10
enemy_speed = 5

# Cargar imágenes
player_img = window.Image.new()
player_img.src = "imgs/dou.png"

bullet_img = window.Image.new()
bullet_img.src = "imgs/remasterbesos.png"

enemy_img = window.Image.new()
enemy_img.src = "imgs/baby.png"

# Dibujar jugador
def draw_player():
    ctx.drawImage(player_img, player["x"], player["y"], player["width"], player["height"])

# Dibujar balas
def draw_bullets():
    for bullet in bullets:
        ctx.drawImage(bullet_img, bullet["x"], bullet["y"], bullet["width"], bullet["height"])

# Dibujar enemigos
def draw_enemies():
    for enemy in enemies:
        ctx.drawImage(enemy_img, enemy["x"], enemy["y"], enemy["width"], enemy["height"])

# Actualizar lógica del juego
def update():
    # Actualizar balas
    for bullet in bullets[:]:
        bullet["y"] -= bullet_speed
        if bullet["y"] < 0:
            bullets.remove(bullet)

    # Generar enemigos
    if window.Math.random() < 0.05:
        enemies.append({
            "x": window.Math.random() * (canvas.width - 60),
            "y": 0,
            "width": 60,
            "height": 60
        })

    # Actualizar enemigos
    for enemy in enemies[:]:
        enemy["y"] += enemy_speed
        if enemy["y"] > canvas.height:
            enemies.remove(enemy)

    # Detectar colisiones
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (bullet["x"] < enemy["x"] + enemy["width"] and
                bullet["x"] + bullet["width"] > enemy["x"] and
                bullet["y"] < enemy["y"] + enemy["height"] and
                bullet["y"] + bullet["height"] > enemy["y"]):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

# Dibujar todo
def draw():
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    draw_player()
    draw_bullets()
    draw_enemies()

# Manejar teclas
keys = set()

def keydown(event):
    keys.add(event.key)

def keyup(event):
    keys.discard(event.key)

document.addEventListener("keydown", keydown)
document.addEventListener("keyup", keyup)

# Bucle principal
def game_loop():
    # Mover jugador
    if "ArrowLeft" in keys and player["x"] > 0:
        player["x"] -= player["speed"]
    if "ArrowRight" in keys and player["x"] < canvas.width - player["width"]:
        player["x"] += player["speed"]

    # Disparar balas
    if " " in keys:
        if len(bullets) < 10:  # Limitar la cantidad de balas activas
            bullets.append({
                "x": player["x"] + player["width"] // 2 - 25,
                "y": player["y"],
                "width": 50,
                "height": 50
            })

    update()
    draw()
    window.requestAnimationFrame(game_loop)

# Iniciar el juego
game_loop()
