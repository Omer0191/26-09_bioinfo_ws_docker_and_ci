from greeter.main import greet, main


def test_greet_by_name():
    assert greet("Alice") == "Hello, Alice! Hei!"


def test_main_prompts_for_name(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt="": "Bob")

    main()

    captured = capsys.readouterr()
    assert "Hello, Bob! Hei!" in captured.out
