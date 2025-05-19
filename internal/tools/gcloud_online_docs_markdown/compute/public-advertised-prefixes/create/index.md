# gcloud compute public-advertised-prefixes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create)*

**NAME**

: **gcloud compute public-advertised-prefixes create - creates a Compute Engine public advertised prefix**

**SYNOPSIS**

: **`gcloud compute public-advertised-prefixes create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create#NAME)` `[--dns-verification-ip](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create#--dns-verification-ip)`=`DNS_VERIFICATION_IP` `[--range](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create#--range)`=`RANGE` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create#--description)`=`DESCRIPTION`] [`[--pdp-scope](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create#--pdp-scope)`=`PDP_SCOPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a public advertised prefix:

```
gcloud compute public-advertised-prefixes create my-public-advertised-prefix --range=120.120.10.0/24 --dns-verification-ip=120.120.10.15
```

To create a v2 public advertised prefix:

```
gcloud compute public-advertised-prefixes create my-v2-public-advertised-prefix --range=120.120.10.0/24 --dns-verification-ip=120.120.10.15 --pdp-scope=REGIONAL
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the public advertised prefix to operate on.

**REQUIRED FLAGS**

: **--dns-verification-ip**:
IP address to use for verification. It must be within the IP range specified in
--range.

**--range**:
IP range allocated to this public advertised prefix, in CIDR format.

**OPTIONAL FLAGS**

: **--description**:
Description of this public advertised prefix.

**--pdp-scope**:
Specifies how child public delegated prefix will be scoped.
`PDP_SCOPE` must be one of: `GLOBAL`,
`REGIONAL`.

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
gcloud alpha compute public-advertised-prefixes create
```

```
gcloud beta compute public-advertised-prefixes create
```