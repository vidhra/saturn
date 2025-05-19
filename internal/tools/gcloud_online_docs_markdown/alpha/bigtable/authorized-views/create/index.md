# gcloud alpha bigtable authorized-views create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create)*

**NAME**

: **gcloud alpha bigtable authorized-views create - create a new Cloud Bigtable authorized view**

**SYNOPSIS**

: **`gcloud alpha bigtable authorized-views create` (`[AUTHORIZED_VIEW](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create#AUTHORIZED_VIEW)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create#--instance)`=`INSTANCE` `[--table](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create#--table)`=`TABLE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create#--async)`] [`[--definition-file](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create#--definition-file)`=`DEFINITION_FILE`] [`[--pre-encoded](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create#--pre-encoded)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new Cloud Bigtable authorized view.

**EXAMPLES**

: To create an authorized view 'my-authorized-view' in instance 'my-instance' and
table 'my-table', using the definition file 'authorized_view.json':

```
gcloud alpha bigtable authorized-views create my-authorized-view --instance=test-instance --table=test-table --definition-file=authorized_view.json
```

To create an authorized view 'my-authorized-view' in instance 'my-instance' and
table 'my-table', using the pre-encoded definition file
'authorized_view_pre_encoded.json':

```
gcloud alpha bigtable authorized-views create my-authorized-view --instance=test-instance --table=test-table --definition-file=authorized_view_pre_encoded.json --pre-encoded
```

**POSITIONAL ARGUMENTS**

: **Authorized view resource - Cloud Bigtable authorized view to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `authorized_view` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`AUTHORIZED_VIEW`**:
ID of the authorized-view or fully qualified identifier for the authorized-view.
To set the `authorized_view` attribute:

- provide the argument `authorized_view` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Name of the Cloud Bigtable instance.
To set the `instance` attribute:

- provide the argument `authorized_view` on the command line with a
fully specified name;
- provide the argument `--instance` on the command line.

**--table**:
Name of the Cloud Bigtable table.
To set the `table` attribute:

- provide the argument `authorized_view` on the command line with a
fully specified name;
- provide the argument `--table` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--definition-file**:
Path to a JSON or YAML file containing a valid authorized view protobuf.
The 'name' field is ignored. The name is deduced from the other command line
arguments.
Example: { "subsetView": { "rowPrefixes": ["store1#"], "familySubsets": {
"column_family_name": { "qualifiers":["address"], "qualifierPrefixes":["tel"] }
} }, "deletionProtection": true }

**--pre-encoded**:
By default, Base64 encoding is applied to all binary fields ("rowPrefixes",
"qualifiers" and "qualifierPrefixes") in the JSON or YAML definition file.
Use this to indicate that all binary fields are already Base64-encoded and
should be used directly.

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

: This command uses the `bigtableadmin/v2` API. The full documentation
for this API can be found at: [https://cloud.google.com/bigtable/](https://cloud.google.com/bigtable/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud bigtable authorized-views create
```

```
gcloud beta bigtable authorized-views create
```