import sys, pygame, random
#PyGame Setup
pygame.init(); width, height = 1920, 1080; screen = pygame.display.set_mode((width, height))
#Game variables setup
player_score = [0, 0]; dummy = 0; active_player = 1; winner = 0; game_running = True; winning_score = 51; hold_color, roll_color = (255, 255, 255), (255, 255, 255); cur_dice = 0
#Game images, text, font setup
dice = [pygame.image.load(f'dice-1.png'), pygame.image.load(f'dice-2.png'), pygame.image.load(f'dice-3.png'), pygame.image.load(f'dice-4.png'), pygame.image.load(f'dice-5.png'), pygame.image.load(f'dice-6.png')]; font = pygame.font.Font('Game Played.otf', 100); player1, player2, score1, score2, roll, hold, winner_text = font.render('Player 1', True, (0,0,0)), font.render('Player 2', True, (0,0,0)), font.render(str(player_score[0]), True, (0,0,0)), font.render(str(player_score[1]), True, (0,0,0)), font.render('Roll', True, (0,0,0)), font.render('Hold', True, (0,0,0)), font.render('Winner!', True, (229, 80, 57))
#Game Logic
while True:
    screen.fill((116, 185, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and game_running:
            if pygame.mouse.get_pos()[0] >= 0.25*width-(roll.get_size()[0]/2)-50 and pygame.mouse.get_pos()[0] <= 0.25*width+(roll.get_size()[0]/2)+90-50 and pygame.mouse.get_pos()[1] >= 0.25*height-(roll.get_size()[1]/2)-25 and pygame.mouse.get_pos()[1] <= 0.25*height+(roll.get_size()[1]/2)+55-25:
                cur_dice = random.randint(0, 5)
                if not cur_dice == 0:
                    player_score[active_player-1] += cur_dice+1
                    dummy += cur_dice+1
                else:
                    player_score[active_player-1] -= dummy
                    dummy = 0
                    active_player = 3-active_player 
                roll_color = (178, 190, 195)
            if pygame.mouse.get_pos()[0] >= 0.75*width-(hold.get_size()[0]/2)-50 and pygame.mouse.get_pos()[0] <= 0.75*width+(hold.get_size()[0]/2)+90-50 and pygame.mouse.get_pos()[1] >= 0.25*height-(hold.get_size()[1]/2)-25 and pygame.mouse.get_pos()[1] <= 0.25*height+(hold.get_size()[1]/2)+55-25:
                dummy = 0
                if player_score[active_player-1] >= winning_score:
                    winner = active_player
                    game_running = False
                active_player = 3 - active_player
                hold_color = (178, 190, 195)
        if event.type == pygame.MOUSEBUTTONUP: hold_color, roll_color = (255, 255, 255), (255, 255, 255)      
    score1, score2 = font.render(str(player_score[0]), True, (0,0,0)), font.render(str(player_score[1]), True, (0,0,0))
    if game_running and active_player == 1: pygame.draw.circle(screen, (255, 118, 117), (0.25*width-player1.get_size()[0]/2-50, 0.65*height), 20)
    elif game_running and active_player == 2: pygame.draw.circle(screen, (255, 118, 117), (0.75*width-player2.get_size()[0]/2-50, 0.65*height), 20)
    if not game_running and winner == 1: screen.blit(winner_text, (0.25*width-winner_text.get_size()[0]/2, 0.55*height-winner_text.get_size()[1]/2))
    elif not game_running and winner == 2: screen.blit(winner_text, (0.75*width-winner_text.get_size()[0]/2, 0.55*height-winner_text.get_size()[1]/2))
    pygame.draw.rect(screen, roll_color, [0.25*width-(roll.get_size()[0]/2)-50, 0.25*height-(roll.get_size()[1]/2)-25, roll.get_size()[0]+90, roll.get_size()[1]+55])
    pygame.draw.rect(screen, hold_color, [0.75*width-(hold.get_size()[0]/2)-50, 0.25*height-(hold.get_size()[1]/2)-25, hold.get_size()[0]+90, hold.get_size()[1]+55])
    screen.blit(roll, (0.25*width-(roll.get_size()[0]/2), 0.25*height-(roll.get_size()[1]/2)))
    screen.blit(hold, (0.75*width-(hold.get_size()[0]/2), 0.25*height-(hold.get_size()[1]/2)))
    screen.blit(dice[cur_dice], (width/2-(dice[cur_dice].get_size()[0]/2), (height/2-(dice[cur_dice].get_size()[1]/2)-height/4)))
    screen.blit(player1, (0.25*width-player1.get_size()[0]/2, 0.65*height-player1.get_size()[1]/2))
    screen.blit(player2, (0.75*width-player2.get_size()[0]/2, 0.65*height-player2.get_size()[1]/2))
    screen.blit(score1, (0.25*width-score1.get_size()[0]/2, 0.80*height-score1.get_size()[1]/2))
    screen.blit(score2, (0.75*width-score2.get_size()[0]/2, 0.80*height-score2.get_size()[1]/2))
    pygame.display.update() 