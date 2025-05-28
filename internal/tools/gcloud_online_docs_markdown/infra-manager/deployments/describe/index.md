# gcloud infra-manager deployments describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/describe](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/describe)*

**NAME**

: **gcloud infra-manager deployments describe - describe deployments**

**SYNOPSIS**

: **`gcloud infra-manager deployments describe` (`[DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/describe#DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a deployment

**EXAMPLES**

: To describe a deployment `example-deployment` in project
`p1` at location `us-central1`, run:

```
gcloud infra-manager deployments describe projects/p1/locations/us-central1/deployments/example-deployment
```

**POSITIONAL ARGUMENTS**

: **Deployment resource - The deployment to describe The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `deployment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DEPLOYMENT`**:
ID of the deployment or fully qualified identifier for the deployment.
To set the `deployment` attribute:

- provide the argument `deployment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
locations TBD
To set the `location` attribute:

- provide the argument `deployment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.**

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

: This command uses the `config/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/infrastructure-manager/docs](https://cloud.google.com/infrastructure-manager/docs)