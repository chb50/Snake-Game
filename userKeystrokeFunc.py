#keystroke input from user to be displayed on game interface
import pygame

def userKeystroke(event, userString):

    #note: userString is whatever the user has typed up to this point
    shift = pygame.key.get_pressed()
    
    if event.key == pygame.K_SPACE:
        userString += " "
        return userString
    elif shift[pygame.K_RSHIFT] or shift[pygame.K_LSHIFT]:
        #then we caps
        if event.key == pygame.K_a:
            userString += "A"
            return userString
        if event.key == pygame.K_b:
            userString += "B"
            return userString
        if event.key == pygame.K_c:
            userString += "C"
            return userString
        if event.key == pygame.K_d:
            userString += "D"
            return userString
        if event.key == pygame.K_e:
            userString += "E"
            return userString
        if event.key == pygame.K_f:
            userString += "F"
            return userString
        if event.key == pygame.K_g:
            userString += "G"
            return userString
        if event.key == pygame.K_h:
            userString += "H"
            return userString
        if event.key == pygame.K_i:
            userString += "I"
            return userString
        if event.key == pygame.K_j:
            userString += "J"
            return userString
        if event.key == pygame.K_k:
            userString += "K"
            return userString
        if event.key == pygame.K_l:
            userString += "L"
            return userString
        if event.key == pygame.K_m:
            userString += "M"
            return userString
        if event.key == pygame.K_n:
            userString += "N"
            return userString
        if event.key == pygame.K_o:
            userString += "O"
            return userString
        if event.key == pygame.K_p:
            userString += "P"
            return userString
        if event.key == pygame.K_q:
            userString += "Q"
            return userString
        if event.key == pygame.K_r:
            userString += "R"
            return userString
        if event.key == pygame.K_s:
            userString += "S"
            return userString
        if event.key == pygame.K_t:
            userString += "T"
            return userString
        if event.key == pygame.K_u:
            userString += "U"
            return userString
        if event.key == pygame.K_v:
            userString += "V"
            return userString
        if event.key == pygame.K_w:
            userString += "W"
            return userString
        if event.key == pygame.K_x:
            userString += "X"
            return userString
        if event.key == pygame.K_y:
            userString += "Y"
            return userString
        if event.key == pygame.K_z:
            userString += "Z"
            return userString
    else:
        if event.key == pygame.K_a:
            userString += "a"
            return userString
        if event.key == pygame.K_b:
            userString += "b"
            return userString
        if event.key == pygame.K_c:
            userString += "c"
            return userString
        if event.key == pygame.K_d:
            userString += "d"
            return userString
        if event.key == pygame.K_e:
            userString += "e"
            return userString
        if event.key == pygame.K_f:
            userString += "f"
            return userString
        if event.key == pygame.K_g:
            userString += "g"
            return userString
        if event.key == pygame.K_h:
            userString += "h"
            return userString
        if event.key == pygame.K_i:
            userString += "i"
            return userString
        if event.key == pygame.K_j:
            userString += "j"
            return userString
        if event.key == pygame.K_k:
            userString += "k"
            return userString
        if event.key == pygame.K_l:
            userString += "l"
            return userString
        if event.key == pygame.K_m:
            userString += "m"
            return userString
        if event.key == pygame.K_n:
            userString += "n"
            return userString
        if event.key == pygame.K_o:
            userString += "o"
            return userString
        if event.key == pygame.K_p:
            userString += "p"
            return userString
        if event.key == pygame.K_q:
            userString += "q"
            return userString
        if event.key == pygame.K_r:
            userString += "r"
            return userString
        if event.key == pygame.K_s:
            userString += "s"
            return userString
        if event.key == pygame.K_t:
            userString += "t"
            return userString
        if event.key == pygame.K_u:
            userString += "u"
            return userString
        if event.key == pygame.K_v:
            userString += "v"
            return userString
        if event.key == pygame.K_w:
            userString += "w"
            return userString
        if event.key == pygame.K_x:
            userString += "x"
            return userString
        if event.key == pygame.K_y:
            userString += "y"
            return userString
        if event.key == pygame.K_z:
            userString += "z"
            return userString
        if event.key == pygame.K_1:
            userString += "1"
            return userString
        if event.key == pygame.K_2:
            userString += "2"
            return userString
        if event.key == pygame.K_3:
            userString += "3"
            return userString
        if event.key == pygame.K_4:
            userString += "4"
            return userString
        if event.key == pygame.K_5:
            userString += "5"
            return userString
        if event.key == pygame.K_6:
            userString += "6"
            return userString
        if event.key == pygame.K_7:
            userString += "7"
            return userString
        if event.key == pygame.K_8:
            userString += "8"
            return userString
        if event.key == pygame.K_9:
            userString += "9"
            return userString
        if event.key == pygame.K_0:
            userString += "0"
            return userString

    #if none of the above keys were pressed, then simply return the the string that was given
    return userString
