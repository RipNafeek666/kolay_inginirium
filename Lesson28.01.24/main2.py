while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xCirc -= 1
    elif keys[pygame.K_RIGHT]:
        xCirc += 1
    elif keys[pygame.K_UP]:
        yCirc -= 1
    elif keys[pygame.K_DOWN]:
        yCirc += 1
    else:
        xCirc = 250
        yCirc = 250

    if xCirc > xc + 150:
        colorCirc = (255, 0, 0)
    if  xCirc < cx - 150:
        colorCirc = (255, 0, 0)
    if yCirc > cy + 150:
        colorCirc = (255, 0, 0)
    if yCirc < cy - 150:
        colorCirc = (255, 0, 0)
    else:
        colorCirc = (255, 255, 0)

    win.fill((255,255,255))
    pygame.draw.circle(win, (colorCirc), (xCirc, yCirc), 30)
    pygame.display.update()
    pygame.time.delay(10)


