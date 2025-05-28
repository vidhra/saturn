# gcloud kms key-handles create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/create](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/create)*

**NAME**

: **gcloud kms key-handles create - create a new KeyHandle**

**SYNOPSIS**

: **`gcloud kms key-handles create` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/create#--location)`=`LOCATION` `[--resource-type](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/create#--resource-type)`=`RESOURCE_TYPE` (`[--generate-key-handle-id](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/create#--generate-key-handle-id)`     | `[--key-handle-id](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/create#--key-handle-id)`=`KEY_HANDLE_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/key-handles/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new KeyHandle, triggering the provisioning of a new CryptoKey for CMEK
use with the given resource type in the configured key project and the same
location

**EXAMPLES**

: The following command creates a KeyHandle named `my-key-handle`
within the location `global` for the resource type
`compute.googleapis.com/Disk`:

```
gcloud kms key-handles create --key-handle-id=my-key-handle --my-key-handle --location=global --resource-type=compute.googleapis.com/Disk
```

In case we want to generate a random KeyHandle id, we can use the
`--generate-key-handle-id` flag instead of the
`--key-handle-id` flag.

**REQUIRED FLAGS**

: **Location resource - The KMS location resource. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

**--resource-type**:
The resource type selector for KeyHandle resources of the form
{SERVICE}.{UNIVERSE_DOMAIN}/{TYPE}.

**--generate-key-handle-id**

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
gcloud alpha kms key-handles create
```

```
gcloud beta kms key-handles create
```