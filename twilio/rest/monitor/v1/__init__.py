r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Monitor
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.monitor.v1.alert import AlertList
from twilio.rest.monitor.v1.event import EventList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Monitor

        :param domain: The Twilio.monitor domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._alerts = None
        self._events = None
        
    @property
    def alerts(self) -> AlertList:
        """
        :rtype: twilio.rest.monitor.v1.alert.AlertList
        """
        if self._alerts is None:
            self._alerts = AlertList(self)
        return self._alerts

    @property
    def events(self) -> EventList:
        """
        :rtype: twilio.rest.monitor.v1.event.EventList
        """
        if self._events is None:
            self._events = EventList(self)
        return self._events

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Monitor.V1>'
