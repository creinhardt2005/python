import pytest
from television import Television

@pytest.fixture
def tv():
    """Fixture to create a new Television object."""
    return Television()

def test_initial(tv):
    """Tests the Television initialization state."""
    assert not tv._Television__status
    assert not tv._Television__muted
    assert tv._Television__volume == tv.MIN_VOLUME
    assert tv._Television__channel == tv.MIN_CHANNEL

def test_power(tv):
    """Tests the power toggle."""
    tv.power()
    assert tv._Television__status
    tv.power()
    assert not tv._Television__status

def test_mute(tv):
    """Tests the mute function when the TV is on."""
    tv.mute()
    assert not tv._Television__muted
    tv.power()
    tv.mute()
    assert tv._Television__muted
    tv.mute()
    assert not tv._Television__muted

def test_channel_up(tv):
    """Tests channel change upwards."""
    tv.power()
    for _ in range(tv.MAX_CHANNEL + 2):
        tv.channel_up()
    assert tv._Television__channel == tv.MIN_CHANNEL

def test_channel_down(tv):
    """Tests channel change downwards."""
    tv.power()
    tv._Television__channel = tv.MIN_CHANNEL
    for _ in range(tv.MAX_CHANNEL + 2):
        tv.channel_down()
    assert tv._Television__channel == tv.MAX_CHANNEL

def test_volume_up(tv):
    """Tests the volume increase function."""
    tv.power()
    tv._Television__muted = True
    tv.volume_up()
    assert not tv._Television__muted
    for _ in range(tv.MAX_VOLUME + 2):
        tv.volume_up()
    assert tv._Television__volume == tv.MAX_VOLUME

def test_volume_down(tv):
    """Tests the volume decrease function."""
    tv.power()
    tv._Television__volume = tv.MAX_VOLUME
    tv._Television__muted = True
    tv.volume_down()
    assert not tv._Television__muted
    for _ in range(tv.MAX_VOLUME + 2):
        tv.volume_down()
    assert tv._Television__volume == tv.MIN_VOLUME

def test_string(tv):
    """Tests the __str__ method for accurate representation."""
    assert str(tv) == "TV Status: Power = Off, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "TV Status: Power = On, Channel = 0, Volume = 0"
    tv.mute()
    assert str(tv) == "TV Status: Power = On, Channel = 0, Volume = Muted"
    tv.volume_up()
    assert str(tv) == "TV Status: Power = On, Channel = 0, Volume = 1"
    
