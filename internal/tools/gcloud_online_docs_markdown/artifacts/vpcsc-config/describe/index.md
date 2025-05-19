# gcloud artifacts vpcsc-config describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config/describe](https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config/describe)*

**NAME**

: **gcloud artifacts vpcsc-config describe - describe the current Artifact Registry configuration for VPC Service Controls**

**SYNOPSIS**

: **`gcloud artifacts vpcsc-config describe` [`[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config/describe#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/vpcsc-config/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe the current Artifact Registry configuration for VPC Service Controls.
This command can fail for the following reasons:

- Lack of permission - "accesscontextmanager.policies.get".
- The resource could be outside of the VPC SC perimeter.
- Lack of permission - "artifactregistry.vpcscconfigs.get"

**EXAMPLES**

: The following command returns the current VPC Service Controls configuration for
the project my-project and region us-west1:

```
gcloud artifacts vpcsc-config describe --project=my-project --location=us-west1
```

**FLAGS**

: **Location resource - The Artifact Registry VPC SC configs to describe. This
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

: These variants are also available:

```
gcloud alpha artifacts vpcsc-config describe
```

```
gcloud beta artifacts vpcsc-config describe
```