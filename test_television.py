import pytest
from television import Television

@pytest.fixture
def tv():
    """Fixture to create a new Television object."""
    return Television()

def test_initial(tv):
    """Tests the Television initialization state."""
    assert not tv.status
    assert not tv.muted
    assert tv.volume == tv.MIN_VOLUME
    assert tv.channel == tv.MIN_CHANNEL

def test_power(tv):
    """Tests the power toggle."""
    tv.power()
    assert tv.status
    tv.power()
    assert not tv.status

def test_mute(tv):
    """Tests the mute function when the TV is on."""
    tv.mute()
    assert not tv.muted
    tv.power()
    tv.mute()
    assert tv.muted
    tv.mute()
    assert not tv.muted

def test_channel_up(tv):
    """Tests channel change upwards."""
    tv.power()
    for _ in range(tv.MAX_CHANNEL + 2):
        tv.channel_up()
    assert tv.channel == tv.MIN_CHANNEL

def test_channel_down(tv):
    """Tests channel change downwards."""
    tv.power()
    tv.channel = tv.MIN_CHANNEL
    for _ in range(tv.MAX_CHANNEL + 2):
        tv.channel_down()
    assert tv.channel == tv.MAX_CHANNEL

def test_volume_up(tv):
    """Tests the volume increase function."""
    tv.power()
    tv.muted = True
    tv.volume_up()
    assert not tv.muted
    for _ in range(tv.MAX_VOLUME + 2):
        tv.volume_up()
    assert tv.volume == tv.MAX_VOLUME

def test_volume_down(tv):
    """Tests the volume decrease function."""
    tv.power()
    tv.volume = tv.MAX_VOLUME
    tv.muted = True
    tv.volume_down()
    assert not tv.muted
    for _ in range(tv.MAX_VOLUME + 2):
        tv.volume_down()
    assert tv.volume == tv.MIN_VOLUME

def test_string(tv):
    """Tests the __str__ method for accurate representation."""
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"
    tv.mute()
    assert str(tv) == "Power = On, Channel = 0, Volume = Muted"
    tv.volume_up()
    assert str(tv) == "Power = On, Channel = 0, Volume = 1"
