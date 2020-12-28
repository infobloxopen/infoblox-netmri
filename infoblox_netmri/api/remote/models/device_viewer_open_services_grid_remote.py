from ..remote import RemoteModel


class DeviceViewerOpenServicesGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DataSourceID:`` none
    |  ``attribute type:`` string

    |  ``ipaddress:`` none
    |  ``attribute type:`` string

    |  ``ListenAddr:`` none
    |  ``attribute type:`` string

    |  ``PortProtocol:`` none
    |  ``attribute type:`` string

    |  ``Port:`` none
    |  ``attribute type:`` string

    |  ``ExpectedService:`` none
    |  ``attribute type:`` string

    |  ``Service:`` none
    |  ``attribute type:`` string

    |  ``PortTimestamp:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DataSourceID",
                  "ipaddress",
                  "ListenAddr",
                  "PortProtocol",
                  "Port",
                  "ExpectedService",
                  "Service",
                  "PortTimestamp",
                  )
