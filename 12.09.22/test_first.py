import first_task
import pytest


tests = [
    ('jTkd NDKek mdKW KDKN NnjD', 'Заглавных букв больше в 40.0% строк'),
    ('mfmKMKM kcmdKMS KDMKkmc snJMMCn nddjcj NCJDInc', 'Заглавных букв больше в 66.66666666666666% строк')
]


@pytest.mark.parametrize('inp, answer', tests)
def test_first(inp, answer):
    """Tests check_upper function."""
    assert first_task.check_upper(inp) == answer
