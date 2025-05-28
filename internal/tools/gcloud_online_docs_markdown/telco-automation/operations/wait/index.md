# gcloud telco-automation operations wait  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/telco-automation/operations/wait](https://cloud.google.com/sdk/gcloud/reference/telco-automation/operations/wait)*

**NAME**

: **gcloud telco-automation operations wait - poll long-running telco automation operation until it completes**

**SYNOPSIS**

: **`gcloud telco-automation operations wait` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/telco-automation/operations/wait#OPERATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/telco-automation/operations/wait#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/telco-automation/operations/wait#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Poll a long-running telco automation operation until it completes. When the
operation is complete, this command will display the results of the analysis.

**EXAMPLES**

: To poll a long-running telco automation operation named
`test-operation` in region `us-central1` until it
completes, run the following:

```
gcloud telco-automation operations wait test-operation --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Operation resource - ID for the operation to poll until complete. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OPERATION`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
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

**API REFERENCE**

: This command uses the `telcoautomation/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/blog/topics/telecommunications/network-automation-csps-linus-nephio-cloud-native](https://cloud.google.com/blog/topics/telecommunications/network-automation-csps-linus-nephio-cloud-native)

**NOTES**

: This variant is also available:

```
gcloud alpha telco-automation operations wait
```