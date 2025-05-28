# gcloud firebase test network-profiles describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles/describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles/describe)*

**NAME**

: **gcloud firebase test network-profiles describe - describe a network profile**

**SYNOPSIS**

: **`gcloud firebase test network-profiles describe` `[PROFILE_ID](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles/describe#PROFILE_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a network profile.
Run `$ [gcloud firebase test
network-profiles](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles) --help` for descriptions of the network profile
parameters.

**EXAMPLES**

: To describe a network profile, run:

```
gcloud firebase test network-profiles describe GSM
```

To describe a network profiles in JSON format, run:

```
gcloud firebase test network-profiles describe GSM --format=json
```

**POSITIONAL ARGUMENTS**

: **`PROFILE_ID`**:
The network profile to describe, found using $ [gcloud firebase
test network-profiles list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles/list).

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
gcloud alpha firebase test network-profiles describe
```

```
gcloud beta firebase test network-profiles describe
```