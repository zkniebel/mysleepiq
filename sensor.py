"""Support for SleepIQ sensors."""
from custom_components import mysleepiq

ICON = "mdi:hotel"


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the SleepIQ sensors."""
    if discovery_info is None:
        return

    data = mysleepiq.DATA
    data.update()

    dev = list()
    for bed_id, bed in data.beds.items():
        for side in mysleepiq.SIDES:
            if getattr(bed, side) is not None:
                dev.append(SleepNumberSensor(data, bed_id, side))
                dev.append(FavoriteSleepNumberSensor(data, bed_id, side))
    add_entities(dev)


class SleepNumberSensor(mysleepiq.SleepIQSensor):
    """Implementation of a SleepIQ sensor."""

    def __init__(self, sleepiq_data, bed_id, side):
        """Initialize the sensor."""
        mysleepiq.SleepIQSensor.__init__(self, sleepiq_data, bed_id, side)

        self._state = None
        self.type = mysleepiq.SLEEP_NUMBER
        self._name = mysleepiq.SENSOR_TYPES[self.type]

        self.update()

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return ICON

    def update(self):
        """Get the latest data from SleepIQ and updates the states."""
        mysleepiq.SleepIQSensor.update(self)
        self._state = self.side.sleep_number

class FavoriteSleepNumberSensor(mysleepiq.SleepIQSensor):
    """Implementation of a SleepIQ sensor."""

    def __init__(self, sleepiq_data, bed_id, side):
        """Initialize the sensor."""
        mysleepiq.SleepIQSensor.__init__(self, sleepiq_data, bed_id, side)

        self._state = None
        self.type = mysleepiq.SLEEP_NUMBER_FAVORITE
        self._name = mysleepiq.SENSOR_TYPES[self.type]

        self.update()

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return ICON

    def update(self):
        """Get the latest data from SleepIQ and updates the states."""
        mysleepiq.SleepIQSensor.update(self)
        self._state = self.fav_sleep_number
