# gcloud access-context-manager cloud-bindings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update)*

**NAME**

: **gcloud access-context-manager cloud-bindings update - update a existing cloud access binding under an organization**

**SYNOPSIS**

: **`gcloud access-context-manager cloud-bindings update` (`[--binding](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update#--binding)`=`BINDING` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update#--organization)`=`ORGANIZATION`) [`[--append](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update#--append)`] [`[--binding-file](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update#--binding-file)`=`YAML_FILE`] [`[--dry-run-level](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update#--dry-run-level)`=[`DRY_RUN_LEVEL`,…]] [`[--level](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update#--level)`=[`LEVEL`,…]] [`[--session-length](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update#--session-length)`=`SESSION_LENGTH`] [`[--session-reauth-method](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update#--session-reauth-method)`=`SESSION_REAUTH_METHOD`; default="login"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/cloud-bindings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing cloud access binding. You can update the level, dry run
level, session settings, and scoped access settings. They cannot all be empty.

**EXAMPLES**

: To update an existing cloud access binding, run:

```
gcloud access-context-manager cloud-bindings update --binding=my-binding-id --level=accessPolicies/123/accessLevels/new-abc
```

To remove level and add dry run level, run:

```
gcloud access-context-manager cloud-bindings update --binding=my-binding-id --level= --dry-run-level=accessPolicies/123/accessLevels/new-def
```

To replace scoped access settings with a new list, run:

```
gcloud access-context-manager cloud-bindings update --binding=my-binding-id --binding-file='binding.yaml'
```

To append scoped access settings to the existing list, run:

```
gcloud access-context-manager cloud-bindings update --binding=my-binding-id --binding-file='binding.yaml' --append
```

Note this is only possible for scoped access settings that exclusively hold
session settings (i.e. no access levels).
To update session settings, run:

```
gcloud access-context-manager cloud-bindings update --binding=my-binding-id --session-length=2h
```

To update the session reauth method you must also specify --session-length (this
can be the existing value if you only want to modify the reauth method), run:

```
gcloud access-context-manager cloud-bindings update --binding=my-binding-id --session-length=2h --session-reauth-method=login
```

To disable session settings, set --session-length=0, for example:

```
gcloud access-context-manager cloud-bindings update --binding=my-binding-id --session-length=0
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

: This command uses the `accesscontextmanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/access-context-manager/docs/reference/rest/](https://cloud.google.com/access-context-manager/docs/reference/rest/)

**NOTES**

: This variant is also available:

```
gcloud alpha access-context-manager cloud-bindings update
```