class Television:
    """Class that models Television with defaults for power, mute, volume, and channel."""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Sets up the Television with initial settings."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """Toggles the TV's power state."""
        if self.__status:
            self.__muted = False
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggles mute when the TV is on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Switches channel forward, looping to MIN_CHANNEL first."""
        if self.__status:
            self.__channel = self.MIN_CHANNEL if self.__channel == self.MAX_CHANNEL else self.__channel + 1

    def channel_down(self) -> None:
        """Switches channel backward, looping to MAX_CHANNEL first."""
        if self.__status:
            self.__channel = self.MAX_CHANNEL if self.__channel == self.MIN_CHANNEL else self.__channel - 1

    def volume_up(self) -> None:
        """Raises the volume by 1 within limits and unmutes if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """Lowers the volume by 1 within limits and unmutes if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        """Returns description of the Television's current state."""
        power_status = "On" if self.__status else "Off"
        volume_display = "Muted" if self.__muted else self.__volume
        return f"TV Status: Power = {power_status}, Channel = {self.__channel}, Volume = {volume_display}"
