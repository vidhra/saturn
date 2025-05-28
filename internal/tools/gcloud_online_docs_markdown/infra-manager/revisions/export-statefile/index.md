# gcloud infra-manager revisions export-statefile  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/revisions/export-statefile](https://cloud.google.com/sdk/gcloud/reference/infra-manager/revisions/export-statefile)*

**NAME**

: **gcloud infra-manager revisions export-statefile - export a terraform state file**

**SYNOPSIS**

: **`gcloud infra-manager revisions export-statefile` (`[REVISION](https://cloud.google.com/sdk/gcloud/reference/infra-manager/revisions/export-statefile#REVISION)` : `[--deployment](https://cloud.google.com/sdk/gcloud/reference/infra-manager/revisions/export-statefile#--deployment)`=`DEPLOYMENT` `[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/revisions/export-statefile#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/revisions/export-statefile#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command generates a signed url to download a terraform state file.

**EXAMPLES**

: Export state file for revision
`projects/p1/locations/l1/deployments/d1/revisions/r-0`:

```
gcloud infra-manager revisions export-statefile projects/p1/locations/l1/deployments/d1/revisions/r-0
```

**POSITIONAL ARGUMENTS**

: **Revision resource - the revision to be used as parent. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`REVISION`**:
ID of the revision or fully qualified identifier for the revision.
To set the `revision` attribute:

- provide the argument `REVISION` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--deployment**:
The deployment for the revision.
To set the `deployment` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- provide the argument `--deployment` on the command line.

**--location**:
The Cloud location for the revision.
To set the `location` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.**

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