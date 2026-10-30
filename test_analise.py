from analise import win_rate, ganho_medio, expectancy, max_drawdown

DADOS = [50.0, -20.0, 35.5, -15.0]


def test_win_rate():
    assert win_rate(DADOS) == 0.5


def test_ganho_medio():
    assert ganho_medio(DADOS) == 42.75


def test_ganho_medio_sem_ganhos():
    assert ganho_medio([-1.0, -2.0]) == 0


def test_max_drawdown():
    assert max_drawdown(DADOS) == 20.0


def test_max_drawdown_lista_vazia():
    assert max_drawdown([]) == 0

def test_expectancy():
    assert expectancy(DADOS) == 12.625
