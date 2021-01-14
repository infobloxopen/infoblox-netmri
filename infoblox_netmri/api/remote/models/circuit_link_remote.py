from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class CircuitLinkRemote(RemoteModel):
    """
    This table list out all the entries of Circuit Link.


    |  ``CLinkID:`` The internal NetMRI identifier of the Circuit Link.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which Circuit Link entry was collected or found.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``CLinkStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``CLinkEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``CLinkTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``CLinkChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``CLinkIndex:`` The index of the interface in the Circuit Link.
    |  ``attribute type:`` string

    |  ``CLinkIfIndex:`` The SNMP index for the local interface for this Circuit Link table entry.
    |  ``attribute type:`` string

    |  ``InterfaceID:`` The internal NetMRI identifier for the local interface for this Circuit Link table entry.
    |  ``attribute type:`` number

    |  ``CLinkOverallState:`` The overall state of the Circuit Link which is defined within the NetMRI.
    |  ``attribute type:`` string

    |  ``CLinkDTGNumber:`` The NetMRI-determined a DTGNumber in the circuit link.
    |  ``attribute type:`` string

    |  ``CLinkTGCNumber:`` The NetMRI-determined a TGCNumber in the circuit link.
    |  ``attribute type:`` string

    |  ``CLinkNodeType:`` The NetMRI-determined node type of the CircuitLink.
    |  ``attribute type:`` string

    |  ``CLinkTransmissionType:`` The NetMRI-determined transmission type of the Circuit Link Entry.
    |  ``attribute type:`` string

    |  ``CLinkParentID:`` The internal NetMRI identifier for each parent device in the Circuit Link.
    |  ``attribute type:`` number

    |  ``CLinkSwitchCode:`` The NetMRI-determined switch code of the Circuit Link.
    |  ``attribute type:`` string




    """

    properties = ("CLinkID",
                  "DeviceID",
                  "DataSourceID",
                  "CLinkStartTime",
                  "CLinkEndTime",
                  "CLinkTimestamp",
                  "CLinkChangedCols",
                  "CLinkIndex",
                  "CLinkIfIndex",
                  "InterfaceID",
                  "CLinkOverallState",
                  "CLinkDTGNumber",
                  "CLinkTGCNumber",
                  "CLinkNodeType",
                  "CLinkTransmissionType",
                  "CLinkParentID",
                  "CLinkSwitchCode",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"CLinkID": self.CLinkID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"CLinkID": self.CLinkID})

    @property
    @check_api_availability
    def interface(self):
        """
        interface
        ``attribute type:`` model
        """
        return self.broker.interface(**{"CLinkID": self.CLinkID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"CLinkID": self.CLinkID})
