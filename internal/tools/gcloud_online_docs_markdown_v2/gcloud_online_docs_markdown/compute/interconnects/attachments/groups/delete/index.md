# gcloud compute interconnects attachments groups delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/delete](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/delete)*

**NAME**

: **gcloud compute interconnects attachments groups delete - delete Compute Engine interconnect attachment groups**

**SYNOPSIS**

: **`gcloud compute interconnects attachments groups delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/delete#NAME)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects attachments groups delete` is used to
delete interconnect attachment groups.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To delete an interconnect attachment group, run:

```
gcloud compute interconnects attachments groups delete example-attachment-group"
```

Although not shown in this example, you can delete multiple interconnect
attachment groups in a single command.

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the interconnect attachment groups to delete.

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
gcloud alpha compute interconnects attachments groups delete
```

```
gcloud beta compute interconnects attachments groups delete
```