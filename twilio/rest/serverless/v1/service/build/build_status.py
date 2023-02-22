"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
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



class BuildStatusList(ListResource):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BuildStatusList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Build resource from.
        :param sid: The SID of the Build resource to fetch.
        
        :returns: twilio.rest.serverless.v1.service.build.build_status.BuildStatusList
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'sid': sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a BuildStatusContext
        
        :returns: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        """
        return BuildStatusContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'])

    def __call__(self):
        """
        Constructs a BuildStatusContext
        
        :returns: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        """
        return BuildStatusContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.BuildStatusList>'


class BuildStatusContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Builds/${sid}/Status'
        
    
    def fetch(self):
        
        """
        Fetch the BuildStatusInstance

        :returns: The fetched BuildStatusInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BuildStatusInstance(self._version, payload, service_sid=self._solution['service_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.BuildStatusContext>'



class BuildStatusInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'status' : payload.get('status'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = BuildStatusContext(
                self._version,
                service_sid=self._solution['service_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildStatusInstance {}>'.format(context)



