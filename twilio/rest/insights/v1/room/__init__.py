"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.insights.v1.room.participants import ParticipantList


class RoomList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the RoomList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.insights.v1.room.RoomList
        :rtype: twilio.rest.insights.v1.room.RoomList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Video/Rooms'.format(**self._solution)
        
        
    
    
    def stream(self, room_type=values.unset, codec=values.unset, room_name=values.unset, created_after=values.unset, created_before=values.unset, limit=None, page_size=None):
        """
        Streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param list[VideoRoomSummaryRoomType] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param list[VideoRoomSummaryCodec] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.room.RoomInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            room_type=room_type,
            codec=codec,
            room_name=room_name,
            created_after=created_after,
            created_before=created_before,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, room_type=values.unset, codec=values.unset, room_name=values.unset, created_after=values.unset, created_before=values.unset, limit=None, page_size=None):
        """
        Lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param list[VideoRoomSummaryRoomType] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param list[VideoRoomSummaryCodec] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.room.RoomInstance]
        """
        return list(self.stream(
            room_type=room_type,
            codec=codec,
            room_name=room_name,
            created_after=created_after,
            created_before=created_before,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, room_type=values.unset, codec=values.unset, room_name=values.unset, created_after=values.unset, created_before=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RoomInstance records from the API.
        Request is executed immediately
        
        :param list[VideoRoomSummaryRoomType] room_type: Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
        :param list[VideoRoomSummaryCodec] codec: Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
        :param str room_name: Room friendly name.
        :param datetime created_after: Only read rooms that started on or after this ISO 8601 timestamp.
        :param datetime created_before: Only read rooms that started before this ISO 8601 timestamp.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomPage
        """
        data = values.of({ 
            'RoomType': room_type,
            'Codec': codec,
            'RoomName': room_name,
            'CreatedAfter': serialize.iso8601_datetime(created_after),
            'CreatedBefore': serialize.iso8601_datetime(created_before),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RoomPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RoomPage(self._version, response, self._solution)


    def get(self, room_sid):
        """
        Constructs a RoomContext
        
        :param room_sid: The SID of the Room resource.
        
        :returns: twilio.rest.insights.v1.room.RoomContext
        :rtype: twilio.rest.insights.v1.room.RoomContext
        """
        return RoomContext(self._version, room_sid=room_sid)

    def __call__(self, room_sid):
        """
        Constructs a RoomContext
        
        :param room_sid: The SID of the Room resource.
        
        :returns: twilio.rest.insights.v1.room.RoomContext
        :rtype: twilio.rest.insights.v1.room.RoomContext
        """
        return RoomContext(self._version, room_sid=room_sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.RoomList>'




class RoomPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RoomPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.room.RoomPage
        :rtype: twilio.rest.insights.v1.room.RoomPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RoomInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.room.RoomInstance
        :rtype: twilio.rest.insights.v1.room.RoomInstance
        """
        return RoomInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.RoomPage>'





class RoomContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid,  }
        self._uri = '/Video/Rooms/${room_sid}'
        
        self._participants = None
    
    def fetch(self):
        
        """
        Fetch the RoomInstance

        :returns: The fetched RoomInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RoomInstance(self._version, payload, room_sid=self._solution['room_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.RoomContext>'



class RoomInstance(InstanceResource):
    def __init__(self, version, payload, room_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'room_sid' : payload.get('room_sid'),
            'room_name' : payload.get('room_name'),
            'create_time' : payload.get('create_time'),
            'end_time' : payload.get('end_time'),
            'room_type' : payload.get('room_type'),
            'room_status' : payload.get('room_status'),
            'status_callback' : payload.get('status_callback'),
            'status_callback_method' : payload.get('status_callback_method'),
            'created_method' : payload.get('created_method'),
            'end_reason' : payload.get('end_reason'),
            'max_participants' : payload.get('max_participants'),
            'unique_participants' : payload.get('unique_participants'),
            'unique_participant_identities' : payload.get('unique_participant_identities'),
            'concurrent_participants' : payload.get('concurrent_participants'),
            'max_concurrent_participants' : payload.get('max_concurrent_participants'),
            'codecs' : payload.get('codecs'),
            'media_region' : payload.get('media_region'),
            'duration_sec' : payload.get('duration_sec'),
            'total_participant_duration_sec' : payload.get('total_participant_duration_sec'),
            'total_recording_duration_sec' : payload.get('total_recording_duration_sec'),
            'processing_state' : payload.get('processing_state'),
            'recording_enabled' : payload.get('recording_enabled'),
            'edge_location' : payload.get('edge_location'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'room_sid': room_sid or self._properties['room_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = RoomContext(
                self._version,
                room_sid=self._solution['room_sid'],
            )
        return self._context

    @property
    def participants(self):
        return self._proxy.participants
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.RoomInstance {}>'.format(context)



