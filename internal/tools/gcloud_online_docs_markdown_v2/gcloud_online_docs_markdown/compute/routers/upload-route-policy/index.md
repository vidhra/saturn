# gcloud compute routers upload-route-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy](https://cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy)*

**NAME**

: **gcloud compute routers upload-route-policy - upload a route policy into a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers upload-route-policy` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy#NAME)` `[--file-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy#--file-name)`=`FILE_NAME` [`[--file-format](https://cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy#--file-format)`=`FILE_FORMAT`] [`[--policy-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy#--policy-name)`=`POLICY_NAME`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers upload-route-policy` uploads a route policy
into a Compute Engine router.

**EXAMPLES**

: To upload a route policy `my-import-policy` from a file
`my-import-policy.yaml` into a router `my-router` in
region `us-central1`, run:

```
gcloud compute routers upload-route-policy my-router --region=us-central1 --policy-name=my-import-policy --file-name=my-import-policy.yaml"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the router to upload.

**REQUIRED FLAGS**

: **--file-name**:
Local path to the file defining the policy

**OPTIONAL FLAGS**

: **--file-format**:
Format of the file passed to --file-name. `FILE_FORMAT`
must be one of: `json`, `yaml`.

**--policy-name**:
Name of the route policy to add/replace.

**--region**:
Region of the router to upload. If not specified, you might be prompted to
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
gcloud alpha compute routers upload-route-policy
```

```
gcloud beta compute routers upload-route-policy
```