"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
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
from twilio.rest.trusthub.v1.trust_products.trust_products_channel_endpoint_assignment import TrustProductsChannelEndpointAssignmentList
from twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments import TrustProductsEntityAssignmentsList
from twilio.rest.trusthub.v1.trust_products.trust_products_evaluations import TrustProductsEvaluationsList


class TrustProductsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the TrustProductsList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.trusthub.v1.trust_products.TrustProductsList
        :rtype: twilio.rest.trusthub.v1.trust_products.TrustProductsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/TrustProducts'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, email, policy_sid, status_callback=values.unset):
        """
        Create the TrustProductsInstance
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str email: The email address that will receive updates when the Customer-Profile resource changes status.
        :param str policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
        :param str status_callback: The URL we call to inform your application of status changes.
        
        :returns: The created TrustProductsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.TrustProductsInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Email': email,
            'PolicySid': policy_sid,
            'StatusCallback': status_callback,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return TrustProductsInstance(self._version, payload)
    
    
    def stream(self, status=values.unset, friendly_name=values.unset, policy_sid=values.unset, limit=None, page_size=None):
        """
        Streams TrustProductsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param TrustProductStatus status: The verification status of the Customer-Profile resource.
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.trust_products.TrustProductsInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            friendly_name=friendly_name,
            policy_sid=policy_sid,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, friendly_name=values.unset, policy_sid=values.unset, limit=None, page_size=None):
        """
        Lists TrustProductsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param TrustProductStatus status: The verification status of the Customer-Profile resource.
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.trust_products.TrustProductsInstance]
        """
        return list(self.stream(
            status=status,
            friendly_name=friendly_name,
            policy_sid=policy_sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, friendly_name=values.unset, policy_sid=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of TrustProductsInstance records from the API.
        Request is executed immediately
        
        :param TrustProductStatus status: The verification status of the Customer-Profile resource.
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str policy_sid: The unique string of a policy that is associated to the Customer-Profile resource.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TrustProductsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.TrustProductsPage
        """
        data = values.of({ 
            'Status': status,
            'FriendlyName': friendly_name,
            'PolicySid': policy_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return TrustProductsPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TrustProductsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TrustProductsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.TrustProductsPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return TrustProductsPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a TrustProductsContext
        
        :param sid: The unique string that we created to identify the Customer-Profile resource.
        
        :returns: twilio.rest.trusthub.v1.trust_products.TrustProductsContext
        :rtype: twilio.rest.trusthub.v1.trust_products.TrustProductsContext
        """
        return TrustProductsContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a TrustProductsContext
        
        :param sid: The unique string that we created to identify the Customer-Profile resource.
        
        :returns: twilio.rest.trusthub.v1.trust_products.TrustProductsContext
        :rtype: twilio.rest.trusthub.v1.trust_products.TrustProductsContext
        """
        return TrustProductsContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.TrustProductsList>'










class TrustProductsPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TrustProductsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trusthub.v1.trust_products.TrustProductsPage
        :rtype: twilio.rest.trusthub.v1.trust_products.TrustProductsPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TrustProductsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trusthub.v1.trust_products.TrustProductsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.TrustProductsInstance
        """
        return TrustProductsInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.TrustProductsPage>'





class TrustProductsContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/TrustProducts/${sid}'
        
        self._trust_products_channel_endpoint_assignment = None
        self._trust_products_entity_assignments = None
        self._trust_products_evaluations = None
    
    def delete(self):
        
        

        """
        Deletes the TrustProductsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the TrustProductsInstance

        :returns: The fetched TrustProductsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TrustProductsInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, status, status_callback, friendly_name, email):
        data = values.of({
            'status': status,'status_callback': status_callback,'friendly_name': friendly_name,'email': email,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return TrustProductsInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.TrustProductsContext>'



class TrustProductsInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'policy_sid' : payload.get('policy_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'status' : payload.get('status'),
            'valid_until' : payload.get('valid_until'),
            'email' : payload.get('email'),
            'status_callback' : payload.get('status_callback'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TrustProductsContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def trust_products_channel_endpoint_assignment(self):
        return self._proxy.trust_products_channel_endpoint_assignment
    @property
    def trust_products_entity_assignments(self):
        return self._proxy.trust_products_entity_assignments
    @property
    def trust_products_evaluations(self):
        return self._proxy.trust_products_evaluations
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.TrustProductsInstance {}>'.format(context)



