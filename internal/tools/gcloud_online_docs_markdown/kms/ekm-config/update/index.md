# gcloud kms ekm-config update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/update](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/update)*

**NAME**

: **gcloud kms ekm-config update - update the EkmConfig**

**SYNOPSIS**

: **`gcloud kms ekm-config update` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/update#--location)`=`LOCATION` [`[--default-ekm-connection](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/update#--default-ekm-connection)`=`DEFAULT_EKM_CONNECTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud kms ekm-config update can be used to update the EkmConfig. Applies to all
CryptoKeys and CryptoKeyVersions with a `protection level` of
`external vpc`.

**EXAMPLES**

: The following command sets the default ekm-connection to `laplace`
for its project `foo` and location `us-east1`:

```
gcloud kms ekm-config update --location=us-east1 --default-ekm-connection="projects/foo/locations/us-east1/ekmConnections/laplace"
```

The following command removes the default-ekm-connection in
`us-east1` for the current project:

```
gcloud kms ekm-config update --location=us-east1 --default-ekm-connection=""
```

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

**OPTIONAL FLAGS**

: **--default-ekm-connection**:
The resource name of the EkmConnection to be used as the default EkmConnection
for all `external-vpc` CryptoKeys in a project and location. Can be
an empty string to remove the default EkmConnection.

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
gcloud alpha kms ekm-config update
```

```
gcloud beta kms ekm-config update
```