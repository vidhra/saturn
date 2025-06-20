# gcloud netapp active-directories delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/delete](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/delete)*

**NAME**

: **gcloud netapp active-directories delete - delete a Cloud NetApp Active Directory**

**SYNOPSIS**

: **`gcloud netapp active-directories delete` (`[ACTIVE_DIRECTORY](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/delete#ACTIVE_DIRECTORY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes an AD (Active Directory) config for Cloud NetApp Volumes.

**EXAMPLES**

: The following command deletes an AD named AD_NAME with the required arguments:

```
gcloud netapp active-directories delete AD_NAME --location=us-central1
```

To delete a AD Config asynchronously, run the following command:

```
gcloud netapp active-directories delete AD_NAME --location=us-central1 --async
```

**POSITIONAL ARGUMENTS**

: **Active directory resource - The Active Directory to delete. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `active_directory` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ACTIVE_DIRECTORY`**:
ID of the active_directory or fully qualified identifier for the
active_directory.
To set the `active_directory` attribute:

- provide the argument `active_directory` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the active_directory.
To set the `location` attribute:

- provide the argument `active_directory` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

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

: These variants are also available:

```
gcloud alpha netapp active-directories delete
```

```
gcloud beta netapp active-directories delete
```