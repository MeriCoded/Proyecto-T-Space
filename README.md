‎‧₊˚✧ Estelar’s Adventure: Space Battle ‎‧₊˚✧

Estelar’s Adventure: Space Battle es un videojuego de tipo arcade de naves espaciales inspirado en los clásicos de los años 80 y 90, basándonos en los típicos juegos de 
16 bits con estética retro. 

El jugador controla a Estelar, una nave enviada a detener una invasión de meteoritos y derrotar a un jefe que amenaza a la Tierra, equipada con diferentes 
niveles de disparo que se desbloquean a medida que acumulás puntos. El objetivo es sobrevivir, esquivar meteoritos y disparar estratégicamente hasta llegar al jefe final.

---

El proyecto está dividido en varios módulos para mantener el orden del código:

- main.py: Lógica principal del juego.
- settings.py: Configuración general del juego (FPS, resolución, velocidades).
- estelar.py: Clase principal del jugador y su sistema de disparos/progresión.
- meteor.py: Clases para los distintos tipos de meteoritos (con herencia y polimorfismo).
- boss.py: Lógica del jefe final y sus patrones de disparo.
- space.py: Decorado/scroll de fondo espacial.
- menu.py, gameover.py, victory.py, controles.py: Interfaces de usuario (pantallas).
- constants.py: Variables constantes para definir momentos clave del juego (niveles, tiempo, etc).
- Assets/: Carpeta con todos los recursos visuales y sonoros del juego (sprites, sonidos, música).

---

Sonido y estilo visual

Estilo retro 16 bits: tanto en música como en efectos de sonido.
Música ambiental en el menú.
Efectos para disparos, botones y colisiones.

---

Requisitos

Python 3.10 o superior (probado con Python 3.11+).
Pygame 2.5 o superior.

Podés instalar Pygame con:

pip install pygame

---

Créditos

Proyecto desarrollado como parte de la Tecnicatura en Desarrollo de Videojuegos de la Universidad Nacional de la Matanza
Materia: Programación.
Profesores: Volker, Mariano Leonardo y Hirschfeldt, Dario

Autores/Desarrolladores:
OYOLA MANA, AGUSTIN THOMAS (Meri),
OVEJERO PEREZ, LUCIANO (Lucho),
ESPÓSITO ARCOSA, JULIETA ARIANA (Alaska),
ALZAMORA, BRUNO JULIAN,
DE LA TORRE , RUBEN ALEJANDRO,
SERVIDIO, STEFANO
