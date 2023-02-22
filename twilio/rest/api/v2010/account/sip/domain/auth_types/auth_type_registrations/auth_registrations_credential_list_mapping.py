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


class AuthRegistrationsCredentialListMappingList(ListResource):

    def __init__(self, version: Version, account_sid: str, domain_sid: str):
        """
        Initialize the AuthRegistrationsCredentialListMappingList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read.
        :param domain_sid: The SID of the SIP domain that contains the resources to read.
        
        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'domain_sid': domain_sid,  }
        self._uri = '/Accounts/${account_sid}/SIP/Domains/${domain_sid}/Auth/Registrations/CredentialListMappings.json'.format(**self._solution)
        
        
    
    
    
    def create(self, credential_list_sid):
        """
        Create the AuthRegistrationsCredentialListMappingInstance
        :param str credential_list_sid: The SID of the CredentialList resource to map to the SIP domain.
        
        :returns: The created AuthRegistrationsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingInstance
        """
        data = values.of({ 
            'CredentialListSid': credential_list_sid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return AuthRegistrationsCredentialListMappingInstance(self._version, payload, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AuthRegistrationsCredentialListMappingInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AuthRegistrationsCredentialListMappingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AuthRegistrationsCredentialListMappingInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthRegistrationsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AuthRegistrationsCredentialListMappingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AuthRegistrationsCredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthRegistrationsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AuthRegistrationsCredentialListMappingPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AuthRegistrationsCredentialListMappingContext
        
        :param sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingContext
        """
        return AuthRegistrationsCredentialListMappingContext(self._version, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a AuthRegistrationsCredentialListMappingContext
        
        :param sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingContext
        """
        return AuthRegistrationsCredentialListMappingContext(self._version, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthRegistrationsCredentialListMappingList>'








class AuthRegistrationsCredentialListMappingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AuthRegistrationsCredentialListMappingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingPage
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AuthRegistrationsCredentialListMappingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping.AuthRegistrationsCredentialListMappingInstance
        """
        return AuthRegistrationsCredentialListMappingInstance(self._version, payload, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthRegistrationsCredentialListMappingPage>'





class AuthRegistrationsCredentialListMappingContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, domain_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'domain_sid': domain_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/SIP/Domains/${domain_sid}/Auth/Registrations/CredentialListMappings/${sid}.json'
        
    
    def delete(self):
        
        

        """
        Deletes the AuthRegistrationsCredentialListMappingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the AuthRegistrationsCredentialListMappingInstance

        :returns: The fetched AuthRegistrationsCredentialListMappingInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AuthRegistrationsCredentialListMappingInstance(self._version, payload, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthRegistrationsCredentialListMappingContext>'



class AuthRegistrationsCredentialListMappingInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, domain_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'friendly_name' : payload.get('friendly_name'),
            'sid' : payload.get('sid'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'domain_sid': domain_sid or self._properties['domain_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AuthRegistrationsCredentialListMappingContext(
                self._version,
                account_sid=self._solution['account_sid'],domain_sid=self._solution['domain_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AuthRegistrationsCredentialListMappingInstance {}>'.format(context)



