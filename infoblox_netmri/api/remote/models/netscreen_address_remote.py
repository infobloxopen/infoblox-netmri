from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class NetscreenAddressRemote(RemoteModel):
    """
    This table list out the entries of net screening address of each device.


    |  ``NSAddressID:`` The internal NetMRI identifier of netscreen address.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier of each device from which netscreen address table entry was found.
    |  ``attribute type:`` number

    |  ``NSAddressStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``NSAddressEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``NSAddressTimeStamp:`` The date and time of netscreen address was calculated or collected.
    |  ``attribute type:`` datetime

    |  ``NSAddressChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``NSAddressIndex:`` The current index value of the local interface for the netscreen address.
    |  ``attribute type:`` string

    |  ``NSAddressName:`` The name of the netscreen address.
    |  ``attribute type:`` string

    |  ``NSAddressZone:`` The zone of the netscreen address.
    |  ``attribute type:`` string

    |  ``NSAddressIpDotted:`` The management IP address of the netscreen address is dotted(or colon delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``NSAddressIpNumeric:`` The numerical value of the remote IP address in the netscreen address.
    |  ``attribute type:`` number

    |  ``NSAddressDomainDotted:`` The management Domain IP address of the netscreen address is dotted(or colon delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``NSAddressDomainNumeric:`` The numerical value of Domain IP address in the netscreen address.
    |  ``attribute type:`` number

    |  ``NSAddressNetmaskDotted:`` The management netmask IP address of netscreen address is dotted (or colon delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``NSAddressNetmaskNumeric:`` The numerical value of netmask in the netscreen address.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number




    """

    properties = ("NSAddressID",
                  "DeviceID",
                  "NSAddressStartTime",
                  "NSAddressEndTime",
                  "NSAddressTimeStamp",
                  "NSAddressChangedCols",
                  "NSAddressIndex",
                  "NSAddressName",
                  "NSAddressZone",
                  "NSAddressIpDotted",
                  "NSAddressIpNumeric",
                  "NSAddressDomainDotted",
                  "NSAddressDomainNumeric",
                  "NSAddressNetmaskDotted",
                  "NSAddressNetmaskNumeric",
                  "DataSourceID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"NSAddressID": self.NSAddressID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"NSAddressID": self.NSAddressID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"NSAddressID": self.NSAddressID})
