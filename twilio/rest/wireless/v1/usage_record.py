"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Wireless
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


class UsageRecordList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the UsageRecordList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.wireless.v1.usage_record.UsageRecordList
        :rtype: twilio.rest.wireless.v1.usage_record.UsageRecordList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/UsageRecords'.format(**self._solution)
        
        
    
    def stream(self, end=values.unset, start=values.unset, granularity=values.unset, limit=None, page_size=None):
        """
        Streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param datetime end: Only include usage that has occurred on or before this date. Format is [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).
        :param datetime start: Only include usage that has occurred on or after this date. Format is [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).
        :param AccountUsageRecordGranularity granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.usage_record.UsageRecordInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            end=end,
            start=start,
            granularity=granularity,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, end=values.unset, start=values.unset, granularity=values.unset, limit=None, page_size=None):
        """
        Lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param datetime end: Only include usage that has occurred on or before this date. Format is [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).
        :param datetime start: Only include usage that has occurred on or after this date. Format is [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).
        :param AccountUsageRecordGranularity granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.usage_record.UsageRecordInstance]
        """
        return list(self.stream(
            end=end,
            start=start,
            granularity=granularity,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, end=values.unset, start=values.unset, granularity=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately
        
        :param datetime end: Only include usage that has occurred on or before this date. Format is [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).
        :param datetime start: Only include usage that has occurred on or after this date. Format is [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).
        :param AccountUsageRecordGranularity granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.wireless.v1.usage_record.UsageRecordPage
        """
        data = values.of({ 
            'End': serialize.iso8601_datetime(end),
            'Start': serialize.iso8601_datetime(start),
            'Granularity': granularity,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return UsageRecordPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.wireless.v1.usage_record.UsageRecordPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UsageRecordPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.UsageRecordList>'


class UsageRecordPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UsageRecordPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.wireless.v1.usage_record.UsageRecordPage
        :rtype: twilio.rest.wireless.v1.usage_record.UsageRecordPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UsageRecordInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.wireless.v1.usage_record.UsageRecordInstance
        :rtype: twilio.rest.wireless.v1.usage_record.UsageRecordInstance
        """
        return UsageRecordInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.UsageRecordPage>'






class UsageRecordInstance(InstanceResource):
    def __init__(self, version, payload):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'period' : payload.get('period'),
            'commands' : payload.get('commands'),
            'data' : payload.get('data'),
        }

        self._context = None
        self._solution = {
            
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = UsageRecordContext(
                self._version,
                
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Wireless.V1.UsageRecordInstance {}>'.format(context)



