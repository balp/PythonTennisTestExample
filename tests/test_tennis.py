from tennis.tennis import TennisGame


def test_0_0_player_one_player_two():
    game = TennisGame("Player One", "Player Two")

    assert game.score() == "Love-All"
