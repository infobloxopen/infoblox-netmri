from ..remote import RemoteModel


class DataSourceRemote(RemoteModel):
    """
    The NetMRI devices in this deployment.


    |  ``DataSourceID:`` The internal NetMRI identifier for this data source.
    |  ``attribute type:`` number

    |  ``DataSourceStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``DataSourceEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DataSourceChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DataSourceTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``Network:`` The network to which this data source is assigned.
    |  ``attribute type:`` string

    |  ``DataSourceName:`` The name of this data source.
    |  ``attribute type:`` string

    |  ``DataSourceIPDotted:`` The IP address of this data source, in dotted notation.
    |  ``attribute type:`` string

    |  ``DataSourceIPNumeric:`` The numerical IP address of this data source.
    |  ``attribute type:`` number

    |  ``DataSourcePrivateIPDotted:`` Another IP address for the data source, in dotted notation.
    |  ``attribute type:`` string

    |  ``DataSourcePrivateIPNumeric:`` The numerical version of the alternate IP address.
    |  ``attribute type:`` number

    |  ``DataSourceSerialNo:`` The serial number of the collector.
    |  ``attribute type:`` string

    |  ``network_name:`` The name of the Network View associated.
    |  ``attribute type:`` string

    """

    properties = ("DataSourceID",
                  "DataSourceStartTime",
                  "DataSourceEndTime",
                  "DataSourceChangedCols",
                  "DataSourceTimestamp",
                  "Network",
                  "DataSourceName",
                  "DataSourceIPDotted",
                  "DataSourceIPNumeric",
                  "DataSourcePrivateIPDotted",
                  "DataSourcePrivateIPNumeric",
                  "DataSourceSerialNo",
                  "network_name",
                  )
