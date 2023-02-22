"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
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



class CallSummaryList(ListResource):

    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the CallSummaryList

        :param Version version: Version that contains the resource
        :param call_sid: 
        
        :returns: twilio.rest.insights.v1.call.call_summary.CallSummaryList
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'call_sid': call_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a CallSummaryContext
        
        :returns: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        """
        return CallSummaryContext(self._version, call_sid=self._solution['call_sid'])

    def __call__(self):
        """
        Constructs a CallSummaryContext
        
        :returns: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        :rtype: twilio.rest.insights.v1.call.call_summary.CallSummaryContext
        """
        return CallSummaryContext(self._version, call_sid=self._solution['call_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallSummaryList>'


class CallSummaryContext(InstanceContext):
    def __init__(self, version: Version, call_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'call_sid': call_sid,  }
        self._uri = '/Voice/${call_sid}/Summary'
        
    
    def fetch(self, processing_state):
        
        """
        Fetch the CallSummaryInstance

        :returns: The fetched CallSummaryInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CallSummaryInstance(self._version, payload, call_sid=self._solution['call_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallSummaryContext>'



class CallSummaryInstance(InstanceResource):
    def __init__(self, version, payload, call_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'call_sid' : payload.get('call_sid'),
            'call_type' : payload.get('call_type'),
            'call_state' : payload.get('call_state'),
            'answered_by' : payload.get('answered_by'),
            'processing_state' : payload.get('processing_state'),
            'created_time' : payload.get('created_time'),
            'start_time' : payload.get('start_time'),
            'end_time' : payload.get('end_time'),
            'duration' : payload.get('duration'),
            'connect_duration' : payload.get('connect_duration'),
            '_from' : payload.get('from'),
            'to' : payload.get('to'),
            'carrier_edge' : payload.get('carrier_edge'),
            'client_edge' : payload.get('client_edge'),
            'sdk_edge' : payload.get('sdk_edge'),
            'sip_edge' : payload.get('sip_edge'),
            'tags' : payload.get('tags'),
            'url' : payload.get('url'),
            'attributes' : payload.get('attributes'),
            'properties' : payload.get('properties'),
            'trust' : payload.get('trust'),
            'annotation' : payload.get('annotation'),
        }

        self._context = None
        self._solution = {
            'call_sid': call_sid or self._properties['call_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = CallSummaryContext(
                self._version,
                call_sid=self._solution['call_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.CallSummaryInstance {}>'.format(context)



