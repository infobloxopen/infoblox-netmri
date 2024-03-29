from ..broker import Broker


class DeviceSupportBundleBroker(Broker):
    controller = "device_support_bundles"

    def index(self, **kwargs):
        """Lists the available device support bundles. Any of the inputs listed may be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Device Support Bundle.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Device Support Bundle.
             :type id: Array of Integer

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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Valid values are id, name, version, author, enabled_ind, system_ind, neighbor_ind, inventory_ind, environmental_ind, cpu_ind, memory_ind, vlan_ind, forwarding_ind, port_ind, config_ind, created_by, updated_by, created_at, updated_at, valid_ind, unit_tests, status, integrated_ind.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each DeviceSupportBundle. Valid values are id, name, version, author, enabled_ind, system_ind, neighbor_ind, inventory_ind, environmental_ind, cpu_ind, memory_ind, vlan_ind, forwarding_ind, port_ind, config_ind, created_by, updated_by, created_at, updated_at, valid_ind, unit_tests, status, integrated_ind. If empty or omitted, all attributes will be returned.
             :type select: Array

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_support_bundles: An array of the DeviceSupportBundle objects that match the specified input criteria.
             :rtype device_support_bundles: Array of DeviceSupportBundle

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified device support bundle from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Device Support Bundle.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def delete(self, **kwargs):
        """Delete a device support bundle specified by name

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: Unique device support bundle name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read from the delete output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete"), kwargs)

    def export(self, **kwargs):
        """Export specified device support bundle in tgz format.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: Unique Device Support Bundle name indicating the bundle to export
             :type dsb_name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("export"), kwargs)

    def import_data(self, **kwargs):
        """Import Device Support Bundles in bulk via a xml, tgz, tar, or zip file

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param file: Device Support Bundle file contents to be imported
             :type file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read from the import output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import"), kwargs)

    def discard(self, **kwargs):
        """Discard all changes to the modified Device Support Bundle

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: Name of the DSB for which changes should be discarded
             :type dsb_name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("discard"), kwargs)

    def generate_templates(self, **kwargs):
        """Return DSB file templates

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: The unique name of the new DSB (it will be inserted into template files where necessary)
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param type: The type of the DSB template
             :type type: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("generate_templates"), kwargs)

    def show(self, **kwargs):
        """Return all existing files for a DSB

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: DSB name
             :type dsb_name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def validate(self, **kwargs):
        """Validate DSB files

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: DSB name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: DSB config description content
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ccs_scripts: DSB Perl scripts content
             :type ccs_scripts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param perl_scripts: DSB CCS scripts content
             :type perl_scripts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes already read from the output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("validate"), kwargs)

    def save(self, **kwargs):
        """Save DSB scripts to working directory

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: DSB name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param description: DSB config description content
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ccs_scripts: DSB Perl scripts content
             :type ccs_scripts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param perl_scripts: DSB CCS scripts content
             :type perl_scripts: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("save"), kwargs)

    def install(self, **kwargs):
        """Install a saved, validated DSB script

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: DSB name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes already read from the output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("install"), kwargs)

    def test_bundle(self, **kwargs):
        """Test DSB in real-time

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: Unique device support bundle name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ip: Device IP to test the DSB against
             :type device_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes already read from the test output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("test_bundle"), kwargs)

    def validate_bundle(self, **kwargs):
        """Validate DSB

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: Unique device support bundle name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes already read from the validation output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("validate_bundle"), kwargs)
