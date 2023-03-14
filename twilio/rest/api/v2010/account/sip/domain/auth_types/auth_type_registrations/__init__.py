r"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values


from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.auth_registrations_credential_list_mapping import AuthRegistrationsCredentialListMappingList


class AuthTypeRegistrationsList(ListResource):

    def __init__(self, version: Version, account_sid: str, domain_sid: str):
        """
        Initialize the AuthTypeRegistrationsList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch.
        :param domain_sid: The SID of the SIP domain that contains the resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.AuthTypeRegistrationsList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.AuthTypeRegistrationsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'domain_sid': domain_sid,  }
        self._uri = '/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations.json'.format(**self._solution)
        
        self._credential_list_mappings = None
        

    @property
    def credential_list_mappings(self):
        """
        Access the credential_list_mappings

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.AuthRegistrationsCredentialListMappingList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_registrations.AuthRegistrationsCredentialListMappingList
        """
        if self._credential_list_mappings is None:
            self._credential_list_mappings = AuthRegistrationsCredentialListMappingList(self._version, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'])
        return self._credential_list_mappings


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthTypeRegistrationsList>'




