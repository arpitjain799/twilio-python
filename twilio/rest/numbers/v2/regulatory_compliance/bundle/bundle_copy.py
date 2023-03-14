r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
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
from twilio.base.page import Page


class BundleCopyList(ListResource):

    def __init__(self, version: Version, bundle_sid: str):
        """
        Initialize the BundleCopyList

        :param Version version: Version that contains the resource
        :param bundle_sid: The unique string that we created to identify the Bundle resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'bundle_sid': bundle_sid,  }
        self._uri = '/RegulatoryCompliance/Bundles/{bundle_sid}/Copies'.format(**self._solution)
        
        
    
    def create(self, friendly_name=values.unset):
        """
        Create the BundleCopyInstance

        :param str friendly_name: The string that you assigned to describe the copied bundle.
        
        :returns: The created BundleCopyInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return BundleCopyInstance(self._version, payload, bundle_sid=self._solution['bundle_sid'])

    async def create_async(self, friendly_name=values.unset):
        """
        Asynchronously create the BundleCopyInstance

        :param str friendly_name: The string that you assigned to describe the copied bundle.
        
        :returns: The created BundleCopyInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return BundleCopyInstance(self._version, payload, bundle_sid=self._solution['bundle_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams BundleCopyInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams BundleCopyInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return await self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists BundleCopyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists BundleCopyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of BundleCopyInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BundleCopyInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return BundleCopyPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronously retrieve a single page of BundleCopyInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BundleCopyInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return BundleCopyPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BundleCopyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BundleCopyInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return BundleCopyPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of BundleCopyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BundleCopyInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return BundleCopyPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.BundleCopyList>'




class BundleCopyPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the BundleCopyPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyPage
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BundleCopyInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance
        """
        return BundleCopyInstance(self._version, payload, bundle_sid=self._solution['bundle_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.BundleCopyPage>'




class BundleCopyInstance(InstanceResource):

    class Status(object):
        DRAFT = "draft"
        PENDING_REVIEW = "pending-review"
        IN_REVIEW = "in-review"
        TWILIO_REJECTED = "twilio-rejected"
        TWILIO_APPROVED = "twilio-approved"
        PROVISIONALLY_APPROVED = "provisionally-approved"

    def __init__(self, version, payload, bundle_sid: str):
        """
        Initialize the BundleCopyInstance
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy.BundleCopyInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'regulation_sid': payload.get('regulation_sid'),
            'friendly_name': payload.get('friendly_name'),
            'status': payload.get('status'),
            'valid_until': deserialize.iso8601_datetime(payload.get('valid_until')),
            'email': payload.get('email'),
            'status_callback': payload.get('status_callback'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        self._context = None
        self._solution = { 'bundle_sid': bundle_sid,  }
    
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Bundle resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Bundle resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def regulation_sid(self):
        """
        :returns: The unique string of a regulation that is associated to the Bundle resource.
        :rtype: str
        """
        return self._properties['regulation_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: BundleCopyInstance.Status
        """
        return self._properties['status']
    
    @property
    def valid_until(self):
        """
        :returns: The date and time in GMT in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format when the resource will be valid until.
        :rtype: datetime
        """
        return self._properties['valid_until']
    
    @property
    def email(self):
        """
        :returns: The email address that will receive updates when the Bundle resource changes status.
        :rtype: str
        """
        return self._properties['email']
    
    @property
    def status_callback(self):
        """
        :returns: The URL we call to inform your application of status changes.
        :rtype: str
        """
        return self._properties['status_callback']
    
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
        return '<Twilio.Numbers.V2.BundleCopyInstance {}>'.format(context)



