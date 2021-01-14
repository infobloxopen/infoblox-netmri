from ..remote import RemoteModel


class NaVulnerabilitiesNoticesGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VulnerabilityID:`` none
    |  ``attribute type:`` string

    |  ``severity_name:`` none
    |  ``attribute type:`` string

    |  ``severity_sort:`` none
    |  ``attribute type:`` string

    |  ``cve_severity:`` none
    |  ``attribute type:`` string

    |  ``cve_id:`` none
    |  ``attribute type:`` string

    |  ``SeverityID:`` none
    |  ``attribute type:`` string

    |  ``DeviceVulnTimestamp:`` none
    |  ``attribute type:`` string

    |  ``vendor_published:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``Summary:`` none
    |  ``attribute type:`` string

    |  ``announcement_url:`` none
    |  ``attribute type:`` string

    |  ``vendor:`` none
    |  ``attribute type:`` string

    |  ``model:`` none
    |  ``attribute type:`` string

    |  ``os_version:`` none
    |  ``attribute type:`` string

    |  ``total:`` none
    |  ``attribute type:`` string

    |  ``vuln:`` none
    |  ``attribute type:`` string

    |  ``not_vuln:`` none
    |  ``attribute type:`` string

    |  ``manual:`` none
    |  ``attribute type:`` string

    |  ``ignored:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VulnerabilityID",
                  "severity_name",
                  "severity_sort",
                  "cve_severity",
                  "cve_id",
                  "SeverityID",
                  "DeviceVulnTimestamp",
                  "vendor_published",
                  "name",
                  "Summary",
                  "announcement_url",
                  "vendor",
                  "model",
                  "os_version",
                  "total",
                  "vuln",
                  "not_vuln",
                  "manual",
                  "ignored",
                  )
