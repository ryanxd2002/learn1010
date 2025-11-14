import copy

from learn1010.logic import any_move_possible
from learn1010.board import board as board_module
from learn1010.constants.pieces import PIECES
from learn1010.logic import check_valid


def find_piece(name):
    for p in PIECES:
        if p["name"] == name:
            return p
    raise KeyError(name)


def test_empty_pieces_list():
    b = board_module.create_empty_board()
    # ensure can_place is available in the module
    any_move_possible.can_place = check_valid.can_place

    assert any_move_possible.any_move_possible(b, []) is False


def test_any_move_possible_true(monkeypatch):
    b = board_module.create_empty_board()
    single = find_piece("single")

    # ensure the function uses the known can_place implementation
    monkeypatch.setattr(any_move_possible, "can_place", check_valid.can_place, raising=False)

    assert any_move_possible.any_move_possible(b, [single]) is True


def test_any_move_possible_false_when_board_full(monkeypatch):
    # create a full board (no zeros)
    b = [[1 for _ in range(10)] for _ in range(10)]
    single = find_piece("single")

    monkeypatch.setattr(any_move_possible, "can_place", check_valid.can_place, raising=False)

    assert any_move_possible.any_move_possible(b, [single]) is False


def test_no_placeable_due_to_size(monkeypatch):
    # small 1x1 empty board and a piece of width 2
    b = [[0]]
    line2 = find_piece("line2_h")

    monkeypatch.setattr(any_move_possible, "can_place", check_valid.can_place, raising=False)

    assert any_move_possible.any_move_possible(b, [line2]) is False
