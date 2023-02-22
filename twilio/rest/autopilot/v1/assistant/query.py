"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
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


class QueryList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the QueryList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
        
        :returns: twilio.rest.autopilot.v1.assistant.query.QueryList
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        self._uri = '/Assistants/${assistant_sid}/Queries'.format(**self._solution)
        
        
    
    
    
    
    def create(self, language, query, tasks=values.unset, model_build=values.unset):
        """
        Create the QueryInstance
        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the new query. For example: `en-US`.
        :param str query: The end-user's natural language input. It can be up to 2048 characters long.
        :param str tasks: The list of tasks to limit the new query to. Tasks are expressed as a comma-separated list of task `unique_name` values. For example, `task-unique_name-1, task-unique_name-2`. Listing specific tasks is useful to constrain the paths that a user can take.
        :param str model_build: The SID or unique name of the [Model Build](https://www.twilio.com/docs/autopilot/api/model-build) to be queried.
        
        :returns: The created QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        """
        data = values.of({ 
            'Language': language,
            'Query': query,
            'Tasks': tasks,
            'ModelBuild': model_build,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return QueryInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])
    
    
    def stream(self, language=values.unset, model_build=values.unset, status=values.unset, dialogue_sid=values.unset, limit=None, page_size=None):
        """
        Streams QueryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used by the Query resources to read. For example: `en-US`.
        :param str model_build: The SID or unique name of the [Model Build](https://www.twilio.com/docs/autopilot/api/model-build) to be queried.
        :param str status: The status of the resources to read. Can be: `pending-review`, `reviewed`, or `discarded`
        :param str dialogue_sid: The SID of the [Dialogue](https://www.twilio.com/docs/autopilot/api/dialogue).
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.query.QueryInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            language=language,
            model_build=model_build,
            status=status,
            dialogue_sid=dialogue_sid,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, language=values.unset, model_build=values.unset, status=values.unset, dialogue_sid=values.unset, limit=None, page_size=None):
        """
        Lists QueryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used by the Query resources to read. For example: `en-US`.
        :param str model_build: The SID or unique name of the [Model Build](https://www.twilio.com/docs/autopilot/api/model-build) to be queried.
        :param str status: The status of the resources to read. Can be: `pending-review`, `reviewed`, or `discarded`
        :param str dialogue_sid: The SID of the [Dialogue](https://www.twilio.com/docs/autopilot/api/dialogue).
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.query.QueryInstance]
        """
        return list(self.stream(
            language=language,
            model_build=model_build,
            status=status,
            dialogue_sid=dialogue_sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, language=values.unset, model_build=values.unset, status=values.unset, dialogue_sid=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of QueryInstance records from the API.
        Request is executed immediately
        
        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used by the Query resources to read. For example: `en-US`.
        :param str model_build: The SID or unique name of the [Model Build](https://www.twilio.com/docs/autopilot/api/model-build) to be queried.
        :param str status: The status of the resources to read. Can be: `pending-review`, `reviewed`, or `discarded`
        :param str dialogue_sid: The SID of the [Dialogue](https://www.twilio.com/docs/autopilot/api/dialogue).
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryPage
        """
        data = values.of({ 
            'Language': language,
            'ModelBuild': model_build,
            'Status': status,
            'DialogueSid': dialogue_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return QueryPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of QueryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return QueryPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a QueryContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Query resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.query.QueryContext
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryContext
        """
        return QueryContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a QueryContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Query resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.query.QueryContext
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryContext
        """
        return QueryContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.QueryList>'










class QueryPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the QueryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.autopilot.v1.assistant.query.QueryPage
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of QueryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        """
        return QueryInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.QueryPage>'





class QueryContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'sid': sid,  }
        self._uri = '/Assistants/${assistant_sid}/Queries/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the QueryInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the QueryInstance

        :returns: The fetched QueryInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return QueryInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, sample_sid, status):
        data = values.of({
            'sample_sid': sample_sid,'status': status,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return QueryInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.QueryContext>'



class QueryInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'results' : payload.get('results'),
            'language' : payload.get('language'),
            'model_build_sid' : payload.get('model_build_sid'),
            'query' : payload.get('query'),
            'sample_sid' : payload.get('sample_sid'),
            'assistant_sid' : payload.get('assistant_sid'),
            'sid' : payload.get('sid'),
            'status' : payload.get('status'),
            'url' : payload.get('url'),
            'source_channel' : payload.get('source_channel'),
            'dialogue_sid' : payload.get('dialogue_sid'),
        }

        self._context = None
        self._solution = {
            'assistant_sid': assistant_sid or self._properties['assistant_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = QueryContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.QueryInstance {}>'.format(context)



