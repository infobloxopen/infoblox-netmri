from ..remote import RemoteModel


class JobTargetRemote(RemoteModel):
    """
    Definition of targets of execution for a Job Specification or a Job.


    |  ``job_id:`` The internal identifier of the job this target belongs to.
    |  ``attribute type:`` number

    |  ``managed_process_id:`` The internal identifier of JobProcess that runs this target.
    |  ``attribute type:`` number

    |  ``dis_session_id:`` Unused.
    |  ``attribute type:`` string

    |  ``target_type:`` Type of Target.
    |  ``attribute type:`` string

    |  ``device_id:`` The internal identifier of device if that target denotes a Device.
    |  ``attribute type:`` number

    |  ``device_group_id:`` The internal identifier of device-group if that target is of type TargetdeviceGroup.
    |  ``attribute type:`` number

    |  ``interface_group_id:`` The internal identifier of interface-group if that target is of type TargetInterfaceGroup.
    |  ``attribute type:`` number

    |  ``interface_id:`` The internal identifier of interface if that target is of type TargetInterface.
    |  ``attribute type:`` number

    |  ``device_filter_set_id:`` The internal identifier of DevicFilterSet that target is of type TargetDeviceFilterSet.
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``job_specification_id:`` The internal identifier of the job specification that issued this target.
    |  ``attribute type:`` number

    |  ``status:`` The last known execution status for this target.
    |  ``attribute type:`` string

    |  ``last_status_at:`` The date and time the status was updated.
    |  ``attribute type:`` datetime

    |  ``completed_at:`` The date and time this target was completed in the script execution.
    |  ``attribute type:`` datetime

    |  ``status_info:`` Extra information on the execution status for this target.
    |  ``attribute type:`` string

    |  ``id:`` The internal identifier of this target.
    |  ``attribute type:`` number

    |  ``input_data:`` Target specific input data.
    |  ``attribute type:`` string

    """

    properties = ("job_id",
                  "managed_process_id",
                  "dis_session_id",
                  "target_type",
                  "device_id",
                  "device_group_id",
                  "interface_group_id",
                  "interface_id",
                  "device_filter_set_id",
                  "created_at",
                  "updated_at",
                  "job_specification_id",
                  "status",
                  "last_status_at",
                  "completed_at",
                  "status_info",
                  "id",
                  "input_data",
                  )
