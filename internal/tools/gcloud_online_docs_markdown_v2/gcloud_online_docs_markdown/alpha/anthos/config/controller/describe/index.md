# gcloud alpha anthos config controller describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/describe)*

**NAME**

: **gcloud alpha anthos config controller describe - describe Anthos Config Controller instances**

**SYNOPSIS**

: **`gcloud alpha anthos config controller describe` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/describe#NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/controller/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe an Anthos Config Controller instance.

**EXAMPLES**

: To describe an Anthos Config Controller instance named default in the location
``us-central1``, run:

```
gcloud alpha anthos config controller describe default --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Instance resource - The identifier for an Anthos Config Controller instance. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `name` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAME`**:
ID of the instance or fully qualified identifier for the instance.
To set the `name` attribute:

- provide the argument `name` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The name of the Anthos Config Controller instance location. Currently, only
`us-central1`, `us-east1`, `us-east4`,
`us-east5`, `us-west2`,
`northamerica-northeast1`, `northamerica-northeast2`,
`europe-north1`, `europe-west1`,
`europe-west3`, `europe-west6`,
`australia-southeast1`, `australia-southeast2`,
`asia-northeast1`, `asia-northeast2` and
`asia-southeast1` are supported.
To set the `location` attribute:

- provide the argument `name` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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

: This command uses the `krmapihosting/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/](https://cloud.google.com/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud anthos config controller describe
```