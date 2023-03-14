r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class RecordingRulesList(ListResource):

    def __init__(self, version: Version, room_sid: str):
        """
        Initialize the RecordingRulesList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room resource where the recording rules to update apply.
        
        :returns: twilio.rest.video.v1.room.recording_rules.RecordingRulesList
        :rtype: twilio.rest.video.v1.room.recording_rules.RecordingRulesList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid,  }
        self._uri = '/Rooms/{room_sid}/RecordingRules'.format(**self._solution)
        
        
    
    def fetch(self):
        """
        Asynchronously fetch the RecordingRulesInstance

        :returns: The fetched RecordingRulesInstance
        :rtype: twilio.rest.video.v1.room.recording_rules.RecordingRulesInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return RecordingRulesInstance(self._version, payload, room_sid=self._solution['room_sid'])

    async def fetch_async(self):
        """
        Asynchronously fetch the RecordingRulesInstance

        :returns: The fetched RecordingRulesInstance
        :rtype: twilio.rest.video.v1.room.recording_rules.RecordingRulesInstance
        """
        payload = await self._version.fetch_async(method='GET', uri=self._uri)

        return RecordingRulesInstance(self._version, payload, room_sid=self._solution['room_sid'])
    
    
    def update(self, rules=values.unset):
        """
        Update the RecordingRulesInstance

        :param object rules: A JSON-encoded array of recording rules.
        
        :returns: The created RecordingRulesInstance
        :rtype: twilio.rest.video.v1.room.recording_rules.RecordingRulesInstance
        """
        data = values.of({ 
            'Rules': serialize.object(rules),
        })
        
        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return RecordingRulesInstance(self._version, payload, room_sid=self._solution['room_sid'])

    async def update_async(self, rules=values.unset):
        """
        Asynchronously update the RecordingRulesInstance

        :param object rules: A JSON-encoded array of recording rules.
        
        :returns: The created RecordingRulesInstance
        :rtype: twilio.rest.video.v1.room.recording_rules.RecordingRulesInstance
        """
        data = values.of({ 
            'Rules': serialize.object(rules),
        })
        
        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return RecordingRulesInstance(self._version, payload, room_sid=self._solution['room_sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RecordingRulesList>'

class RecordingRulesInstance(InstanceResource):

    def __init__(self, version, payload, room_sid: str):
        """
        Initialize the RecordingRulesInstance
        :returns: twilio.rest.video.v1.room.recording_rules.RecordingRulesInstance
        :rtype: twilio.rest.video.v1.room.recording_rules.RecordingRulesInstance
        """
        super().__init__(version)

        self._properties = { 
            'room_sid': payload.get('room_sid'),
            'rules': payload.get('rules'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        self._context = None
        self._solution = { 'room_sid': room_sid,  }
    
    
    @property
    def room_sid(self):
        """
        :returns: The SID of the Room resource for the Recording Rules
        :rtype: str
        """
        return self._properties['room_sid']
    
    @property
    def rules(self):
        """
        :returns: A collection of Recording Rules that describe how to include or exclude matching tracks for recording
        :rtype: list[VideoV1RoomRoomRecordingRuleRules]
        """
        return self._properties['rules']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RecordingRulesInstance {}>'.format(context)



