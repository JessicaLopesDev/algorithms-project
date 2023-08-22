from challenges.challenge_encrypt_message import encrypt_message
import pytest

def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("jessica", "j")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 1)

    assert encrypt_message("jessica", 2) == "aciss_ej"
    assert encrypt_message("jessica", 3) == "sej_acis"
    assert encrypt_message("jessica", 8) == "acissej"

