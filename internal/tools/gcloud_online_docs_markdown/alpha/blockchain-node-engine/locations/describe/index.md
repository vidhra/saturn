# gcloud alpha blockchain-node-engine locations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/locations/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/locations/describe)*

**NAME**

: **gcloud alpha blockchain-node-engine locations describe - describe a Blockchain Node Engine location**

**SYNOPSIS**

: **`gcloud alpha blockchain-node-engine locations describe` [`[LOCATION](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/locations/describe#LOCATION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/locations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe a Blockchain Node Engine location.
To get a list of available locations for your project run:

```
gcloud alpha blockchain-node-engine locations list
```

**EXAMPLES**

: The following command describes Blockchain Node Engine location
`us-central1`:

```
gcloud alpha blockchain-node-engine locations describe us-central1
```

**POSITIONAL ARGUMENTS**

: **Location resource - The Blockchain Node Engine location you want to describe.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `location` on the command line with a fully
specified name;
- set the property `web3/location` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`LOCATION`]**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `location` on the command line;
- set the property `web3/location`.**

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

: This command uses the `blockchainnodeengine/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/blockchain-node-engine](https://cloud.google.com/blockchain-node-engine)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.