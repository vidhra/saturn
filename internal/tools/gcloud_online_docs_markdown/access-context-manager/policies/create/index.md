# gcloud access-context-manager policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create)*

**NAME**

: **gcloud access-context-manager policies create - create a new access policy**

**SYNOPSIS**

: **`gcloud access-context-manager policies create` `[--organization](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create#--organization)`=`ORGANIZATION` `[--title](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create#--title)`=`TITLE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create#--async)`] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create#--scopes)`=[`SCOPES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Access Context Manager policy. An Access Context Manager policy,
also known as an access policy, is a container for access levels and VPC Service
Controls service perimeters.
You can optionally specify either a folder or a project as a scope of an access
policy. A scoped policy only allows projects under that scope to be restricted
by any service perimeters defined with that policy. The scope must be within the
organization that this policy is associated with. You can specify only one
folder or project as the scope for an access policy. If you don't specify a
scope, then the scope extends to the entire organization and any projects within
the organization can be added to service perimeters in this policy.
This command only creates an access policy. Access levels and service perimeters
need to be created explicitly.

**EXAMPLES**

: To create an access policy that applies to the entire organization, run:

```
gcloud access-context-manager policies create --organization=organizations/123 --title="My Policy"
```

To create an access policy that applies to the folder with the ID 345, run:

```
gcloud access-context-manager policies create --organization=organizations/123 --scopes=folders/345 --title="My Folder Policy"
```

Only projects within this folder can be added to service perimeters within this
policy.
To create an access policy that applies only to the project with the project
number 567, run:

```
gcloud access-context-manager policies create --organization=organizations/123 --scopes=projects/567 --title="My Project Policy"
```

**REQUIRED FLAGS**

: **--organization**:
Parent organization for the access policies.

**--title**:
Short human-readable title of the access policy.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--scopes**:
Folder or project on which this policy is applicable. You can specify only one
folder or project as the scope and the scope must exist within the specified
organization. If you don't specify a scope, the policy applies to the entire
organization.

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

: These variants are also available:

```
gcloud alpha access-context-manager policies create
```

```
gcloud beta access-context-manager policies create
```