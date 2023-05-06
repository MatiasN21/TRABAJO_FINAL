import pygame
import random 

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("APRUEBENME THE GAME")

 #Cargar música
pygame.mixer.music.load(r"JUEGO\Undertale_Megalovania.mp3")

# Reproducir música en bucle
pygame.mixer.music.play(-1)

# Cargar recursos
player_image = pygame.image.load(r'JUEGO\Player.png')
enemy_image = pygame.image.load(r'JUEGO\enemy2.png')
map_image = pygame.image.load(r'JUEGO\Mapa_Arena.png')
font = pygame.font.Font(None, 24)

# Crear el personaje y los enemigos
# Crear el personaje y los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.max_health = 100
        self.velocidad_x = random.randint(-5, 5)
        self.velocidad_y = random.randint(-5, 5)
        self.alive = True
        self.timer = 0
        self.respawn_timer = 0
        self.is_alive = True
    def draw(self, screen):
        screen.blit(self.image, self.rect)    

    def update(self):
        if self.health <= 0 and self.alive:
            self.kill()  # Eliminar la instancia del enemigo de todos los grupos de sprites que la contienen
            self.alive = False
            self.timer = 120
        if self.timer > 0:
            self.timer -= 1
        elif not self.alive:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(0, screen_height - self.rect.height)
            self.health = self.max_health
            self.alive = True
            self.timer = 0
        else:
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y
            if self.rect.right > screen_width or self.rect.left < 0:
                self.velocidad_x = -self.velocidad_x
            if self.rect.bottom > screen_height or self.rect.top < 0:
                self.velocidad_y = -self.velocidad_y

#Crear la lista de enemigos muertos
dead_enemies = []      
INVULNERABILITY_DURATION = 1000  # invulnerabilidad de 1 segundo

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height / 2
        self.health = 100 # Vida del jugador
        self.attack_damage = 20  # Daño del ataque
        self.last_collision_time = pygame.time.get_ticks()  # Almacenamos el tiempo de la última colisión
        self.invincible = False  # Inicialmente el jugador no está invulnerable
        self.invulnerable = True

    def update(self):
        if self.health <= 0:
            self.kill()

        # Comprobamos si ha pasado el tiempo suficiente desde la última colisión
        now = pygame.time.get_ticks()
        if now - self.last_collision_time > INVULNERABILITY_DURATION:
            # Si ha pasado, podemos volver a ser vulnerables
            self.invincible = False

    def take_damage(self, damage):
        if not self.invincible:  # Comprobamos si somos vulnerables
            self.health -= damage
            self.invincible = True  # Activamos la invulnerabilidad
            self.last_collision_time = pygame.time.get_ticks()  # Almacenamos el tiempo de la última colisión

    def draw_health_bar(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), (self.rect.x, self.rect.y - 10, self.health, 5))        

    def update(self, enemies, dead_enemies):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if keys[pygame.K_SPACE]:
            self.attack(enemies, dead_enemies)
             
    def attack(self, enemies, dead_enemies):
    # Buscar si hay algún enemigo eliminado que pueda reaparecer
     for enemy in dead_enemies:
        if enemy.respawn_timer <= pygame.time.get_ticks():
    # Si el temporizador ha pasado, eliminar el enemigo de la lista de enemigos eliminados
            dead_enemies.remove(enemy)
            # Reiniciar la posición y la salud del enemigo
            enemy.rect.x = random.randint(0, screen_width)
            enemy.rect.y = random.randint(0, screen_height)
            enemy.health = enemy.max_health
            # Agregar el enemigo a la lista de enemigos activos
            enemies.add(enemy)
            print("Enemigo reaparece!")
            # Salir del bucle
            break
     else:
        # Si no se encontró ningún enemigo que pueda reaparecer, generar uno nuevo
        new_enemie = Enemy(random.randint(0, screen_width), random.randint(0, screen_height))
        enemies.add(new_enemie)
        print("Ataque!")               

class Map(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = map_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Lógica de actualización del mapa (si es necesario)
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Implementar la lógica del juego
player = Player()
enemies = pygame.sprite.Group()
for i in range(10):
    enemy = Enemy(1 * i + 10, 10)
    enemies.add(enemy)

# Crear el mapa
game_map = Map(0, 0)

# Crear la interfaz de usuario
def draw_text(text, x, y):
    surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface, (x, y))

# Implementar la lógica del juego
player = Player()
enemies = pygame.sprite.Group()
for i in range(15):
    enemy = Enemy(1 * i + 10, 10)
    enemies.add(enemy)

# Crear el mapa
game_map = Map(0, 0)

# Crear la interfaz de usuario
def draw_text(text, x, y):
    font = pygame.font.Font(None, 60)
    surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface, (x, y))

# Bucle principal del juego
running = True
clock = pygame.time.Clock()
invulnerability_timer = 0
INVULNERABLE_TIME = 1000 # 1 segundo de invulnerabilidad
start_time = pygame.time.get_ticks() # tiempo de inicio del juego

while running:
    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Crear un nuevo enemigo después de 2 segundos
        if event.type == pygame.USEREVENT+1:
            x = random.randint(0, screen_width-enemy_image.get_width())
            y = random.randint(0, screen_height-enemy_image.get_height())
            enemy = Enemy(x, y)
            enemies.add(enemy)

    # Actualizar el juego
    player.update(enemies, dead_enemies)
    enemies.update()
    game_map.update()
 
    # Comprobar colisiones entre el jugador y los enemigos
    for enemy in enemies:
        if pygame.sprite.collide_rect(player, enemy) and not player.invulnerable:
            player.health -= 10
            player.invulnerable = True
            invulnerability_timer = pygame.time.get_ticks()

    # Controlar el tiempo de invulnerabilidad del jugador
    if player.invulnerable and pygame.time.get_ticks() - invulnerability_timer > INVULNERABLE_TIME:
        player.invulnerable = False

    # Verificar que los enemigos estén vivos antes de dibujarlos
    for enemy in enemies:
         if enemy.is_alive:
            enemy.draw(screen)

    # Verificar si la vida del jugador ha llegado a cero
    if player.health <= 0:
        draw_text("Has Perdido!", 100, 100)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Verificar si han pasado 60 segundos desde que comenzó el juego
    if pygame.time.get_ticks() - start_time >= 60000:
        draw_text("Has ganado el juego!", 100, 100)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Dibujar elementos en pantalla
    screen.fill((0, 0, 0))
    game_map.draw(screen)
    enemies.draw(screen)
    screen.blit(player.image, player.rect)
    draw_text("Salud: " + str(player.health), 10, 10)
    pygame.display.flip()

    # Configurar la velocidad de fotogramas
    clock.tick(60)

# Salir del juego
pygame.quit()



#Para este juego se uso la libreria pygame
