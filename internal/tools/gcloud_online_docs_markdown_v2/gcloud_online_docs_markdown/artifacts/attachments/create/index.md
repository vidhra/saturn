# gcloud artifacts attachments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create)*

**NAME**

: **gcloud artifacts attachments create - creates an Artifact Registry attachment in a repository**

**SYNOPSIS**

: **`gcloud artifacts attachments create` (`[ATTACHMENT](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create#ATTACHMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create#--repository)`=`REPOSITORY`) `[--attachment-type](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create#--attachment-type)`=`ATTACHMENT_TYPE` `[--files](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create#--files)`=[`FILES`,…] `[--target](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create#--target)`=`TARGET` [`[--attachment-namespace](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create#--attachment-namespace)`=`ATTACHMENT_NAMESPACE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates an Artifact Registry attachment in a repository.

**EXAMPLES**

: To create an attachment for target
`projects/myproject/locations/us-central1/packages/mypackage/versions/sha256:123`
using a file located in `/path/to/file/sbom.json`:

```
gcloud artifacts attachments create --target=projects/myproject/locations/us-central1/packages/mypackage/versions/sha256:123 --files=/path/to/file/sbom.json
```

**POSITIONAL ARGUMENTS**

: **Attachment resource - The Artifact Registry attachment name. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `attachment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ATTACHMENT`**:
ID of the attachment or fully qualified identifier for the attachment.
To set the `name` attribute:

- provide the argument `attachment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the attachment.
To set the `location` attribute:

- provide the argument `attachment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
Repository of the attachment.
To set the `repository` attribute:

- provide the argument `attachment` on the command line with a fully
specified name;
- provide the argument `--repository` on the command line;
- set the property `artifacts/repository`.**

**REQUIRED FLAGS**

: **--attachment-type**:
Type of the attachment

**--files**:
Comma-seperated list of files that are part of this attachment

**--target**:
Target of the attachment, should be fully qualified version name

**OPTIONAL FLAGS**

: **--attachment-namespace**:
Namespace of the attachment

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