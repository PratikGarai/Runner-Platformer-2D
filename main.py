import pygame

if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption("Sample Game")
    screen = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()


    test_surface = pygame.Surface((100, 100))
    test_surface.fill((255, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(test_surface, (50, 100))

        pygame.display.update()
        clock.tick(60)