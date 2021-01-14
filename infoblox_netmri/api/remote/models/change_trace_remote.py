from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class ChangeTraceRemote(RemoteModel):
    """
    The individual pieces of change evidence for a specific detected change.


    |  ``ChangeID:`` The internal NetMRI identifier for the change associated with this change trace.
    |  ``attribute type:`` number

    |  ``ChangeTraceDesc:`` A description of the change trace.
    |  ``attribute type:`` string

    |  ``ChangeTraceID:`` The internal NetMRI identifier for this change trace.
    |  ``attribute type:`` number

    |  ``ChangeTraceMethod:`` The method through which this change trace was identified.
    |  ``attribute type:`` string

    |  ``ChangeTraceTime:`` The date/time that this change trace was identified by NetMRI.
    |  ``attribute type:`` datetime

    |  ``ChangeTraceType:`` The type of change trace (Hardware, Software, Admin, or External).
    |  ``attribute type:`` string

    |  ``ChangeTraceUser:`` The user name of the user whose actions generated this change trace, if available.
    |  ``attribute type:`` string

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``ifIndex:`` Currently unused.
    |  ``attribute type:`` number



    """

    properties = ("ChangeID",
                  "ChangeTraceDesc",
                  "ChangeTraceID",
                  "ChangeTraceMethod",
                  "ChangeTraceTime",
                  "ChangeTraceType",
                  "ChangeTraceUser",
                  "DataSourceID",
                  "ifIndex",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"ChangeTraceID": self.ChangeTraceID})

    @property
    @check_api_availability
    def detected_change(self):
        """
        The DetectedChange object to which this change trace contributed.
        ``attribute type:`` model
        """
        return self.broker.detected_change(**{"ChangeTraceID": self.ChangeTraceID})
