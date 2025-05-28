# gcloud iam principal-access-boundary-policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete)*

**NAME**

: **gcloud iam principal-access-boundary-policies delete - delete PrincipalAccessBoundaryPolicy instance**

**SYNOPSIS**

: **`gcloud iam principal-access-boundary-policies delete` (`[PRINCIPAL_ACCESS_BOUNDARY_POLICY](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete#PRINCIPAL_ACCESS_BOUNDARY_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete#--organization)`=`ORGANIZATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete#--async)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete#--etag)`=`ETAG`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete#--force)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete PrincipalAccessBoundaryPolicy instance.

**EXAMPLES**

: To delete `my-policy` instance in organization `123`, run:

```
gcloud iam principal-access-boundary-policies delete my-policy --organization=123 --location=global
```

**POSITIONAL ARGUMENTS**

: **PrincipalAccessBoundaryPolicy resource - The name of the principal access
boundary policy to delete.
Format:
`organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`
The arguments in this group can be used to specify the attributes of this
resource.
This must be specified.

**`PRINCIPAL_ACCESS_BOUNDARY_POLICY`**:
ID of the principalAccessBoundaryPolicy or fully qualified identifier for the
principalAccessBoundaryPolicy.
To set the `principal_access_boundary_policy` attribute:

- provide the argument `principal_access_boundary_policy` on the
command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the principalAccessBoundaryPolicy resource.
To set the `location` attribute:

- provide the argument `principal_access_boundary_policy` on the
command line with a fully specified name;
- provide the argument `--location` on the command line.

**--organization**:
The organization id of the principalAccessBoundaryPolicy resource.
To set the `organization` attribute:

- provide the argument `principal_access_boundary_policy` on the
command line with a fully specified name;
- provide the argument `--organization` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--etag**:
The etag of the principal access boundary policy. If this is provided, it must
match the server's etag.

**--force**:
If set to true, the request will force the deletion of the Policy even if the
Policy references PolicyBindings.

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

: This command uses the `iam/v3` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: This variant is also available:

```
gcloud beta iam principal-access-boundary-policies delete
```