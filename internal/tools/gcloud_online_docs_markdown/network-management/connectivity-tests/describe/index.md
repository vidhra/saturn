# gcloud network-management connectivity-tests describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/describe](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/describe)*

**NAME**

: **gcloud network-management connectivity-tests describe - describe a connectivity test**

**SYNOPSIS**

: **`gcloud network-management connectivity-tests describe` `[CONNECTIVITY_TEST](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/describe#CONNECTIVITY_TEST)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details of a connectivity test.

**EXAMPLES**

: The following command prints of a connectivity test with the name
`my-test`.

```
gcloud network-management connectivity-tests describe my-test
```

**POSITIONAL ARGUMENTS**

: **Connectivity test resource - Name of the connectivity test you want to describe.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `connectivity_test` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONNECTIVITY_TEST`**:
ID of the connectivity test or fully qualified identifier for the connectivity
test.
To set the `connectivity_test` attribute:

- provide the argument `connectivity_test` on the command line.**

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

: This command uses the `networkmanagement/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/](https://cloud.google.com/)

**NOTES**

: This variant is also available:

```
gcloud beta network-management connectivity-tests describe
```