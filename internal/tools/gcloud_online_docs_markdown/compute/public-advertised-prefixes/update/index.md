# gcloud compute public-advertised-prefixes update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update)*

**NAME**

: **gcloud compute public-advertised-prefixes update - updates a Compute Engine public advertised prefix**

**SYNOPSIS**

: **`gcloud compute public-advertised-prefixes update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update#NAME)` (`[--announce-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update#--announce-prefix)`     | `[--status](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update#--status)`=`STATUS`     | `[--withdraw-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update#--withdraw-prefix)`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update a public advertised prefix:

```
gcloud compute public-advertised-prefixes update my-pap --status=ptr-configured
```

To announce a public advertised prefix:

```
gcloud compute public-advertised-prefixes update my-pap --announce-prefix
```

To withdraw a public advertised prefix:

```
gcloud compute public-advertised-prefixes update my-pap --withdraw-prefix
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the public advertised prefix to operate on.

**REQUIRED FLAGS**

: **--announce-prefix**

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
gcloud alpha compute public-advertised-prefixes update
```

```
gcloud beta compute public-advertised-prefixes update
```