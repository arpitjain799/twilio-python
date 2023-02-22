"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class EventList(ListResource):

    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the EventList

        :param Version version: Version that contains the resource
        :param account_sid: The unique SID identifier of the Account.
        :param call_sid: The unique SID identifier of the Call.
        
        :returns: twilio.rest.api.v2010.account.call.event.EventList
        :rtype: twilio.rest.api.v2010.account.call.event.EventList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid,  }
        self._uri = '/Accounts/${account_sid}/Calls/${call_sid}/Events.json'.format(**self._solution)
        
        
    
    def stream(self, limit=None, page_size=None):
        """
        Streams EventInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.event.EventInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists EventInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.event.EventInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of EventInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EventInstance
        :rtype: twilio.rest.api.v2010.account.call.event.EventPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return EventPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EventInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EventInstance
        :rtype: twilio.rest.api.v2010.account.call.event.EventPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return EventPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.EventList>'


class EventPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the EventPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.call.event.EventPage
        :rtype: twilio.rest.api.v2010.account.call.event.EventPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EventInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.call.event.EventInstance
        :rtype: twilio.rest.api.v2010.account.call.event.EventInstance
        """
        return EventInstance(self._version, payload, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.EventPage>'






class EventInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, call_sid: str):
        super().__init__(version)
        self._properties = { 
            'request' : payload.get('request'),
            'response' : payload.get('response'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'call_sid': call_sid or self._properties['call_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = EventContext(
                self._version,
                account_sid=self._solution['account_sid'],call_sid=self._solution['call_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.EventInstance {}>'.format(context)



