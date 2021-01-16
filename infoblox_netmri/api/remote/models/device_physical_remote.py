from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DevicePhysicalRemote(RemoteModel):
    """
    Physical device components (chassis, module, port, etc.)


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device containing this component.
    |  ``attribute type:`` number

    |  ``DevicePhysicalID:`` The internal NetMRI identifier for this physical component.
    |  ``attribute type:`` number

    |  ``PhysicalAlias:`` This is an 'alias' name for the physical entity, as specified by a network manager, and provides a non-volatile 'handle' for the physical entity. Note that NetMRI does not currently allow setting of this value; use the device's console for that purpose.
    |  ``attribute type:`` string

    |  ``PhysicalAssetID:`` This object is a user-assigned asset tracking identifier (as specified by a network manager) for the physical entity, and provides non-volatile storage of this information. Note that NetMRI does not currently allow setting of this value; use the device's console for that purpose.
    |  ``attribute type:`` string

    |  ``PhysicalChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``PhysicalClass:`` An indication of the general hardware type of the physical entity.
    |  ``attribute type:`` string

    |  ``PhysicalContainedIn:`` The value of PhysicalIndex (SNMP Index) for the physical entity which 'contains' this physical entity. A value of zero indicates this physical entity is not contained in any other physical entity. Note that the set of 'containment' relationships define a strict hierarchy; that is, recursion is not allowed.

In the event that a physical entity is contained by more than one physical entity (e.g., double-wide modules), this object should identify the containing entity with the lowest value of PhysicalIndex (SNMP Index).
    |  ``attribute type:`` number

    |  ``PhysicalDescr:`` A textual description of physical entity. This object should contain a string that identifies the manufacturer's name for the physical entity, and should be set to a distinct value for each version or model of the physical entity.
    |  ``attribute type:`` string

    |  ``PhysicalEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``PhysicalFirmwareRev:`` The vendor-specific firmware revision string for the physical entity.
    |  ``attribute type:`` string

    |  ``PhysicalHardwareRev:`` The vendor-specific hardware revision string for the physical entity. The preferred value is the hardware revision identifier actually printed on the component itself (if present).
    |  ``attribute type:`` string

    |  ``PhysicalIndex:`` A unique index for this specific component within the device.
    |  ``attribute type:`` number

    |  ``PhysicalMfgName:`` The name of the manufacturer of this physical component.  The preferred value is the manufacturer name string actually printed on the component itself (if present).
    |  ``attribute type:`` string

    |  ``PhysicalModelName:`` The vendor-specific model name identifier string associated with this physical component. The preferred value is the customer-visible part number, which may be printed on the component itself.
    |  ``attribute type:`` string

    |  ``PhysicalName:`` The textual name of the physical entity. This is the name of the component as assigned by the local device and should be suitable for use in commands entered at the device's console.
    |  ``attribute type:`` string

    |  ``PhysicalParentRelPos:`` An indication of the relative position of this 'child' component among all its 'sibling' components. Sibling components are defined as components that share the same values of each of the PhysicalContainedIn and PhysicalClass attributes. If possible, this value should match any external labeling of the physical component.
    |  ``attribute type:`` number

    |  ``PhysicalSerialNum:`` The vendor-specific serial number string for the physical entity. The preferred value is the serial number string actually printed on the component itself (if present).
    |  ``attribute type:`` string

    |  ``PhysicalSoftwareRev:`` The vendor-specific software revision string for the physical entity.
    |  ``attribute type:`` string

    |  ``PhysicalStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``PhysicalTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``PhysicalVendorType:`` An indication of the vendor-specific hardware type of the physical entity.
    |  ``attribute type:`` string

    |  ``UnitState:`` The vendor-specific operational state of the physical component.
    |  ``attribute type:`` string




    |  ``network_id:`` The Network View ID assigned to this component.
    |  ``attribute type:`` number


    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "DevicePhysicalID",
                  "PhysicalAlias",
                  "PhysicalAssetID",
                  "PhysicalChangedCols",
                  "PhysicalClass",
                  "PhysicalContainedIn",
                  "PhysicalDescr",
                  "PhysicalEndTime",
                  "PhysicalFirmwareRev",
                  "PhysicalHardwareRev",
                  "PhysicalIndex",
                  "PhysicalMfgName",
                  "PhysicalModelName",
                  "PhysicalName",
                  "PhysicalParentRelPos",
                  "PhysicalSerialNum",
                  "PhysicalSoftwareRev",
                  "PhysicalStartTime",
                  "PhysicalTimestamp",
                  "PhysicalVendorType",
                  "UnitState",
                  "network_id",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DevicePhysicalID": self.DevicePhysicalID})

    @property
    @check_api_availability
    def device(self):
        """
        The device containing this component.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DevicePhysicalID": self.DevicePhysicalID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device containing this component.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DevicePhysicalID": self.DevicePhysicalID})

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"DevicePhysicalID": self.DevicePhysicalID})
