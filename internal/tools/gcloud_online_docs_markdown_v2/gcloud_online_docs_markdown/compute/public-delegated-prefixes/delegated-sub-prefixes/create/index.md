# gcloud compute public-delegated-prefixes delegated-sub-prefixes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create)*

**NAME**

: **gcloud compute public-delegated-prefixes delegated-sub-prefixes create - creates a Compute Engine delegated sub prefix**

**SYNOPSIS**

: **`gcloud compute public-delegated-prefixes delegated-sub-prefixes create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#NAME)` `[--public-delegated-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#--public-delegated-prefix)`=`PUBLIC_DELEGATED_PREFIX` [`[--allocatable-prefix-length](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#--allocatable-prefix-length)`=`ALLOCATABLE_PREFIX_LENGTH`] [`[--create-addresses](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#--create-addresses)`] [`[--delegatee-project](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#--delegatee-project)`=`DELEGATEE_PROJECT`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#--description)`=`DESCRIPTION`] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#--mode)`=`MODE`] [`[--range](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#--range)`=`RANGE`] [`[--global-public-delegated-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#--global-public-delegated-prefix)`     | `[--public-delegated-prefix-region](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#--public-delegated-prefix-region)`=`PUBLIC_DELEGATED_PREFIX_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a Compute Engine delegated sub prefix.

**EXAMPLES**

: To create a delegated sub prefix for a global public delegated prefix:

```
gcloud compute public-delegated-prefixes delegated-sub-prefixes create my-sub-prefix --range=120.120.10.128/28 --public-delegated-prefix=my-pdp --global-public-delegated-prefix
```

To create a delegated sub prefix for a regional public delegated prefix:

```
gcloud compute public-delegated-prefixes delegated-sub-prefixes create my-sub-prefix --range=120.120.10.128/30 --create-addresses --public-delegated-prefix=my-pdp --public-delegated-prefix-region=us-east1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the delegated sub prefix to create.

**REQUIRED FLAGS**

: **--public-delegated-prefix**:
Name of the public delegated prefix to create the delegate sub prefix for.

**OPTIONAL FLAGS**

: **--allocatable-prefix-length**:
Specify allocatable prefix length supported by this sub prefix.

**--create-addresses**:
Specify if the sub prefix is delegated to create address resources in the
delegatee project. Default is false.

**--delegatee-project**:
Project to delegate the IPv4 range specified in `--range` to. If
empty, the sub-range is delegated to the same/existing project.

**--description**:
Description of the delegated sub prefix to create.

**--mode**:
Specifies the mode of this IPv6 PDP. `MODE` must be one
of: `delegation`,
`external-ipv6-forwarding-rule-creation`,
`external-ipv6-subnetwork-creation`.

**--range**:
IPv4 range from this public delegated prefix that should be delegated, in CIDR
format. If not specified, the entire range ofthe public advertised prefix is
delegated.

**--global-public-delegated-prefix**

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
gcloud alpha compute public-delegated-prefixes delegated-sub-prefixes create
```

```
gcloud beta compute public-delegated-prefixes delegated-sub-prefixes create
```