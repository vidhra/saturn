# gcloud alpha artifacts vpcsc-config deny  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/vpcsc-config/deny](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/vpcsc-config/deny)*

**NAME**

: **gcloud alpha artifacts vpcsc-config deny - deny access to upstream sources outside the service perimeter for Artifact Registry remote repositories inside the perimeter**

**SYNOPSIS**

: **`gcloud alpha artifacts vpcsc-config deny` [`[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/vpcsc-config/deny#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/vpcsc-config/deny#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Deny access to upstream sources outside the service
perimeter for Artifact Registry remote repositories inside the perimeter.
This command can fail for the following reasons:

- Lack of permission - "accesscontextmanager.policies.update".
- The resource could be outside of the VPC SC perimeter.
- Lack of permission - "artifactregistry.vpcscconfigs.update"

**EXAMPLES**

: The following command denies access to upstream sources outside the service
perimeter for remote repositories in the project my-project and in the region
us--west1:

```
gcloud alpha artifacts vpcsc-config deny --project=my-project --location=us-west1
```

**FLAGS**

: **Location resource - The Artifact Registry VPC SC config to update. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `artifacts/location` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- set the property `artifacts/location`.**

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

: This command uses the `artifactregistry/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/artifacts/docs/](https://cloud.google.com/artifacts/docs/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts vpcsc-config deny
```

```
gcloud beta artifacts vpcsc-config deny
```