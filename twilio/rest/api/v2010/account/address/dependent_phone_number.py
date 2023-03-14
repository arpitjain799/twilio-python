r"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DependentPhoneNumberList(ListResource):

    def __init__(self, version: Version, account_sid: str, address_sid: str):
        """
        Initialize the DependentPhoneNumberList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the DependentPhoneNumber resources to read.
        :param address_sid: The SID of the Address resource associated with the phone number.
        
        :returns: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberList
        :rtype: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'address_sid': address_sid,  }
        self._uri = '/Accounts/{account_sid}/Addresses/{address_sid}/DependentPhoneNumbers.json'.format(**self._solution)
        
        
    
    def stream(self, limit=None, page_size=None):
        """
        Streams DependentPhoneNumberInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams DependentPhoneNumberInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return await self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DependentPhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists DependentPhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DependentPhoneNumberInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DependentPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return DependentPhoneNumberPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronously retrieve a single page of DependentPhoneNumberInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DependentPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return DependentPhoneNumberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DependentPhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DependentPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return DependentPhoneNumberPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of DependentPhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DependentPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return DependentPhoneNumberPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.DependentPhoneNumberList>'


class DependentPhoneNumberPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the DependentPhoneNumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberPage
        :rtype: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DependentPhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberInstance
        """
        return DependentPhoneNumberInstance(self._version, payload, account_sid=self._solution['account_sid'], address_sid=self._solution['address_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.DependentPhoneNumberPage>'




class DependentPhoneNumberInstance(InstanceResource):

    class AddressRequirement(object):
        NONE = "none"
        ANY = "any"
        LOCAL = "local"
        FOREIGN = "foreign"

    class EmergencyStatus(object):
        ACTIVE = "Active"
        INACTIVE = "Inactive"

    def __init__(self, version, payload, account_sid: str, address_sid: str):
        """
        Initialize the DependentPhoneNumberInstance
        :returns: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberInstance
        :rtype: twilio.rest.api.v2010.account.address.dependent_phone_number.DependentPhoneNumberInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'phone_number': payload.get('phone_number'),
            'voice_url': payload.get('voice_url'),
            'voice_method': payload.get('voice_method'),
            'voice_fallback_method': payload.get('voice_fallback_method'),
            'voice_fallback_url': payload.get('voice_fallback_url'),
            'voice_caller_id_lookup': payload.get('voice_caller_id_lookup'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'sms_fallback_method': payload.get('sms_fallback_method'),
            'sms_fallback_url': payload.get('sms_fallback_url'),
            'sms_method': payload.get('sms_method'),
            'sms_url': payload.get('sms_url'),
            'address_requirements': payload.get('address_requirements'),
            'capabilities': payload.get('capabilities'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'api_version': payload.get('api_version'),
            'sms_application_sid': payload.get('sms_application_sid'),
            'voice_application_sid': payload.get('voice_application_sid'),
            'trunk_sid': payload.get('trunk_sid'),
            'emergency_status': payload.get('emergency_status'),
            'emergency_address_sid': payload.get('emergency_address_sid'),
            'uri': payload.get('uri'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'address_sid': address_sid,  }
    
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the DependentPhoneNumber resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the DependentPhoneNumber resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def phone_number(self):
        """
        :returns: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        :rtype: str
        """
        return self._properties['phone_number']
    
    @property
    def voice_url(self):
        """
        :returns: The URL we call when the phone number receives a call. The `voice_url` will not be used if a `voice_application_sid` or a `trunk_sid` is set.
        :rtype: str
        """
        return self._properties['voice_url']
    
    @property
    def voice_method(self):
        """
        :returns: The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['voice_method']
    
    @property
    def voice_fallback_method(self):
        """
        :returns: The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['voice_fallback_method']
    
    @property
    def voice_fallback_url(self):
        """
        :returns: The URL that we call when an error occurs retrieving or executing the TwiML requested by `url`.
        :rtype: str
        """
        return self._properties['voice_fallback_url']
    
    @property
    def voice_caller_id_lookup(self):
        """
        :returns: Whether we look up the caller's caller-ID name from the CNAM database. Can be: `true` or `false`. Caller ID lookups can cost $0.01 each.
        :rtype: bool
        """
        return self._properties['voice_caller_id_lookup']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def sms_fallback_method(self):
        """
        :returns: The HTTP method we use to call `sms_fallback_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['sms_fallback_method']
    
    @property
    def sms_fallback_url(self):
        """
        :returns: The URL that we call when an error occurs while retrieving or executing the TwiML from `sms_url`.
        :rtype: str
        """
        return self._properties['sms_fallback_url']
    
    @property
    def sms_method(self):
        """
        :returns: The HTTP method we use to call `sms_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['sms_method']
    
    @property
    def sms_url(self):
        """
        :returns: The URL we call when the phone number receives an incoming SMS message.
        :rtype: str
        """
        return self._properties['sms_url']
    
    @property
    def address_requirements(self):
        """
        :returns: 
        :rtype: DependentPhoneNumberInstance.AddressRequirement
        """
        return self._properties['address_requirements']
    
    @property
    def capabilities(self):
        """
        :returns: The set of Boolean properties that indicates whether a phone number can receive calls or messages.  Capabilities are  `Voice`, `SMS`, and `MMS` and each capability can be: `true` or `false`.
        :rtype: dict
        """
        return self._properties['capabilities']
    
    @property
    def status_callback(self):
        """
        :returns: The URL we call using the `status_callback_method` to send status information to your application.
        :rtype: str
        """
        return self._properties['status_callback']
    
    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method we use to call `status_callback`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['status_callback_method']
    
    @property
    def api_version(self):
        """
        :returns: The API version used to start a new TwiML session.
        :rtype: str
        """
        return self._properties['api_version']
    
    @property
    def sms_application_sid(self):
        """
        :returns: The SID of the application that handles SMS messages sent to the phone number. If an `sms_application_sid` is present, we ignore all `sms_*_url` values and use those of the application.
        :rtype: str
        """
        return self._properties['sms_application_sid']
    
    @property
    def voice_application_sid(self):
        """
        :returns: The SID of the application that handles calls to the phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
        :rtype: str
        """
        return self._properties['voice_application_sid']
    
    @property
    def trunk_sid(self):
        """
        :returns: The SID of the Trunk that handles calls to the phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
        :rtype: str
        """
        return self._properties['trunk_sid']
    
    @property
    def emergency_status(self):
        """
        :returns: 
        :rtype: DependentPhoneNumberInstance.EmergencyStatus
        """
        return self._properties['emergency_status']
    
    @property
    def emergency_address_sid(self):
        """
        :returns: The SID of the emergency address configuration that we use for emergency calling from the phone number.
        :rtype: str
        """
        return self._properties['emergency_address_sid']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.DependentPhoneNumberInstance {}>'.format(context)



