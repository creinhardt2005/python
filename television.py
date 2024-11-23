class Television:
    """Class that models Television with defaults for power, mute, volume, and channel."""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Sets up the Television with initial settings."""
        self.status: bool = False
        self.muted: bool = False
        self.volume: int = self.MIN_VOLUME
        self.channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """Toggles the TV's power state."""
        if self.status:
            self.muted = False
        self.status = not self.status

    def mute(self) -> None:
        """Toggles mute when the TV is on."""
        if self.status:
            self.muted = self.muted is False

    def channel_up(self) -> None:
        """Switches channel forward, looping to MIN_CHANNEL first.."""
        if self.status:
            self.channel = self.MIN_CHANNEL if self.channel == self.MAX_CHANNEL else self.channel + 1

    def channel_down(self) -> None:
        """Switches channel backward, looping to MAX_CHANNEL first."""
        if self.status:
            self.channel = self.MAX_CHANNEL if self.channel == self.MIN_CHANNEL else self.channel - 1

    def volume_up(self) -> None:
        """Raises the volume by 1 within limits and unmutes if muted."""
        if self.status:
            if self.muted:
                self.muted = False
            self.volume = min(self.volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """Lowers the volume by 1 within limits and unmutes if muted."""
        if self.status:
            if self.muted:
                self.muted = False
            self.volume = max(self.volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        """Returns description of the Television's current state."""
        power_status = "On" if self.status else "Off"
        volume_display = "Muted" if self.muted else self.volume
        return f"Power = {power_status}, Channel = {self.channel}, Volume = {volume_display}"
