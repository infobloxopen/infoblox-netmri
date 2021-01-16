from ..broker import Broker


class DevicePhysicalBroker(Broker):
    controller = "device_physicals"

    def show(self, **kwargs):
        """Shows the details for the specified device physical.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device physical methods. The listed methods will be called on each device physical returned and included in the output. Available methods are: meta, network_id, data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_physical: The device physical identified by the specified DevicePhysicalID.
             :rtype device_physical: DevicePhysical

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device physicals. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing this component.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing this component.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the device physicals as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device physical methods. The listed methods will be called on each device physical returned and included in the output. Available methods are: meta, network_id, data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source.
             :type include: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` DevicePhysicalID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePhysicalID. Valid values are DevicePhysicalID, DataSourceID, DeviceID, PhysicalIndex, PhysicalStartTime, PhysicalEndTime, PhysicalChangedCols, PhysicalTimestamp, PhysicalDescr, PhysicalVendorType, PhysicalContainedIn, PhysicalClass, PhysicalParentRelPos, PhysicalName, PhysicalHardwareRev, PhysicalFirmwareRev, PhysicalSoftwareRev, PhysicalSerialNum, PhysicalMfgName, PhysicalModelName, PhysicalAlias, PhysicalAssetID, UnitState.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each DevicePhysical. Valid values are DevicePhysicalID, DataSourceID, DeviceID, PhysicalIndex, PhysicalStartTime, PhysicalEndTime, PhysicalChangedCols, PhysicalTimestamp, PhysicalDescr, PhysicalVendorType, PhysicalContainedIn, PhysicalClass, PhysicalParentRelPos, PhysicalName, PhysicalHardwareRev, PhysicalFirmwareRev, PhysicalSoftwareRev, PhysicalSerialNum, PhysicalMfgName, PhysicalModelName, PhysicalAlias, PhysicalAssetID, UnitState. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_physicals: An array of the DevicePhysical objects that match the specified input criteria.
             :rtype device_physicals: Array of DevicePhysical

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device physicals matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing this component.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing this component.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalAlias: This is an 'alias' name for the physical entity, as specified by a network manager, and provides a non-volatile 'handle' for the physical entity. Note that NetMRI does not currently allow setting of this value; use the device's console for that purpose.
             :type PhysicalAlias: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalAlias: This is an 'alias' name for the physical entity, as specified by a network manager, and provides a non-volatile 'handle' for the physical entity. Note that NetMRI does not currently allow setting of this value; use the device's console for that purpose.
             :type PhysicalAlias: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalAssetID: This object is a user-assigned asset tracking identifier (as specified by a network manager) for the physical entity, and provides non-volatile storage of this information. Note that NetMRI does not currently allow setting of this value; use the device's console for that purpose.
             :type PhysicalAssetID: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalAssetID: This object is a user-assigned asset tracking identifier (as specified by a network manager) for the physical entity, and provides non-volatile storage of this information. Note that NetMRI does not currently allow setting of this value; use the device's console for that purpose.
             :type PhysicalAssetID: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type PhysicalChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type PhysicalChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalClass: An indication of the general hardware type of the physical entity.
             :type PhysicalClass: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalClass: An indication of the general hardware type of the physical entity.
             :type PhysicalClass: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalContainedIn: The value of PhysicalIndex (SNMP Index) for the physical entity which 'contains' this physical entity. A value of zero indicates this physical entity is not contained in any other physical entity. Note that the set of 'containment' relationships define a strict hierarchy; that is, recursion is not allowed.

In the event that a physical entity is contained by more than one physical entity (e.g., double-wide modules), this object should identify the containing entity with the lowest value of PhysicalIndex (SNMP Index).
             :type PhysicalContainedIn: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalContainedIn: The value of PhysicalIndex (SNMP Index) for the physical entity which 'contains' this physical entity. A value of zero indicates this physical entity is not contained in any other physical entity. Note that the set of 'containment' relationships define a strict hierarchy; that is, recursion is not allowed.

In the event that a physical entity is contained by more than one physical entity (e.g., double-wide modules), this object should identify the containing entity with the lowest value of PhysicalIndex (SNMP Index).
             :type PhysicalContainedIn: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalDescr: A textual description of physical entity. This object should contain a string that identifies the manufacturer's name for the physical entity, and should be set to a distinct value for each version or model of the physical entity.
             :type PhysicalDescr: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalDescr: A textual description of physical entity. This object should contain a string that identifies the manufacturer's name for the physical entity, and should be set to a distinct value for each version or model of the physical entity.
             :type PhysicalDescr: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type PhysicalEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type PhysicalEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalFirmwareRev: The vendor-specific firmware revision string for the physical entity.
             :type PhysicalFirmwareRev: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalFirmwareRev: The vendor-specific firmware revision string for the physical entity.
             :type PhysicalFirmwareRev: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalHardwareRev: The vendor-specific hardware revision string for the physical entity. The preferred value is the hardware revision identifier actually printed on the component itself (if present).
             :type PhysicalHardwareRev: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalHardwareRev: The vendor-specific hardware revision string for the physical entity. The preferred value is the hardware revision identifier actually printed on the component itself (if present).
             :type PhysicalHardwareRev: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalIndex: A unique index for this specific component within the device.
             :type PhysicalIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalIndex: A unique index for this specific component within the device.
             :type PhysicalIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalMfgName: The name of the manufacturer of this physical component.  The preferred value is the manufacturer name string actually printed on the component itself (if present).
             :type PhysicalMfgName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalMfgName: The name of the manufacturer of this physical component.  The preferred value is the manufacturer name string actually printed on the component itself (if present).
             :type PhysicalMfgName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalModelName: The vendor-specific model name identifier string associated with this physical component. The preferred value is the customer-visible part number, which may be printed on the component itself.
             :type PhysicalModelName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalModelName: The vendor-specific model name identifier string associated with this physical component. The preferred value is the customer-visible part number, which may be printed on the component itself.
             :type PhysicalModelName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalName: The textual name of the physical entity. This is the name of the component as assigned by the local device and should be suitable for use in commands entered at the device's console.
             :type PhysicalName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalName: The textual name of the physical entity. This is the name of the component as assigned by the local device and should be suitable for use in commands entered at the device's console.
             :type PhysicalName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalParentRelPos: An indication of the relative position of this 'child' component among all its 'sibling' components. Sibling components are defined as components that share the same values of each of the PhysicalContainedIn and PhysicalClass attributes. If possible, this value should match any external labeling of the physical component.
             :type PhysicalParentRelPos: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalParentRelPos: An indication of the relative position of this 'child' component among all its 'sibling' components. Sibling components are defined as components that share the same values of each of the PhysicalContainedIn and PhysicalClass attributes. If possible, this value should match any external labeling of the physical component.
             :type PhysicalParentRelPos: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalSerialNum: The vendor-specific serial number string for the physical entity. The preferred value is the serial number string actually printed on the component itself (if present).
             :type PhysicalSerialNum: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalSerialNum: The vendor-specific serial number string for the physical entity. The preferred value is the serial number string actually printed on the component itself (if present).
             :type PhysicalSerialNum: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalSoftwareRev: The vendor-specific software revision string for the physical entity.
             :type PhysicalSoftwareRev: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalSoftwareRev: The vendor-specific software revision string for the physical entity.
             :type PhysicalSoftwareRev: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalStartTime: The starting effective time of this revision of the record.
             :type PhysicalStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalStartTime: The starting effective time of this revision of the record.
             :type PhysicalStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalTimestamp: The date and time this record was collected or calculated.
             :type PhysicalTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalTimestamp: The date and time this record was collected or calculated.
             :type PhysicalTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalVendorType: An indication of the vendor-specific hardware type of the physical entity.
             :type PhysicalVendorType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalVendorType: An indication of the vendor-specific hardware type of the physical entity.
             :type PhysicalVendorType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UnitState: The vendor-specific operational state of the physical component.
             :type UnitState: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitState: The vendor-specific operational state of the physical component.
             :type UnitState: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the device physicals as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device physical methods. The listed methods will be called on each device physical returned and included in the output. Available methods are: meta, network_id, data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source.
             :type include: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` DevicePhysicalID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePhysicalID. Valid values are DevicePhysicalID, DataSourceID, DeviceID, PhysicalIndex, PhysicalStartTime, PhysicalEndTime, PhysicalChangedCols, PhysicalTimestamp, PhysicalDescr, PhysicalVendorType, PhysicalContainedIn, PhysicalClass, PhysicalParentRelPos, PhysicalName, PhysicalHardwareRev, PhysicalFirmwareRev, PhysicalSoftwareRev, PhysicalSerialNum, PhysicalMfgName, PhysicalModelName, PhysicalAlias, PhysicalAssetID, UnitState.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each DevicePhysical. Valid values are DevicePhysicalID, DataSourceID, DeviceID, PhysicalIndex, PhysicalStartTime, PhysicalEndTime, PhysicalChangedCols, PhysicalTimestamp, PhysicalDescr, PhysicalVendorType, PhysicalContainedIn, PhysicalClass, PhysicalParentRelPos, PhysicalName, PhysicalHardwareRev, PhysicalFirmwareRev, PhysicalSoftwareRev, PhysicalSerialNum, PhysicalMfgName, PhysicalModelName, PhysicalAlias, PhysicalAssetID, UnitState. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: This value will be matched against device physicals, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, DevicePhysicalID, PhysicalAlias, PhysicalAssetID, PhysicalChangedCols, PhysicalClass, PhysicalContainedIn, PhysicalDescr, PhysicalEndTime, PhysicalFirmwareRev, PhysicalHardwareRev, PhysicalIndex, PhysicalMfgName, PhysicalModelName, PhysicalName, PhysicalParentRelPos, PhysicalSerialNum, PhysicalSoftwareRev, PhysicalStartTime, PhysicalTimestamp, PhysicalVendorType, UnitState.
             :type query: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_physicals: An array of the DevicePhysical objects that match the specified input criteria.
             :rtype device_physicals: Array of DevicePhysical

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device physicals matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, DevicePhysicalID, PhysicalAlias, PhysicalAssetID, PhysicalChangedCols, PhysicalClass, PhysicalContainedIn, PhysicalDescr, PhysicalEndTime, PhysicalFirmwareRev, PhysicalHardwareRev, PhysicalIndex, PhysicalMfgName, PhysicalModelName, PhysicalName, PhysicalParentRelPos, PhysicalSerialNum, PhysicalSoftwareRev, PhysicalStartTime, PhysicalTimestamp, PhysicalVendorType, UnitState.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceID: The operator to apply to the field DataSourceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceID: If op_DataSourceID is specified, the field named in this input will be compared to the value in DataSourceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_f_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceID: If op_DataSourceID is specified, this value will be compared to the value in DataSourceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_c_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device containing this component. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceID: If op_DeviceID is specified, the field named in this input will be compared to the value in DeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceID must be specified if op_DeviceID is specified.
             :type val_f_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceID: If op_DeviceID is specified, this value will be compared to the value in DeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceID must be specified if op_DeviceID is specified.
             :type val_c_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePhysicalID: The operator to apply to the field DevicePhysicalID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePhysicalID: The internal NetMRI identifier for this physical component. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePhysicalID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePhysicalID: If op_DevicePhysicalID is specified, the field named in this input will be compared to the value in DevicePhysicalID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePhysicalID must be specified if op_DevicePhysicalID is specified.
             :type val_f_DevicePhysicalID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePhysicalID: If op_DevicePhysicalID is specified, this value will be compared to the value in DevicePhysicalID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePhysicalID must be specified if op_DevicePhysicalID is specified.
             :type val_c_DevicePhysicalID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalAlias: The operator to apply to the field PhysicalAlias. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalAlias: This is an 'alias' name for the physical entity, as specified by a network manager, and provides a non-volatile 'handle' for the physical entity. Note that NetMRI does not currently allow setting of this value; use the device's console for that purpose. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalAlias: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalAlias: If op_PhysicalAlias is specified, the field named in this input will be compared to the value in PhysicalAlias using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalAlias must be specified if op_PhysicalAlias is specified.
             :type val_f_PhysicalAlias: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalAlias: If op_PhysicalAlias is specified, this value will be compared to the value in PhysicalAlias using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalAlias must be specified if op_PhysicalAlias is specified.
             :type val_c_PhysicalAlias: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalAssetID: The operator to apply to the field PhysicalAssetID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalAssetID: This object is a user-assigned asset tracking identifier (as specified by a network manager) for the physical entity, and provides non-volatile storage of this information. Note that NetMRI does not currently allow setting of this value; use the device's console for that purpose. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalAssetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalAssetID: If op_PhysicalAssetID is specified, the field named in this input will be compared to the value in PhysicalAssetID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalAssetID must be specified if op_PhysicalAssetID is specified.
             :type val_f_PhysicalAssetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalAssetID: If op_PhysicalAssetID is specified, this value will be compared to the value in PhysicalAssetID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalAssetID must be specified if op_PhysicalAssetID is specified.
             :type val_c_PhysicalAssetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalChangedCols: The operator to apply to the field PhysicalChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalChangedCols: If op_PhysicalChangedCols is specified, the field named in this input will be compared to the value in PhysicalChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalChangedCols must be specified if op_PhysicalChangedCols is specified.
             :type val_f_PhysicalChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalChangedCols: If op_PhysicalChangedCols is specified, this value will be compared to the value in PhysicalChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalChangedCols must be specified if op_PhysicalChangedCols is specified.
             :type val_c_PhysicalChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalClass: The operator to apply to the field PhysicalClass. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalClass: An indication of the general hardware type of the physical entity. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalClass: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalClass: If op_PhysicalClass is specified, the field named in this input will be compared to the value in PhysicalClass using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalClass must be specified if op_PhysicalClass is specified.
             :type val_f_PhysicalClass: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalClass: If op_PhysicalClass is specified, this value will be compared to the value in PhysicalClass using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalClass must be specified if op_PhysicalClass is specified.
             :type val_c_PhysicalClass: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalContainedIn: The operator to apply to the field PhysicalContainedIn. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalContainedIn: The value of PhysicalIndex (SNMP Index) for the physical entity which 'contains' this physical entity. A value of zero indicates this physical entity is not contained in any other physical entity. Note that the set of 'containment' relationships define a strict hierarchy; that is, recursion is not allowed.

In the event that a physical entity is contained by more than one physical entity (e.g., double-wide modules), this object should identify the containing entity with the lowest value of PhysicalIndex (SNMP Index). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalContainedIn: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalContainedIn: If op_PhysicalContainedIn is specified, the field named in this input will be compared to the value in PhysicalContainedIn using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalContainedIn must be specified if op_PhysicalContainedIn is specified.
             :type val_f_PhysicalContainedIn: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalContainedIn: If op_PhysicalContainedIn is specified, this value will be compared to the value in PhysicalContainedIn using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalContainedIn must be specified if op_PhysicalContainedIn is specified.
             :type val_c_PhysicalContainedIn: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalDescr: The operator to apply to the field PhysicalDescr. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalDescr: A textual description of physical entity. This object should contain a string that identifies the manufacturer's name for the physical entity, and should be set to a distinct value for each version or model of the physical entity. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalDescr: If op_PhysicalDescr is specified, the field named in this input will be compared to the value in PhysicalDescr using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalDescr must be specified if op_PhysicalDescr is specified.
             :type val_f_PhysicalDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalDescr: If op_PhysicalDescr is specified, this value will be compared to the value in PhysicalDescr using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalDescr must be specified if op_PhysicalDescr is specified.
             :type val_c_PhysicalDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalEndTime: The operator to apply to the field PhysicalEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalEndTime: If op_PhysicalEndTime is specified, the field named in this input will be compared to the value in PhysicalEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalEndTime must be specified if op_PhysicalEndTime is specified.
             :type val_f_PhysicalEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalEndTime: If op_PhysicalEndTime is specified, this value will be compared to the value in PhysicalEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalEndTime must be specified if op_PhysicalEndTime is specified.
             :type val_c_PhysicalEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalFirmwareRev: The operator to apply to the field PhysicalFirmwareRev. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalFirmwareRev: The vendor-specific firmware revision string for the physical entity. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalFirmwareRev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalFirmwareRev: If op_PhysicalFirmwareRev is specified, the field named in this input will be compared to the value in PhysicalFirmwareRev using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalFirmwareRev must be specified if op_PhysicalFirmwareRev is specified.
             :type val_f_PhysicalFirmwareRev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalFirmwareRev: If op_PhysicalFirmwareRev is specified, this value will be compared to the value in PhysicalFirmwareRev using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalFirmwareRev must be specified if op_PhysicalFirmwareRev is specified.
             :type val_c_PhysicalFirmwareRev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalHardwareRev: The operator to apply to the field PhysicalHardwareRev. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalHardwareRev: The vendor-specific hardware revision string for the physical entity. The preferred value is the hardware revision identifier actually printed on the component itself (if present). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalHardwareRev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalHardwareRev: If op_PhysicalHardwareRev is specified, the field named in this input will be compared to the value in PhysicalHardwareRev using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalHardwareRev must be specified if op_PhysicalHardwareRev is specified.
             :type val_f_PhysicalHardwareRev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalHardwareRev: If op_PhysicalHardwareRev is specified, this value will be compared to the value in PhysicalHardwareRev using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalHardwareRev must be specified if op_PhysicalHardwareRev is specified.
             :type val_c_PhysicalHardwareRev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalIndex: The operator to apply to the field PhysicalIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalIndex: A unique index for this specific component within the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalIndex: If op_PhysicalIndex is specified, the field named in this input will be compared to the value in PhysicalIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalIndex must be specified if op_PhysicalIndex is specified.
             :type val_f_PhysicalIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalIndex: If op_PhysicalIndex is specified, this value will be compared to the value in PhysicalIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalIndex must be specified if op_PhysicalIndex is specified.
             :type val_c_PhysicalIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalMfgName: The operator to apply to the field PhysicalMfgName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalMfgName: The name of the manufacturer of this physical component.  The preferred value is the manufacturer name string actually printed on the component itself (if present). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalMfgName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalMfgName: If op_PhysicalMfgName is specified, the field named in this input will be compared to the value in PhysicalMfgName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalMfgName must be specified if op_PhysicalMfgName is specified.
             :type val_f_PhysicalMfgName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalMfgName: If op_PhysicalMfgName is specified, this value will be compared to the value in PhysicalMfgName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalMfgName must be specified if op_PhysicalMfgName is specified.
             :type val_c_PhysicalMfgName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalModelName: The operator to apply to the field PhysicalModelName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalModelName: The vendor-specific model name identifier string associated with this physical component. The preferred value is the customer-visible part number, which may be printed on the component itself. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalModelName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalModelName: If op_PhysicalModelName is specified, the field named in this input will be compared to the value in PhysicalModelName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalModelName must be specified if op_PhysicalModelName is specified.
             :type val_f_PhysicalModelName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalModelName: If op_PhysicalModelName is specified, this value will be compared to the value in PhysicalModelName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalModelName must be specified if op_PhysicalModelName is specified.
             :type val_c_PhysicalModelName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalName: The operator to apply to the field PhysicalName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalName: The textual name of the physical entity. This is the name of the component as assigned by the local device and should be suitable for use in commands entered at the device's console. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalName: If op_PhysicalName is specified, the field named in this input will be compared to the value in PhysicalName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalName must be specified if op_PhysicalName is specified.
             :type val_f_PhysicalName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalName: If op_PhysicalName is specified, this value will be compared to the value in PhysicalName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalName must be specified if op_PhysicalName is specified.
             :type val_c_PhysicalName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalParentRelPos: The operator to apply to the field PhysicalParentRelPos. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalParentRelPos: An indication of the relative position of this 'child' component among all its 'sibling' components. Sibling components are defined as components that share the same values of each of the PhysicalContainedIn and PhysicalClass attributes. If possible, this value should match any external labeling of the physical component. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalParentRelPos: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalParentRelPos: If op_PhysicalParentRelPos is specified, the field named in this input will be compared to the value in PhysicalParentRelPos using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalParentRelPos must be specified if op_PhysicalParentRelPos is specified.
             :type val_f_PhysicalParentRelPos: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalParentRelPos: If op_PhysicalParentRelPos is specified, this value will be compared to the value in PhysicalParentRelPos using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalParentRelPos must be specified if op_PhysicalParentRelPos is specified.
             :type val_c_PhysicalParentRelPos: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalSerialNum: The operator to apply to the field PhysicalSerialNum. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalSerialNum: The vendor-specific serial number string for the physical entity. The preferred value is the serial number string actually printed on the component itself (if present). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalSerialNum: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalSerialNum: If op_PhysicalSerialNum is specified, the field named in this input will be compared to the value in PhysicalSerialNum using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalSerialNum must be specified if op_PhysicalSerialNum is specified.
             :type val_f_PhysicalSerialNum: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalSerialNum: If op_PhysicalSerialNum is specified, this value will be compared to the value in PhysicalSerialNum using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalSerialNum must be specified if op_PhysicalSerialNum is specified.
             :type val_c_PhysicalSerialNum: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalSoftwareRev: The operator to apply to the field PhysicalSoftwareRev. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalSoftwareRev: The vendor-specific software revision string for the physical entity. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalSoftwareRev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalSoftwareRev: If op_PhysicalSoftwareRev is specified, the field named in this input will be compared to the value in PhysicalSoftwareRev using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalSoftwareRev must be specified if op_PhysicalSoftwareRev is specified.
             :type val_f_PhysicalSoftwareRev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalSoftwareRev: If op_PhysicalSoftwareRev is specified, this value will be compared to the value in PhysicalSoftwareRev using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalSoftwareRev must be specified if op_PhysicalSoftwareRev is specified.
             :type val_c_PhysicalSoftwareRev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalStartTime: The operator to apply to the field PhysicalStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalStartTime: If op_PhysicalStartTime is specified, the field named in this input will be compared to the value in PhysicalStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalStartTime must be specified if op_PhysicalStartTime is specified.
             :type val_f_PhysicalStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalStartTime: If op_PhysicalStartTime is specified, this value will be compared to the value in PhysicalStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalStartTime must be specified if op_PhysicalStartTime is specified.
             :type val_c_PhysicalStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalTimestamp: The operator to apply to the field PhysicalTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalTimestamp: If op_PhysicalTimestamp is specified, the field named in this input will be compared to the value in PhysicalTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalTimestamp must be specified if op_PhysicalTimestamp is specified.
             :type val_f_PhysicalTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalTimestamp: If op_PhysicalTimestamp is specified, this value will be compared to the value in PhysicalTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalTimestamp must be specified if op_PhysicalTimestamp is specified.
             :type val_c_PhysicalTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PhysicalVendorType: The operator to apply to the field PhysicalVendorType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalVendorType: An indication of the vendor-specific hardware type of the physical entity. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalVendorType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalVendorType: If op_PhysicalVendorType is specified, the field named in this input will be compared to the value in PhysicalVendorType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalVendorType must be specified if op_PhysicalVendorType is specified.
             :type val_f_PhysicalVendorType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalVendorType: If op_PhysicalVendorType is specified, this value will be compared to the value in PhysicalVendorType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalVendorType must be specified if op_PhysicalVendorType is specified.
             :type val_c_PhysicalVendorType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UnitState: The operator to apply to the field UnitState. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UnitState: The vendor-specific operational state of the physical component. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UnitState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UnitState: If op_UnitState is specified, the field named in this input will be compared to the value in UnitState using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UnitState must be specified if op_UnitState is specified.
             :type val_f_UnitState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UnitState: If op_UnitState is specified, this value will be compared to the value in UnitState using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UnitState must be specified if op_UnitState is specified.
             :type val_c_UnitState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_network_id: The operator to apply to the field network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. network_id: The Network View ID assigned to this component. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_network_id: If op_network_id is specified, the field named in this input will be compared to the value in network_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_network_id must be specified if op_network_id is specified.
             :type val_f_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_network_id: If op_network_id is specified, this value will be compared to the value in network_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_network_id must be specified if op_network_id is specified.
             :type val_c_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the device physicals as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device physical methods. The listed methods will be called on each device physical returned and included in the output. Available methods are: meta, network_id, data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source.
             :type include: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` DevicePhysicalID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePhysicalID. Valid values are DevicePhysicalID, DataSourceID, DeviceID, PhysicalIndex, PhysicalStartTime, PhysicalEndTime, PhysicalChangedCols, PhysicalTimestamp, PhysicalDescr, PhysicalVendorType, PhysicalContainedIn, PhysicalClass, PhysicalParentRelPos, PhysicalName, PhysicalHardwareRev, PhysicalFirmwareRev, PhysicalSoftwareRev, PhysicalSerialNum, PhysicalMfgName, PhysicalModelName, PhysicalAlias, PhysicalAssetID, UnitState.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each DevicePhysical. Valid values are DevicePhysicalID, DataSourceID, DeviceID, PhysicalIndex, PhysicalStartTime, PhysicalEndTime, PhysicalChangedCols, PhysicalTimestamp, PhysicalDescr, PhysicalVendorType, PhysicalContainedIn, PhysicalClass, PhysicalParentRelPos, PhysicalName, PhysicalHardwareRev, PhysicalFirmwareRev, PhysicalSoftwareRev, PhysicalSerialNum, PhysicalMfgName, PhysicalModelName, PhysicalAlias, PhysicalAssetID, UnitState. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_physicals: An array of the DevicePhysical objects that match the specified input criteria.
             :rtype device_physicals: Array of DevicePhysical

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def update(self, **kwargs):
        """Updates an existing device physical.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated device physical.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated device physical.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated device physical.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_physical: The updated device physical.
             :rtype device_physical: DevicePhysical

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def update_custom_field(self, **kwargs):
        """Updates an existing device physical.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated device physical.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated device physical.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated device physical.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_physical: The updated device physical.
             :rtype device_physical: DevicePhysical

            """

        return self.api_request(self._get_method_fullname("update_custom_field"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def infradevice(self, **kwargs):
        """The device containing this component.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device containing this component.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def network_id(self, **kwargs):
        """The Network View ID assigned to this component.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The Network View ID assigned to this component.
             :rtype : Integer

            """

        return self.api_request(self._get_method_fullname("network_id"), kwargs)

    def device(self, **kwargs):
        """The device containing this component.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device containing this component.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
