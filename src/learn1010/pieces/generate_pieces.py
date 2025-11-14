from learn1010.pieces.pieces import get_all_pieces, print_piece
import random

def generate_hand(num_pieces: int):
    """
    Generate a list of random pieces (the 'hand' the player can choose from).
    Pieces can repeat, which is fine for a simple version.
    """
    all_pieces = get_all_pieces()
    hand = [random.choice(all_pieces) for _ in range(num_pieces)]
    return hand

def print_hand(hand):
    """Print all pieces in the current hand."""
    print("Current hand:")
    for i, piece in enumerate(hand):
        print(f"Piece {i}:")
        print_piece(piece)
