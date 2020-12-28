from ..remote import RemoteModel


class AuthUserRemote(RemoteModel):
    """
    The defined NetMRI users.


    |  ``id:`` The internal NetMRI identifier for this user.
    |  ``attribute type:`` number

    |  ``user_name:`` The user's login name.
    |  ``attribute type:`` string

    |  ``password:`` The user's password (required for local authentication).
    |  ``attribute type:`` string

    |  ``email:`` The user's email address.
    |  ``attribute type:`` string

    |  ``notes:`` Notes on the user, as entered by the administrator.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``first_name:`` The user's first name.
    |  ``attribute type:`` string

    |  ``last_name:`` The user's last name.
    |  ``attribute type:`` string

    |  ``is_system:`` A flag indicating whether this is a built-in user. Built-in users cannot be removed.
    |  ``attribute type:`` number

    |  ``last_login:`` The date and time this use last logged into the NetMRI.
    |  ``attribute type:`` datetime

    |  ``expiration:`` The expiration date for this user's password.
    |  ``attribute type:`` datetime

    |  ``consecutive_failed_logins:`` The number of failed logins since the last successful login.
    |  ``attribute type:`` number

    |  ``account_locked:`` A flag indicating whether or not this account is locked due to failed login attempts.
    |  ``attribute type:`` number

    |  ``account_locked_date:`` The date and time that the user's account was locked.
    |  ``attribute type:`` datetime

    |  ``account_disabled:`` A flag indicating whether this user's account has been administratively disabled.
    |  ``attribute type:`` number

    |  ``account_disabled_date:`` The date and time that the user's account was disabled.
    |  ``attribute type:`` datetime

    |  ``cli_creds_enabled_ind:`` A flag indicating whether or not to use this user's individual CLI credentials for device interaction.
    |  ``attribute type:`` bool

    |  ``password_secure:`` Internal representation of password
    |  ``attribute type:`` string

    |  ``password_version:`` version of encryption used to encrypt password
    |  ``attribute type:`` number

    |  ``cli_user_name_secure:`` The user's network device user name.
    |  ``attribute type:`` string

    |  ``cli_password_secure:`` The user's network device password.
    |  ``attribute type:`` string

    |  ``cli_enable_password_secure:`` The user's network device privileged mode password.
    |  ``attribute type:`` string

    |  ``secure_version:`` The encryption version of the username and passwords.
    |  ``attribute type:`` number

    |  ``auth_service_id:`` The id of the last authentication service where this user was authenticated.
    |  ``attribute type:`` number

    |  ``force_local_ind:`` A flag indicating whether user is forced to use local authorisation or not.
    |  ``attribute type:`` bool

    |  ``last_local_authz_ind:`` The source where the last authorization came from. May be 0 - Remote, 1 - Local, 2 - Forced Local
    |  ``attribute type:`` number

    |  ``cert:`` Client Certificate stored on clinet success authorization when CAC is enabled
    |  ``attribute type:`` string

    |  ``db_username:`` Username for MySQL Database.
    |  ``attribute type:`` string

    |  ``db_password_secure:`` Password for MySQL Database.
    |  ``attribute type:`` string

    |  ``db_creds_enabled_ind:`` A flag which indicates that the user has database credentials enabled.
    |  ``attribute type:`` bool

    """

    properties = ("id",
                  "user_name",
                  "password",
                  "email",
                  "notes",
                  "created_at",
                  "updated_at",
                  "first_name",
                  "last_name",
                  "is_system",
                  "last_login",
                  "expiration",
                  "consecutive_failed_logins",
                  "account_locked",
                  "account_locked_date",
                  "account_disabled",
                  "account_disabled_date",
                  "cli_creds_enabled_ind",
                  "password_secure",
                  "password_version",
                  "cli_user_name_secure",
                  "cli_password_secure",
                  "cli_enable_password_secure",
                  "secure_version",
                  "auth_service_id",
                  "force_local_ind",
                  "last_local_authz_ind",
                  "cert",
                  "db_username",
                  "db_password_secure",
                  "db_creds_enabled_ind",
                  )
