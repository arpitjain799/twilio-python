"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
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



class WorkersCumulativeStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkersCumulativeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the resource to fetch.
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a WorkersCumulativeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        return WorkersCumulativeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __call__(self):
        """
        Constructs a WorkersCumulativeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        return WorkersCumulativeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsList>'


class WorkersCumulativeStatisticsContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workers/CumulativeStatistics'
        
    
    def fetch(self, end_date, minutes, start_date, task_channel):
        
        """
        Fetch the WorkersCumulativeStatisticsInstance

        :returns: The fetched WorkersCumulativeStatisticsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WorkersCumulativeStatisticsInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsContext>'



class WorkersCumulativeStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'start_time' : payload.get('start_time'),
            'end_time' : payload.get('end_time'),
            'activity_durations' : payload.get('activity_durations'),
            'reservations_created' : payload.get('reservations_created'),
            'reservations_accepted' : payload.get('reservations_accepted'),
            'reservations_rejected' : payload.get('reservations_rejected'),
            'reservations_timed_out' : payload.get('reservations_timed_out'),
            'reservations_canceled' : payload.get('reservations_canceled'),
            'reservations_rescinded' : payload.get('reservations_rescinded'),
            'workspace_sid' : payload.get('workspace_sid'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WorkersCumulativeStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsInstance {}>'.format(context)



