from ..remote import RemoteModel


class ScorecardHistoryRemote(RemoteModel):
    """
    This table list out the entries of Scorecard history.


    |  ``Component:`` The issue component (Devices, Configuration, VLANs, etc.).
    |  ``attribute type:`` string

    |  ``Timestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``Correctness:`` The correctness contribution for this issue in the scorecard history.
    |  ``attribute type:`` string

    |  ``Stability:`` The stability contribution for this issue in the scorecard history.
    |  ``attribute type:`` string

    |  ``Info:`` The information details of the scorecard history.
    |  ``attribute type:`` string

    |  ``Warn:`` The warning details of the scorecard history.
    |  ``attribute type:`` string

    |  ``Error:`` The error of the scorecard history.
    |  ``attribute type:`` string

    |  ``InfoDetails:`` The information details of the scorecard history.
    |  ``attribute type:`` string

    |  ``WarnDetails:`` The warning details of the scorecard history.
    |  ``attribute type:`` string

    |  ``ErrorDetails:`` The error details of the scorecard history.
    |  ``attribute type:`` string

    """

    properties = ("Component",
                  "Timestamp",
                  "Correctness",
                  "Stability",
                  "Info",
                  "Warn",
                  "Error",
                  "InfoDetails",
                  "WarnDetails",
                  "ErrorDetails",
                  )
