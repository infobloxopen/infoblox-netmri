from ..remote import RemoteModel


class SensorDatumRemote(RemoteModel):
    """
    Sensor data about the health of the NetMRI


    |  ``id:`` The internal NetMRI identifier for the table entry.
    |  ``attribute type:`` number

    |  ``data_source_id:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``name:`` The name of the sensor data.
    |  ``attribute type:`` string

    |  ``name_index:`` The index for all data with a given name.
    |  ``attribute type:`` string

    |  ``label:`` The label for the sensor data.
    |  ``attribute type:`` string

    |  ``category:`` The type of sensor data.
    |  ``attribute type:`` string

    |  ``value:`` The value of the sensor data.
    |  ``attribute type:`` string

    |  ``status:`` The status of the sensor data.
    |  ``attribute type:`` string

    |  ``units:`` The units the value of the sensor data is in.
    |  ``attribute type:`` string

    |  ``details:`` The description of the status of the sensor data.
    |  ``attribute type:`` string

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``first_seen:`` The time when the failure was first detected.
    |  ``attribute type:`` string

    |  ``type:`` The type of a data defined in a sensor.
    |  ``attribute type:`` string

    |  ``description:`` The description defined in a SensorDatum.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "data_source_id",
                  "name",
                  "name_index",
                  "label",
                  "category",
                  "value",
                  "status",
                  "units",
                  "details",
                  "updated_at",
                  "first_seen",
                  "type",
                  "description",
                  )
