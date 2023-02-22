"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
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


class IpAccessControlListList(ListResource):

    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the IpAccessControlListList

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to read the IP Access Control Lists.
        
        :returns: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListList
        :rtype: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'trunk_sid': trunk_sid,  }
        self._uri = '/Trunks/${trunk_sid}/IpAccessControlLists'.format(**self._solution)
        
        
    
    
    
    def create(self, ip_access_control_list_sid):
        """
        Create the IpAccessControlListInstance
        :param str ip_access_control_list_sid: The SID of the [IP Access Control List](https://www.twilio.com/docs/voice/sip/api/sip-ipaccesscontrollist-resource) that you want to associate with the trunk.
        
        :returns: The created IpAccessControlListInstance
        :rtype: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListInstance
        """
        data = values.of({ 
            'IpAccessControlListSid': ip_access_control_list_sid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return IpAccessControlListInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams IpAccessControlListInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists IpAccessControlListInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of IpAccessControlListInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IpAccessControlListInstance
        :rtype: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return IpAccessControlListPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IpAccessControlListInstance
        :rtype: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return IpAccessControlListPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a IpAccessControlListContext
        
        :param sid: The unique string that we created to identify the IpAccessControlList resource to fetch.
        
        :returns: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListContext
        :rtype: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListContext
        """
        return IpAccessControlListContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a IpAccessControlListContext
        
        :param sid: The unique string that we created to identify the IpAccessControlList resource to fetch.
        
        :returns: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListContext
        :rtype: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListContext
        """
        return IpAccessControlListContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.IpAccessControlListList>'








class IpAccessControlListPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the IpAccessControlListPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListPage
        :rtype: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IpAccessControlListInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListInstance
        :rtype: twilio.rest.trunking.v1.trunk.ip_access_control_list.IpAccessControlListInstance
        """
        return IpAccessControlListInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.IpAccessControlListPage>'





class IpAccessControlListContext(InstanceContext):
    def __init__(self, version: Version, trunk_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'trunk_sid': trunk_sid, 'sid': sid,  }
        self._uri = '/Trunks/${trunk_sid}/IpAccessControlLists/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the IpAccessControlListInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the IpAccessControlListInstance

        :returns: The fetched IpAccessControlListInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return IpAccessControlListInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.IpAccessControlListContext>'



class IpAccessControlListInstance(InstanceResource):
    def __init__(self, version, payload, trunk_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'sid' : payload.get('sid'),
            'trunk_sid' : payload.get('trunk_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'trunk_sid': trunk_sid or self._properties['trunk_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = IpAccessControlListContext(
                self._version,
                trunk_sid=self._solution['trunk_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.IpAccessControlListInstance {}>'.format(context)



