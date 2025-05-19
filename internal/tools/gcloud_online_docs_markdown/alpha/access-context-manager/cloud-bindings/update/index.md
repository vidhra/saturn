# gcloud alpha access-context-manager cloud-bindings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update)*

**NAME**

: **gcloud alpha access-context-manager cloud-bindings update - update an existing access binding under an organization**

**SYNOPSIS**

: **`gcloud alpha access-context-manager cloud-bindings update` (`[--binding](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--binding)`=`BINDING` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--organization)`=`ORGANIZATION`) [`[--append](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--append)`] [`[--binding-file](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--binding-file)`=`YAML_FILE`] [`[--dry-run-level](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--dry-run-level)`=[`DRY_RUN_LEVEL`,…]] [`[--level](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--level)`=[`LEVEL`,…]] [`[--restricted-client-application-client-ids](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--restricted-client-application-client-ids)`=[`RESTRICTED_CLIENT_APPLICATION_CLIENT_IDS`,…]] [`[--restricted-client-application-names](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--restricted-client-application-names)`=[`RESTRICTED_CLIENT_APPLICATION_NAMES`,…]] [`[--session-length](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--session-length)`=`SESSION_LENGTH`] [`[--session-reauth-method](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#--session-reauth-method)`=`SESSION_REAUTH_METHOD`; default="login"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/cloud-bindings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an existing access binding. You can update the
level, dry run level, scoped access settings, session settings, restricted
client application client IDs, and restricted client application names. They
can't all be empty. Session settings are incompatible with restricted client
application client IDs/names; please use scoped access settings to bind session
settings to an application.

**EXAMPLES**

: To update an existing access binding, run:

```
gcloud alpha access-context-manager cloud-bindings update --binding=my-binding-id --level=accessPolicies/123/accessLevels/new-abc
```

To remove level and add dry run level, run:

```
gcloud alpha access-context-manager cloud-bindings update --binding=my-binding-id --level= --dry-run-level=accessPolicies/123/accessLevels/new-def
```

To update restricted client applications, run:

```
gcloud alpha access-context-manager cloud-bindings update --binding=my-binding-id --restricted-client-application-client-ids='123.apps.googleusercontent.com' --restricted-client-application-names='Cloud Console, Google
 Cloud SDK'
```

```
Or
```

```
gcloud alpha access-context-manager cloud-bindings update --binding=my-binding-id --binding-file='binding.yaml'
```

To replace scoped access settings with a new list, run:

```
gcloud alpha access-context-manager cloud-bindings update --binding=my-binding-id --binding-file='binding.yaml'
```

To append scoped access settings to the existing list, run:

```
gcloud alpha access-context-manager cloud-bindings update --binding=my-binding-id --binding-file='binding.yaml' --append
```

Note this is only possible for scoped access settings that exclusively hold
session settings.
To update session settings, run:

```
gcloud alpha access-context-manager cloud-bindings update --binding=my-binding-id --session-length=2h
```

To update the session reauth method you must also specify --session-length (this
can be the existing value if you only want to modify the reauth method), run:

```
gcloud alpha access-context-manager cloud-bindings update --binding=my-binding-id --session-length=2h --session-reauth-method=login
```

To disable session settings, set --session-length=0, for example:

```
gcloud alpha access-context-manager cloud-bindings update --binding=my-binding-id --session-length=0
```

**REQUIRED FLAGS**

: **--binding**

**OPTIONAL FLAGS**

: **--append**:
When true, append the ScopedAccessSettings in `--binding-file` to the
existing ScopedAccessSettings on the binding. When false, the existing binding's
ScopedAccessSettings will be overwritten. Defaults to false. You may only append
ScopedAccessSettings that exclusively hold session settings (i.e no access
levels).

**--binding-file**:
Path to the file that contains a Google Cloud Platform user access binding.
This file contains a YAML-compliant object representing a GcpUserAccessBinding
(as described in the API reference) containing ScopedAccessSettings only. No
other binding fields are allowed.
The file content replaces the corresponding fields in the existing binding.
Unless --append is specified. See --append help text for more details.

**--dry-run-level**:
The dry run access level that replaces the existing dry run level for the given
binding. The input must be the full identifier of an access level, such as
`accessPolicies/123/accessLevels/new-def`.

**--level**:
The access level that replaces the existing level for the given binding. The
input must be the full identifier of an access level, such as
`accessPolicies/123/accessLevels/new-abc`.

**--restricted-client-application-client-ids**:
The application client IDs that replace the existing application client IDs for
the restricted client applications in the given binding.

**--restricted-client-application-names**:
The application names that replace the existing application names for the
restricted client applications in the given binding.

**--session-length**:
The maximum lifetime of a user session provided as an ISO 8601 duration string.
Must be at least one hour or zero, and no more than twenty-four hours.
Granularity is limited to seconds.
When --session-length=0 users in the group attached to this binding will have
infinite session length, effectively disabling the session settings.
A session begins after a user signs in successfully. If a user signs out before
the end of the session lifetime, a new login creates a new session with a fresh
lifetime. When a session expires, the user is asked to reauthenticate in
accordance with session-reauth-method.
Setting --session-reauth-method when --session-length is empty raises an error.
Cannot set --session-length on restricted client applications; please use scoped
access settings.

**--session-reauth-method**:
Specifies the security check a user must undergo when their session expires.
Defaults to --session-reauth-method=LOGIN if unspecified and --session-length is
set. Cannot be used when --session-length is empty or 0.
`SESSION_REAUTH_METHOD` must be one of:

**`login`**:
The user will be prompted to perform regular login. Users who are enrolled in
two-step verification and haven't chosen to "Remember this computer" will be
prompted for their second factor.

**`password`**:
The user will only be required to enter their password.

**`security-key`**:
The user will be prompted to autheticate using their security key. If no
security key has been configured, the LOGIN method is used.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**API REFERENCE**

: This command uses the `accesscontextmanager/v1alpha` API. The full
documentation for this API can be found at: [https://cloud.google.com/access-context-manager/docs/reference/rest/](https://cloud.google.com/access-context-manager/docs/reference/rest/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud access-context-manager cloud-bindings update
```