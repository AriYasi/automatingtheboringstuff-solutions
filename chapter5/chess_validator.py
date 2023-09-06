chess_dict = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def is_valid_chess_board(passed_dict):
    piece_collection = {}

    for k, v in passed_dict.items():
        if v[0] == 'w' or v[0] == 'b':
            pass
        else:
            return False
        
        #piece_collection.setdefault(v, 1)
    
    return True

print(is_valid_chess_board(chess_dict))