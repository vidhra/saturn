# gcloud network-security mirroring-deployments describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/describe](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/describe)*

**NAME**

: **gcloud network-security mirroring-deployments describe - describe a Mirroring Deployment**

**SYNOPSIS**

: **`gcloud network-security mirroring-deployments describe` (`[MIRRORING_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/describe#MIRRORING_DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a mirroring deployment.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To get a description of a mirroring deployment called `my-deployment`
in zone `us-central1-a`, run:

```
gcloud network-security mirroring-deployments describe my-deployment --location=us-central1-a --project=my-project
```

OR

```
gcloud network-security mirroring-deployments describe projects/my-project/locations/us-central1-a/mirroringDeployments/my-deployment
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
gcloud alpha network-security mirroring-deployments describe
```

```
gcloud beta network-security mirroring-deployments describe
```