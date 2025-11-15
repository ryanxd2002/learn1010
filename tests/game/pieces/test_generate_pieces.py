import pytest

from game.pieces import generate_pieces
from game.constants.pieces import PIECES


def test_generate_hand_length_and_contents(monkeypatch):
    # Make random.choice deterministic: always pick the first piece
    monkeypatch.setattr(generate_pieces.random, "choice", lambda seq: seq[0])

    hand = generate_pieces.generate_hand(3, PIECES)
    assert isinstance(hand, list)
    assert len(hand) == 3
    # Should all be the same object as PIECES[0]
    assert all(h is PIECES[0] for h in hand)


def test_generate_hand_zero_and_negative(monkeypatch):
    # Zero pieces -> empty list
    monkeypatch.setattr(generate_pieces.random, "choice", lambda seq: seq[0])
    assert generate_pieces.generate_hand(0, PIECES) == []

    # Negative numbers should behave like range(-1) -> empty list
    assert generate_pieces.generate_hand(-1, PIECES) == []

def test_print_hand_outputs(capsys):
    # Use two known pieces from PIECES and ensure output contains names and markers
    hand = [PIECES[0], PIECES[1]]
    generate_pieces.print_hand(hand)
    out = capsys.readouterr().out

    assert "Current hand:" in out
    # Piece names should be printed
    assert PIECES[0]["name"] in out
    assert PIECES[1]["name"] in out
    # The single piece should show a '#' for its single block
    assert "#" in out
