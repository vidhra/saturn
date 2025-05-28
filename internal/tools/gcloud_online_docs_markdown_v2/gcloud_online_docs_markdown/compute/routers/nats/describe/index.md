# gcloud compute routers nats describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe)*

**NAME**

: **gcloud compute routers nats describe - describe a NAT in a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers nats describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe#NAME)` `[--router](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe#--router)`=`ROUTER` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers nats describe` is used to describe a NAT in a
Compute Engine router.

**EXAMPLES**

: To describe NAT 'n1' in router 'r1', run:

```
gcloud compute routers nats describe n1 --router=r1 --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the NAT to describe

**REQUIRED FLAGS**

: **--router**:
The Router to use for NAT.

**OPTIONAL FLAGS**

: **--region**:
Region of the NAT to describe. If not specified, you might be prompted to select
a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

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

: This command, when specified without alpha or beta, uses the compute/v1/routers
API. The full documentation for this API can be found at: [https://cloud.google.com/compute/docs/reference/rest/v1/routers/](https://cloud.google.com/compute/docs/reference/rest/v1/routers/)
The beta command uses the compute/beta/routers API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/docs/reference/rest/beta/routers/](https://cloud.google.com/compute/docs/reference/rest/beta/routers/)
The alpha command uses the compute/alpha/routers API. Full documentation is not
available for the alpha API.

**NOTES**

: These variants are also available:

```
gcloud alpha compute routers nats describe
```

```
gcloud beta compute routers nats describe
```