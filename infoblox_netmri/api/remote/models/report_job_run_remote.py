from ..remote import RemoteModel


class ReportJobRunRemote(RemoteModel):
    """
    Report Job information for reports that have been run on the system in the past 7 days.


    |  ``id:`` The internal NetMRI identifier for the report job.
    |  ``attribute type:`` number

    |  ``report_id:`` The internal NetMRI identifier for a specific report.
    |  ``attribute type:`` number

    |  ``status:`` The report running status.
    |  ``attribute type:`` string

    |  ``start_time:`` The date and time the report job started running.
    |  ``attribute type:`` datetime

    |  ``is_foreground:`` Value to indicate the report is being run in the NetMRI GUI.
    |  ``attribute type:`` number

    |  ``cancel_time:`` The date and time the report job was canceled.
    |  ``attribute type:`` datetime

    |  ``created_at:`` The date and time the report job was created.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the report job was updated.
    |  ``attribute type:`` datetime

    |  ``report_type:`` The report job type to indicate if a report was scheduled or run on demand.
    |  ``attribute type:`` string

    |  ``job_priority:`` The report job priority, lower priority are processed first.
    |  ``attribute type:`` number

    |  ``size:`` The file size of a completed report.
    |  ``attribute type:`` number

    |  ``ext_job_id:`` The system process id for the report job.
    |  ``attribute type:`` number

    |  ``auth_user_id:`` The internal NetMRI user id that created the Report Job.
    |  ``attribute type:`` number

    |  ``last_checkin:`` The date and time the report job last changed status.
    |  ``attribute type:`` datetime

    |  ``report_job_specification_id:`` The internal NetMRI identifier for the associated Report Job Specification.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "report_id",
                  "status",
                  "start_time",
                  "is_foreground",
                  "cancel_time",
                  "created_at",
                  "updated_at",
                  "report_type",
                  "job_priority",
                  "size",
                  "ext_job_id",
                  "auth_user_id",
                  "last_checkin",
                  "report_job_specification_id",
                  )
