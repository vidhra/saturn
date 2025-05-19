# gcloud anthos config controller delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/delete](https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/delete)*

**NAME**

: **gcloud anthos config controller delete - delete Anthos Config Controller instances**

**SYNOPSIS**

: **`gcloud anthos config controller delete` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/delete#NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an Anthos Config Controller instance.

**EXAMPLES**

: To delete an Anthos Config Controller instance, run:

```
gcloud anthos config controller delete NAME --location=LOCATION
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This variant is also available:

```
gcloud alpha anthos config controller delete
```