"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Bulkexports
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



class JobList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the JobList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.bulkexports.v1.export.job.JobList
        :rtype: twilio.rest.bulkexports.v1.export.job.JobList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self, job_sid):
        """
        Constructs a JobContext
        
        :param job_sid: The unique string that that we created to identify the Bulk Export job
        
        :returns: twilio.rest.bulkexports.v1.export.job.JobContext
        :rtype: twilio.rest.bulkexports.v1.export.job.JobContext
        """
        return JobContext(self._version, job_sid=job_sid)

    def __call__(self, job_sid):
        """
        Constructs a JobContext
        
        :param job_sid: The unique string that that we created to identify the Bulk Export job
        
        :returns: twilio.rest.bulkexports.v1.export.job.JobContext
        :rtype: twilio.rest.bulkexports.v1.export.job.JobContext
        """
        return JobContext(self._version, job_sid=job_sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Bulkexports.V1.JobList>'


class JobContext(InstanceContext):
    def __init__(self, version: Version, job_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'job_sid': job_sid,  }
        self._uri = '/Exports/Jobs/${job_sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the JobInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the JobInstance

        :returns: The fetched JobInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return JobInstance(self._version, payload, job_sid=self._solution['job_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Bulkexports.V1.JobContext>'



class JobInstance(InstanceResource):
    def __init__(self, version, payload, job_sid: str):
        super().__init__(version)
        self._properties = { 
            'resource_type' : payload.get('resource_type'),
            'friendly_name' : payload.get('friendly_name'),
            'details' : payload.get('details'),
            'start_day' : payload.get('start_day'),
            'end_day' : payload.get('end_day'),
            'job_sid' : payload.get('job_sid'),
            'webhook_url' : payload.get('webhook_url'),
            'webhook_method' : payload.get('webhook_method'),
            'email' : payload.get('email'),
            'url' : payload.get('url'),
            'job_queue_position' : payload.get('job_queue_position'),
            'estimated_completion_time' : payload.get('estimated_completion_time'),
        }

        self._context = None
        self._solution = {
            'job_sid': job_sid or self._properties['job_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = JobContext(
                self._version,
                job_sid=self._solution['job_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Bulkexports.V1.JobInstance {}>'.format(context)



