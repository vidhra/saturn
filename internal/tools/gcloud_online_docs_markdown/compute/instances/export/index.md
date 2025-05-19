# gcloud compute instances export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/export](https://cloud.google.com/sdk/gcloud/reference/compute/instances/export)*

**NAME**

: **gcloud compute instances export - export a Compute Engine virtual machine instance's configuration to a file**

**SYNOPSIS**

: **`gcloud compute instances export` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/instances/export#INSTANCE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/export#--zone)`=`ZONE`) [`[--destination](https://cloud.google.com/sdk/gcloud/reference/compute/instances/export#--destination)`=`DESTINATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export a Compute Engine virtual machine instance's configuration to a file.

**EXAMPLES**

: A virtual machine can be exported by running:

```
gcloud compute instances export my-instance --destination=<path-to-file>
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Name of the instance to export. For details on valid
instance names, refer to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The name of the Google Compute Engine zone.
To set the `zone` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. The exported data
will not contain any output-only fields. Alternatively, you may omit this flag
to write to standard output. For a schema describing the export/import format,
see $CLOUDSDKROOT/lib/googlecloudsdk/schemas/…

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

: This command uses the `compute/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: These variants are also available:

```
gcloud alpha compute instances export
```

```
gcloud beta compute instances export
```