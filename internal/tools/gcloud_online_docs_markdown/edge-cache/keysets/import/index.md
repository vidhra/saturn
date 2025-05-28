# gcloud edge-cache keysets import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import)*

**NAME**

: **gcloud edge-cache keysets import - import an EdgeCacheKeyset resource**

**SYNOPSIS**

: **`gcloud edge-cache keysets import` (`[KEYSET](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import#KEYSET)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import#--async)`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import#--source)`=`SOURCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import an EdgeCacheKeyset resource. If the named EdgeCacheKeyset resource
already exists, the resource will be updated to match the imported resource
configuration.
Note: If you are updating an existing EdgeCacheKeyset resource, you should
ensure that it includes any public keys still needed to validate incoming user
requests.
If the named EdgeCacheKeyset resource does not already exist, a new
EdgeCacheKeyset resource will be created with that name.

**EXAMPLES**

: To import an EdgeCacheKeyset resource named 'my-keyset' from a YAML file, run:

```
gcloud edge-cache keysets import my-keyset --source=my-keyset.yaml
```

**POSITIONAL ARGUMENTS**

: **Keyset resource - The EdgeCacheKeyset resource you want to import. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `keyset` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`KEYSET`**:
ID of the keyset or fully qualified identifier for the keyset.
To set the `keyset` attribute:

- provide the argument `keyset` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `keyset` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- use global location.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--source**:
Path to a YAML file containing the configuration export data. The YAML file must
not contain any output-only fields. Alternatively, you may omit this flag to
read from standard input. For a schema describing the export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/…
$CLOUDSDKROOT is can be obtained with the following command:

```
gcloud info --format='value(installation.sdk_root)'
```

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

: This command uses the `networkservices/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cache keysets import
```