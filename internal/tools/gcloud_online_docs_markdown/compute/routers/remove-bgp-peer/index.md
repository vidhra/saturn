# gcloud compute routers remove-bgp-peer  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-bgp-peer](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-bgp-peer)*

**NAME**

: **gcloud compute routers remove-bgp-peer - remove a BGP peer from a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers remove-bgp-peer` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-bgp-peer#NAME)` (`[--peer-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-bgp-peer#--peer-name)`=`PEER_NAME`     | `[--peer-names](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-bgp-peer#--peer-names)`=[`PEER_NAME`,…]) [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-bgp-peer#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-bgp-peer#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers remove-bgp-peer` removes a BGP peer from a
Compute Engine router.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the router to update.

**REQUIRED FLAGS**

: **--peer-name**

**OPTIONAL FLAGS**

: **--region**:
Region of the router to update. If not specified, you might be prompted to
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
gcloud alpha compute routers remove-bgp-peer
```

```
gcloud beta compute routers remove-bgp-peer
```