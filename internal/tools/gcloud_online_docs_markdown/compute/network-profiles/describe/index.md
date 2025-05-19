# gcloud compute network-profiles describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-profiles/describe](https://cloud.google.com/sdk/gcloud/reference/compute/network-profiles/describe)*

**NAME**

: **gcloud compute network-profiles describe - describe a network profile**

**SYNOPSIS**

: **`gcloud compute network-profiles describe` `[NETWORK_PROFILE](https://cloud.google.com/sdk/gcloud/reference/compute/network-profiles/describe#NETWORK_PROFILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-profiles/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a network profile.

**EXAMPLES**

: To retrieve a single network profile and print its properties, run the following
command:
```
gcloud compute network-profiles describe my-network-profile
```

**POSITIONAL ARGUMENTS**

: **Network profile resource - Name of the network profile you want to inspect. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `network_profile` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NETWORK_PROFILE`**:
ID of the network_profile or fully qualified identifier for the network_profile.
To set the `network_profile` attribute:

- provide the argument `network_profile` on the command line.**

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
gcloud alpha compute network-profiles describe
```

```
gcloud beta compute network-profiles describe
```