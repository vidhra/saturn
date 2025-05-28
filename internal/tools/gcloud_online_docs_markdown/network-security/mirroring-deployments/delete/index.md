# gcloud network-security mirroring-deployments delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/delete](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/delete)*

**NAME**

: **gcloud network-security mirroring-deployments delete - delete a Mirroring Deployment**

**SYNOPSIS**

: **`gcloud network-security mirroring-deployments delete` (`[MIRRORING_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/delete#MIRRORING_DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/delete#--async)`] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/delete#--max-wait)`=`MAX_WAIT`; default="20m"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a mirroring deployment. Check the progress of deployment deletion by
using `[gcloud
network-security mirroring-deployments list](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/list)`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To delete a mirroring deployment called `my-deployment` in location
`us-central1`, run:

```
gcloud network-security mirroring-deployments delete my-deployment --location=us-central1-a --project=my-project
```

**POSITIONAL ARGUMENTS**

: **Mirroring deployment resource - Mirroring Deployment. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `MIRRORING_DEPLOYMENT` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MIRRORING_DEPLOYMENT`**:
ID of the mirroring deployment or fully qualified identifier for the mirroring
deployment.
To set the `deployment-id` attribute:

- provide the argument `MIRRORING_DEPLOYMENT` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the mirroring deployment.
To set the `location` attribute:

- provide the argument `MIRRORING_DEPLOYMENT` on the command line with
a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--max-wait**:
Time to synchronously wait for the operation to complete, after which the
operation continues asynchronously. Ignored if --no-async isn't specified. See $
[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

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

**NOTES**

: These variants are also available:

```
gcloud alpha network-security mirroring-deployments delete
```

```
gcloud beta network-security mirroring-deployments delete
```