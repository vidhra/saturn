# gcloud datastream private-connections delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/delete](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/delete)*

**NAME**

: **gcloud datastream private-connections delete - delete a Datastream private connection**

**SYNOPSIS**

: **`gcloud datastream private-connections delete` (`[PRIVATE_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/delete#PRIVATE_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/delete#--location)`=`LOCATION`) [`[--force](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/delete#--force)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes a private connection. You must set the --force parameter to ensure that
the private connectivity configuration is deleted properly.

**EXAMPLES**

: To delete a private connection:

```
gcloud datastream private-connections delete PRIVATE_CONNECTION --location=us-central1 --force
```

**POSITIONAL ARGUMENTS**

: **Private connection resource - Private connection resource - Private connection
to delete. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `private_connection` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PRIVATE_CONNECTION`**:
ID of the private_connection or fully qualified identifier for the
private_connection.
To set the `private_connection` attribute:

- provide the argument `private_connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the resources.
To set the `location` attribute:

- provide the argument `private_connection` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--force**:
You must set the force to ensure that the private connectivity configuration is
deleted properly.

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

: This command uses the `datastream/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/datastream/](https://cloud.google.com/datastream/)

**NOTES**

: This variant is also available:

```
gcloud beta datastream private-connections delete
```