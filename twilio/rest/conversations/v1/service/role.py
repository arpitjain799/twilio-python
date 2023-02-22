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


class RoleList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the RoleList

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to read the Role resources from.
        
        :returns: twilio.rest.conversations.v1.service.role.RoleList
        :rtype: twilio.rest.conversations.v1.service.role.RoleList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        self._uri = '/Services/${chat_service_sid}/Roles'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, type, permission):
        """
        Create the RoleInstance
        :param str friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
        :param ServiceRoleRoleType type: 
        :param list[str] permission: A permission that you grant to the new role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. The values for this parameter depend on the role's `type`.
        
        :returns: The created RoleInstance
        :rtype: twilio.rest.conversations.v1.service.role.RoleInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Type': type,
            'Permission': serialize.map(permission, lambda e: e),
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return RoleInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams RoleInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.conversations.v1.service.role.RoleInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists RoleInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.role.RoleInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RoleInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoleInstance
        :rtype: twilio.rest.conversations.v1.service.role.RolePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RolePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RoleInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoleInstance
        :rtype: twilio.rest.conversations.v1.service.role.RolePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RolePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a RoleContext
        
        :param sid: The SID of the Role resource to update.
        
        :returns: twilio.rest.conversations.v1.service.role.RoleContext
        :rtype: twilio.rest.conversations.v1.service.role.RoleContext
        """
        return RoleContext(self._version, chat_service_sid=self._solution['chat_service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a RoleContext
        
        :param sid: The SID of the Role resource to update.
        
        :returns: twilio.rest.conversations.v1.service.role.RoleContext
        :rtype: twilio.rest.conversations.v1.service.role.RoleContext
        """
        return RoleContext(self._version, chat_service_sid=self._solution['chat_service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.RoleList>'










class RolePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RolePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.service.role.RolePage
        :rtype: twilio.rest.conversations.v1.service.role.RolePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RoleInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.service.role.RoleInstance
        :rtype: twilio.rest.conversations.v1.service.role.RoleInstance
        """
        return RoleInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.RolePage>'





class RoleContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid, 'sid': sid,  }
        self._uri = '/Services/${chat_service_sid}/Roles/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the RoleInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the RoleInstance

        :returns: The fetched RoleInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RoleInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, permission):
        data = values.of({
            'permission': permission,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return RoleInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.RoleContext>'



class RoleInstance(InstanceResource):
    def __init__(self, version, payload, chat_service_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'chat_service_sid' : payload.get('chat_service_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'type' : payload.get('type'),
            'permissions' : payload.get('permissions'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'chat_service_sid': chat_service_sid or self._properties['chat_service_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = RoleContext(
                self._version,
                chat_service_sid=self._solution['chat_service_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.RoleInstance {}>'.format(context)



