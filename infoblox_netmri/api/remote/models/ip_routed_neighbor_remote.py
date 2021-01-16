from ..remote import RemoteModel


class IpRoutedNeighborRemote(RemoteModel):
    """
    Neighbor relationships between devices as defined by device routing tables.  There is one per route carried over the neighbor relationship.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceRouteID:`` The internal NetMRI identifier for the route which this record references.
    |  ``attribute type:`` number

    |  ``IPRoutedNeighborChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``IPRoutedNeighborEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``IPRoutedNeighborID:`` The internal NetMRI identifier for this neighbor/route relationship.
    |  ``attribute type:`` number

    |  ``IPRoutedNeighborMapSource:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``IPRoutedNeighborStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``IPRoutedNeighborTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``NeighborID:`` The internal NetMRI identifier of the corresponding neighbor record for this relationship.
    |  ``attribute type:`` number

    """

    properties = ("DataSourceID",
                  "DeviceRouteID",
                  "IPRoutedNeighborChangedCols",
                  "IPRoutedNeighborEndTime",
                  "IPRoutedNeighborID",
                  "IPRoutedNeighborMapSource",
                  "IPRoutedNeighborStartTime",
                  "IPRoutedNeighborTimestamp",
                  "NeighborID",
                  )
