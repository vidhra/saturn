# gcloud certificate-manager trust-configs import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/import](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/import)*

**NAME**

: **gcloud certificate-manager trust-configs import - import TrustConfig**

**SYNOPSIS**

: **`gcloud certificate-manager trust-configs import` (`[TRUST_CONFIG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/import#TRUST_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/import#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/import#--async)`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/import#--source)`=`SOURCE`] [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/import#--update-mask)`=`UPDATE_MASK`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import a TrustConfig.

**EXAMPLES**

: To import a TrustConfig from a YAML file, run:

```
gcloud certificate-manager trust-configs import my-trust-config --source=my-trust-config.yaml --location=global
```

**POSITIONAL ARGUMENTS**

: **TrustConfig resource - Name of the TrustConfig to import. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `trust_config` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TRUST_CONFIG`**:
ID of the trustConfig or fully qualified identifier for the trustConfig.
To set the `trust_config` attribute:

- provide the argument `trust_config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Certificate Manager location.
To set the `location` attribute:

- provide the argument `trust_config` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- default value of location is [global].**

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

**--update-mask**:
Update mask used to specify fields to be overwritten in the TrustConfig by
import. TrustConfig must already exist. Fields specified in the update-mask are
relative to the TrustConfig. The flag can be a comma-separated list of updatable
non-nested fields, e.g. description or trust_stores. Valid example:
--update-mask=description,trust_stores.

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

: This command uses the `certificatemanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/certificate-manager](https://cloud.google.com/certificate-manager)

**NOTES**

: These variants are also available:

```
gcloud alpha certificate-manager trust-configs import
```

```
gcloud beta certificate-manager trust-configs import
```