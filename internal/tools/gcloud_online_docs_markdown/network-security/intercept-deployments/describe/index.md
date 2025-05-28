# gcloud network-security intercept-deployments describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/describe](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/describe)*

**NAME**

: **gcloud network-security intercept-deployments describe - describe an Intercept Deployment**

**SYNOPSIS**

: **`gcloud network-security intercept-deployments describe` (`[INTERCEPT_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/describe#INTERCEPT_DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an intercept deployment.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To get a description of an intercept deployment called
`my-deployment` in zone `us-central1-a`, run:

```
gcloud network-security intercept-deployments describe my-deployment --location=us-central1-a --project=my-project
```

OR

```
gcloud network-security intercept-deployments describe projects/my-project/locations/us-central1-a/interceptDeployments/my-deployment
```

**POSITIONAL ARGUMENTS**

: **Intercept deployment resource - Intercept Deployment. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERCEPT_DEPLOYMENT`**:
ID of the intercept deployment or fully qualified identifier for the intercept
deployment.
To set the `deployment-id` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the intercept deployment.
To set the `location` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT` on the command line with
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
gcloud alpha network-security intercept-deployments describe
```

```
gcloud beta network-security intercept-deployments describe
```