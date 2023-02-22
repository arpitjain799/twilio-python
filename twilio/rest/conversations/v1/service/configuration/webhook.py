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



class WebhookList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the WebhookList

        :param Version version: Version that contains the resource
        :param chat_service_sid: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
        
        :returns: twilio.rest.conversations.v1.service.configuration.webhook.WebhookList
        :rtype: twilio.rest.conversations.v1.service.configuration.webhook.WebhookList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        
        
        
    
    

    def get(self):
        """
        Constructs a WebhookContext
        
        :returns: twilio.rest.conversations.v1.service.configuration.webhook.WebhookContext
        :rtype: twilio.rest.conversations.v1.service.configuration.webhook.WebhookContext
        """
        return WebhookContext(self._version, chat_service_sid=self._solution['chat_service_sid'])

    def __call__(self):
        """
        Constructs a WebhookContext
        
        :returns: twilio.rest.conversations.v1.service.configuration.webhook.WebhookContext
        :rtype: twilio.rest.conversations.v1.service.configuration.webhook.WebhookContext
        """
        return WebhookContext(self._version, chat_service_sid=self._solution['chat_service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.WebhookList>'


class WebhookContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        self._uri = '/Services/${chat_service_sid}/Configuration/Webhooks'
        
    
    def fetch(self):
        
        """
        Fetch the WebhookInstance

        :returns: The fetched WebhookInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WebhookInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], )
        

        
    
    def update(self, pre_webhook_url, post_webhook_url, filters, method):
        data = values.of({
            'pre_webhook_url': pre_webhook_url,'post_webhook_url': post_webhook_url,'filters': filters,'method': method,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return WebhookInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.WebhookContext>'



class WebhookInstance(InstanceResource):
    def __init__(self, version, payload, chat_service_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'chat_service_sid' : payload.get('chat_service_sid'),
            'pre_webhook_url' : payload.get('pre_webhook_url'),
            'post_webhook_url' : payload.get('post_webhook_url'),
            'filters' : payload.get('filters'),
            'method' : payload.get('method'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'chat_service_sid': chat_service_sid or self._properties['chat_service_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WebhookContext(
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
        return '<Twilio.Conversations.V1.WebhookInstance {}>'.format(context)



