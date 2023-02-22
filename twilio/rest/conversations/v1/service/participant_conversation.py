"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
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


class ParticipantConversationList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the ParticipantConversationList

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant Conversations resource is associated with.
        
        :returns: twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationList
        :rtype: twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        self._uri = '/Services/${chat_service_sid}/ParticipantConversations'.format(**self._solution)
        
        
    
    def stream(self, identity=values.unset, address=values.unset, limit=None, page_size=None):
        """
        Streams ParticipantConversationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str address: A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            identity=identity,
            address=address,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, identity=values.unset, address=values.unset, limit=None, page_size=None):
        """
        Lists ParticipantConversationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str address: A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationInstance]
        """
        return list(self.stream(
            identity=identity,
            address=address,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, identity=values.unset, address=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ParticipantConversationInstance records from the API.
        Request is executed immediately
        
        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str address: A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantConversationInstance
        :rtype: twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationPage
        """
        data = values.of({ 
            'Identity': identity,
            'Address': address,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ParticipantConversationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ParticipantConversationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantConversationInstance
        :rtype: twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ParticipantConversationPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ParticipantConversationList>'


class ParticipantConversationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ParticipantConversationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationPage
        :rtype: twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ParticipantConversationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationInstance
        :rtype: twilio.rest.conversations.v1.service.participant_conversation.ParticipantConversationInstance
        """
        return ParticipantConversationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ParticipantConversationPage>'






class ParticipantConversationInstance(InstanceResource):
    def __init__(self, version, payload, chat_service_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'chat_service_sid' : payload.get('chat_service_sid'),
            'participant_sid' : payload.get('participant_sid'),
            'participant_user_sid' : payload.get('participant_user_sid'),
            'participant_identity' : payload.get('participant_identity'),
            'participant_messaging_binding' : payload.get('participant_messaging_binding'),
            'conversation_sid' : payload.get('conversation_sid'),
            'conversation_unique_name' : payload.get('conversation_unique_name'),
            'conversation_friendly_name' : payload.get('conversation_friendly_name'),
            'conversation_attributes' : payload.get('conversation_attributes'),
            'conversation_date_created' : payload.get('conversation_date_created'),
            'conversation_date_updated' : payload.get('conversation_date_updated'),
            'conversation_created_by' : payload.get('conversation_created_by'),
            'conversation_state' : payload.get('conversation_state'),
            'conversation_timers' : payload.get('conversation_timers'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'chat_service_sid': chat_service_sid or self._properties['chat_service_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ParticipantConversationContext(
                self._version,
                chat_service_sid=self._solution['chat_service_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.ParticipantConversationInstance {}>'.format(context)



