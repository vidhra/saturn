# gcloud compute routers download-route-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/download-route-policy](https://cloud.google.com/sdk/gcloud/reference/compute/routers/download-route-policy)*

**NAME**

: **gcloud compute routers download-route-policy - download a route policy from a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers download-route-policy` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/download-route-policy#NAME)` `[--file-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/download-route-policy#--file-name)`=`FILE_NAME` `[--policy-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/download-route-policy#--policy-name)`=`POLICY_NAME` [`[--file-format](https://cloud.google.com/sdk/gcloud/reference/compute/routers/download-route-policy#--file-format)`=`FILE_FORMAT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/download-route-policy#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/download-route-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers download-route-policy` downloads a route
policy from a Compute Engine router.

**EXAMPLES**

: To download a route policy `my-export-policy` to a file
`my-export-policy.yaml` from a router `my-router` in
region `us-central1`, run:

```
gcloud compute routers download-route-policy my-router --region=us-central1 --policy-name=my-export-policy --file-name=my-export-policy.yaml"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the router to export.

**REQUIRED FLAGS**

: **--file-name**:
The name of the file to download the route policy config to.

**--policy-name**:
Name of the route policy to download.

**OPTIONAL FLAGS**

: **--file-format**:
Format of the file passed to --file-name. `FILE_FORMAT`
must be one of: `json`, `yaml`.

**--region**:
Region of the router to export. If not specified, you might be prompted to
select a region (interactive mode only).
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

**NOTES**

: These variants are also available:

```
gcloud alpha compute routers download-route-policy
```

```
gcloud beta compute routers download-route-policy
```