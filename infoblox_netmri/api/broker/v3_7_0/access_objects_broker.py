from ..broker import Broker


class AccessObjectsBroker(Broker):
    controller = "access_objects"

    def children(self, **kwargs):
        """Returns tree-format information about this children of a node, in a tree view.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` DeviceObject

             :param tree_type: types of objects in the tree, one of ["DeviceObject", "DeviceService"]
             :type tree_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` normal

             :param search_mode: kind of search within the object of the database
             :type search_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param search_key: Search identifier for contextual search process. Used only for contextual search.
             :type search_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param search: String to search in the objects names or direct values
             :type search: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` none

             :param group_mode: organization of tree-view result
             :type group_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param parent_node_id: identifier of an existing node of the tree, for which we want the children nodes, if omitted, parent is the absolute root node of the tree
             :type parent_node_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: Position of the first node of the returned array, in the brotherhood
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 50

             :param limit: Maximum number of nodes expected to return
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tree

             :param formatting: output format. only one value 'tree'
             :type formatting: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return children: list of node. Each one is a hash [id, node_type, label, tooltip, icon, has_details, leaf, children] representing a child's node
             :rtype children: Array

            """

        return self.api_request(self._get_method_fullname("children"), kwargs)

    def cancel_search(self, **kwargs):
        """Cancels background search processes. Currently only works for contextual search.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param search_key: Search identifier for contextual search process. Used only for contextual search.
             :type search_key: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("cancel_search"), kwargs)

    def parents(self, **kwargs):
        """Returns the parents of this node.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param object_id: The tree node id for which we want the parents
             :type object_id: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return parents: list of parents.
             :rtype parents: Array

            """

        return self.api_request(self._get_method_fullname("parents"), kwargs)

    def to_detail(self, **kwargs):
        """Returns the detail for an object.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param object_id: None
             :type object_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param view: 0=tostring, 1=tooltip, 2-popup
             :type view: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return detail: None
             :rtype detail: String

            """

        return self.api_request(self._get_method_fullname("to_detail"), kwargs)

    def object_picker(self, **kwargs):
        """Returns a tree-format of the full sub-tree for this node. Expected to be displayed as a separate tree in a tree-popup window

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` DeviceObject

             :param main_type: types of objects searched, one of ["DeviceObject", "DeviceService"]
             :type main_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param query: query string for matching fields
             :type query: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("object_picker"), kwargs)
