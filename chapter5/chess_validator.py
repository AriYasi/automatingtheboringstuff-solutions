chess_dict = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '2h': 'wpawn'}

def is_valid_chess_board(dict_parameter):
    valid_pieces = {}
    
    #filters out anything not formatted correctly
    for k, v in dict_parameter.items():
        #check if given values are a white or black piece
        piece_color = v[0].lower()
        if piece_color != 'w' and piece_color != 'b':
            return False
        
        #check if piece is out of bounds
        piece_y_location = int(k[0])
        piece_x_location = k[1]
        valid_characters = 'abcdefgh'

        if piece_y_location > 8 or piece_x_location not in valid_characters:
            return False
        
        valid_pieces.setdefault(v, 0)
        valid_pieces[v] += 1

    #Checks final amount of pieces
    for k, v in valid_pieces.items():
        if ('king' in k or 'queen' in k) and v > 1:
            return False
        
        if 'pawn' in k and v > 8:
            return False

        black_count = 0
        white_count = 0

        piece_color = k[0].lower()
        if piece_color == 'w':
            white_count += 1
        else:
            black_count += 1

        if black_count > 16 or white_count > 16:
            return False
    
    return True

print(is_valid_chess_board(chess_dict))