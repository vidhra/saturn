# gcloud compute public-delegated-prefixes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create)*

**NAME**

: **gcloud compute public-delegated-prefixes create - creates a Compute Engine public delegated prefix**

**SYNOPSIS**

: **`gcloud compute public-delegated-prefixes create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#NAME)` `[--range](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#--range)`=`RANGE` (`[--public-advertised-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#--public-advertised-prefix)`=`PUBLIC_ADVERTISED_PREFIX`     | `[--public-delegated-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#--public-delegated-prefix)`=`PUBLIC_DELEGATED_PREFIX`) [`[--allocatable-prefix-length](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#--allocatable-prefix-length)`=`ALLOCATABLE_PREFIX_LENGTH`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#--description)`=`DESCRIPTION`] [`[--enable-live-migration](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#--enable-live-migration)`] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#--mode)`=`MODE`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a public delegated prefix:

```
gcloud compute public-delegated-prefixes create my-public-delegated-prefix --public-advertised-prefix=my-pap --range=120.120.10.128/27 --global
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the public delegated prefix to operate on.

**REQUIRED FLAGS**

: **--range**:
IP range from this public delegated prefix that should be delegated, in CIDR
format. It must be smaller than parent public advertised prefix range.

**--public-advertised-prefix**

**OPTIONAL FLAGS**

: **--allocatable-prefix-length**:
The allocatable prefix length supported by this PDP.

**--description**:
Description of this public delegated prefix.

**--enable-live-migration**:
Specify if this public delegated prefix is meant to be live migrated.

**--mode**:
Specifies the mode of this IPv6 PDP. `MODE` must be one
of: `delegation`,
`external-ipv6-forwarding-rule-creation`,
`external-ipv6-subnetwork-creation`.

**--global**

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
gcloud alpha compute public-delegated-prefixes create
```

```
gcloud beta compute public-delegated-prefixes create
```