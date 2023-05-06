import pygame
import random 
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi juego RPG 2D")

# Cargar recursos
player_image = pygame.image.load(r'JUEGO\Player.png')
enemy_image = pygame.image.load(r'JUEGO\enemy2.png')
map_image = pygame.image.load(r'JUEGO\mapa_capas.png')
font = pygame.font.Font(None, 24)

# Crear el personaje y los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.velocidad_x = random.randint(-5, 5)
        self.velocidad_y = random.randint(-5, 5)
        self.alive = True
        self.timer = 5
        self.respawn_timer = 5

    def update(self):
        if self.health <= 0 and self.alive:
            self.alive = False
            self.timer = 120
        if self.timer > 0:
            self.timer -= 1
        elif not self.alive:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(0, screen_height - self.rect.height)
            self.health = 1
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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height / 2
        self.health = 1000 # Vida del jugador
        self.attack_damage = 20  # Daño del ataque

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
    # Verificar si hay algún enemigo cerca del jugador
     enemies_nearby = False
     for enemy in enemies:
        if pygame.sprite.collide_rect(self, enemy):
            enemies_nearby = True
            break

    # Si no hay ningún enemigo cerca del jugador, agregar un nuevo enemigo
     if not enemies_nearby:
        new_enemie = Enemy(random.randint(0, screen_width), random.randint(0, screen_height))
        enemies.add(new_enemie)
        print("Ataque!")
               
               
def menu_principal():
    # Cargar imagen de fondo
    fondo_menu = pygame.image.load(r'JUEGO\mapa_n.png').convert()

    # Cargar música
    pygame.mixer.music.load(r"JUEGO\Undertale_Megalovania.mp3")

    # Reproducir música en bucle
    pygame.mixer.music.play(-1)

    # Bucle principal del menú
    while True:
        # Manejar eventos de Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Si se presionó una tecla, detener la música y salir del bucle del menú principal
                pygame.mixer.music.stop()
                return

        # Dibujar la imagen de fondo en la pantalla
        screen.blit(fondo_menu, (0, 0))

        # Actualizar la pantalla
        pygame.display.flip()

menu_principal()   
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
for i in range(3):
    enemy = Enemy(100 * i + 10, 10)
    enemies.add(enemy)

# Crear el mapa
game_map = Map(0, 0)

# Crear la interfaz de usuario
def draw_text(text, x, y):
    surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface, (x, y))

# Configurar la frecuencia de eventos
ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
enemy_spawn_time = 500000  # en milisegundos
pygame.time.set_timer(ENEMY_SPAWN_EVENT, enemy_spawn_time)

# Lista de todos los sprites
all_sprites = pygame.sprite.Group()

# Lista de todos los enemigos
enemies = pygame.sprite.Group()

# Variable para rastrear el tiempo desde la última aparición de un enemigo
spawn_timer = 0

# Bucle principal
running = True
clock = pygame.time.Clock()
while running:
    # Control de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # No hacer nada si ya hay demasiados enemigos en pantalla
                if len(enemies) >= 10:
                    continue
                # Reiniciar el temporizador de aparición de enemigos
                spawn_timer = 0
                # Crear un nuevo enemigo y agregarlo a las listas
                new_enemy = Enemy()
                all_sprites.add(new_enemy)
                enemies.add(new_enemy)

    # Actualizar los sprites
    all_sprites.update()

    # Dibujar los sprites
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

# Dibujar elementos en pantalla
    screen.fill((0, 0, 0))
    game_map.draw(screen)
    enemies.draw(screen)
    screen.blit(player.image, player.rect)
    draw_text("Salud: " + str(player.health), 10, 10)
    pygame.display.flip()

    # Actualizar el temporizador de aparición de enemigos
    spawn_timer += clock.tick(60)

    # Aparecer un nuevo enemigo si ha pasado suficiente tiempo desde el último
    if spawn_timer >= 3000:
        spawn_timer = 0
        new_enemy = Enemy()
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)

# Salir del juego
pygame.quit()