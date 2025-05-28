# gcloud apphub service-projects remove  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apphub/service-projects/remove](https://cloud.google.com/sdk/gcloud/reference/apphub/service-projects/remove)*

**NAME**

: **gcloud apphub service-projects remove - remove an Apphub service project**

**SYNOPSIS**

: **`gcloud apphub service-projects remove` (`[SERVICE_PROJECT](https://cloud.google.com/sdk/gcloud/reference/apphub/service-projects/remove#SERVICE_PROJECT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/apphub/service-projects/remove#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/apphub/service-projects/remove#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apphub/service-projects/remove#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove an Apphub service project.

**EXAMPLES**

: To remove the service project `my-service-project` from the host
project `my-host-project`, run:

```
gcloud apphub service-projects remove my-service-project --project=my-host-project
```

**POSITIONAL ARGUMENTS**

: **ServiceProjectAttachment resource - The Service Project ID. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `service_project` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE_PROJECT`**:
ID of the ServiceProjectAttachment or fully qualified identifier for the
ServiceProjectAttachment.
To set the `service_project` attribute:

- provide the argument `service_project` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the ServiceProjectAttachment.
To set the `location` attribute:

- provide the argument `service_project` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- Service project attachments only support global location.**

**FLAGS**

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

**NOTES**

: This variant is also available:

```
gcloud alpha apphub service-projects remove
```