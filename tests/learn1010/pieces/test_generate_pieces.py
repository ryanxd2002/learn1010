import pytest

from learn1010.pieces import generate_pieces
from learn1010.constants.pieces import PIECES


def test_generate_hand_length_and_contents(monkeypatch):
    # Make random.choice deterministic: always pick the first piece
    monkeypatch.setattr(generate_pieces.random, "choice", lambda seq: seq[0])

    hand = generate_pieces.generate_hand(3)
    assert isinstance(hand, list)
    assert len(hand) == 3
    # Should all be the same object as PIECES[0]
    assert all(h is PIECES[0] for h in hand)


def test_generate_hand_zero_and_negative(monkeypatch):
    # Zero pieces -> empty list
    monkeypatch.setattr(generate_pieces.random, "choice", lambda seq: seq[0])
    assert generate_pieces.generate_hand(0) == []

    # Negative numbers should behave like range(-1) -> empty list
    assert generate_pieces.generate_hand(-1) == []


def test_generate_hand_with_custom_get_all(monkeypatch):
    # Replace get_all_pieces in the module to return a custom list
    custom = [
        {"name": "a", "shape": [[1]]},
        {"name": "b", "shape": [[1]]},
    ]
    monkeypatch.setattr(generate_pieces, "get_all_pieces", lambda: custom)
    # Make choice always pick the second element
    monkeypatch.setattr(generate_pieces.random, "choice", lambda seq: seq[1])

    hand = generate_pieces.generate_hand(2)
    assert len(hand) == 2
    assert all(h is custom[1] for h in hand)


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
