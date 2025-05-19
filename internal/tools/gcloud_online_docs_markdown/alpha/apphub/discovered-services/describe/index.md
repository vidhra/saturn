# gcloud alpha apphub discovered-services describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/discovered-services/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/discovered-services/describe)*

**NAME**

: **gcloud alpha apphub discovered-services describe - describe an Apphub discovered service**

**SYNOPSIS**

: **`gcloud alpha apphub discovered-services describe` (`[DISCOVERED_SERVICE](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/discovered-services/describe#DISCOVERED_SERVICE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/discovered-services/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/discovered-services/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe an Apphub discovered service.

**EXAMPLES**

: To describe the DiscoveredService `my-discovered-service` in location
`us-east1`, run:

```
gcloud alpha apphub discovered-services describe my-discovered-service --location=us-east1
```

**POSITIONAL ARGUMENTS**

: **DiscoveredService resource - The Discovered Service ID. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `discovered_service` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DISCOVERED_SERVICE`**:
ID of the discoveredService or fully qualified identifier for the
discoveredService.
To set the `discovered_service` attribute:

- provide the argument `discovered_service` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the discoveredService.
To set the `location` attribute:

- provide the argument `discovered_service` on the command line with a
fully specified name;
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

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud apphub discovered-services describe
```