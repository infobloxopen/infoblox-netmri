from ..remote import RemoteModel


class SdnNetworkRemote(RemoteModel):
    """
    This table list out networks collected from SDN controllers.


    |  ``sdn_network_id:`` The internal NetMRI identifier for this network
    |  ``attribute type:`` number

    |  ``sdn_network_key:`` The unique identifier of each network at the SDN controller side
    |  ``attribute type:`` string

    |  ``sdn_network_name:`` Name of SDN network
    |  ``attribute type:`` string

    |  ``fabric_id:`` Identifier of SdnSetting from which this network was collected
    |  ``attribute type:`` number

    |  ``virtual_network_id:`` ID of Virtual Network which is assigned to this network
    |  ``attribute type:`` number

    |  ``StartTime:`` The starting date/time of this network
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The ending date/time of this network
    |  ``attribute type:`` datetime

    |  ``fabric_handle:`` Name of SDN controller from which this network was collected.
    |  ``attribute type:`` string

    """

    properties = ("sdn_network_id",
                  "sdn_network_key",
                  "sdn_network_name",
                  "fabric_id",
                  "virtual_network_id",
                  "StartTime",
                  "EndTime",
                  "fabric_handle",
                  )
