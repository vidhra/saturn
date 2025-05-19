# gcloud beta active-directory domains extend-schema  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/extend-schema](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/extend-schema)*

**NAME**

: **gcloud beta active-directory domains extend-schema - initiate schema extension for a Managed Microsoft AD domain**

**SYNOPSIS**

: **`gcloud beta active-directory domains extend-schema` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/extend-schema#DOMAIN)` `[--description](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/extend-schema#--description)`=`DESCRIPTION` `[--ldif-file](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/extend-schema#--ldif-file)`=`PATH_TO_FILE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/extend-schema#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/extend-schema#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Initiate schema extension for a Managed Microsoft AD domain.
This command can fail for the following reasons:

- The specified domain doesn't exist.
- The specified domain is either being created or updated.
- The specified domain is under maintenance.
- The active account doesn't have permission to initiate schema extension on the
specified domain.

**EXAMPLES**

: The following command initiates a schema extension for the domain
`my-domain.com` in project `my-project`, with description
`Test Description`, using the LDIF file `demo.ldif`

```
gcloud beta active-directory domains extend-schema my-domain.com --description="Test Description" --ldif-file=demo.ldf --project=my-project --async
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the Managed Microsoft AD domain for which you want to
extend schema. This represents a Cloud resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `domain` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DOMAIN`**:
ID of the domain or fully qualified identifier for the domain.
To set the `domain` attribute:

- provide the argument `domain` on the command line.**

**REQUIRED FLAGS**

: **--description**:
Description of schema change.

**--ldif-file**:
Local LDIF file path that contains commands for schema extension. The file size
can't be larger than 1 MB. Use a full or relative path to a local file
containing the value of ldif_file.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `managedidentities/v1beta1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud active-directory domains extend-schema
```

```
gcloud alpha active-directory domains extend-schema
```