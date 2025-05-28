# gcloud compute instances get-guest-attributes  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-guest-attributes](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-guest-attributes)*

**NAME**

: **gcloud compute instances get-guest-attributes - get the Guest Attributes for a compute instance**

**SYNOPSIS**

: **`gcloud compute instances get-guest-attributes` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-guest-attributes#INSTANCE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-guest-attributes#--zone)`=`ZONE`) [`[--query-path](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-guest-attributes#--query-path)`=`QUERY_PATH`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/get-guest-attributes#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the Guest Attributes for a compute instance.

**EXAMPLES**

: To get the guest attributes for instance 'my-instance' in zone 'ZONE' with query
path 'query/path', run:

```
gcloud compute instances get-guest-attributes my-instance --query-path=query/path --zone=ZONE
```

**POSITIONAL ARGUMENTS**

: **Instance resource - The instance to get the Guest Attributes for. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The name of the Google Compute Engine zone.
To set the `zone` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

**FLAGS**

: **--query-path**:
Attribute path to query. Can be empty string or of the form
`<namespace>/` or `<namespace>/<key>`.
Default is the empty string.

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

: This command uses the `compute/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: These variants are also available:

```
gcloud alpha compute instances get-guest-attributes
```

```
gcloud beta compute instances get-guest-attributes
```