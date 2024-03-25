import os

# Screen
GAME_X = 800
GAME_Y = 400

# Resources
RESOURCE_ROOT = os.path.join(".", "resources")
ASSETS_ROOT = os.path.join(RESOURCE_ROOT, "assets")
BACKGROUND_ROOT = os.path.join(ASSETS_ROOT, "backgrounds")
PLAYER_ROOT = os.path.join(ASSETS_ROOT, "player")
RAT_ROOT = os.path.join(ASSETS_ROOT, "rat")

# Physics
GRAVITY = 1
PLAYER_JUMP_POWER = 18