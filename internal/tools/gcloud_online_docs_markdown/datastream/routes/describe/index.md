# gcloud datastream routes describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/routes/describe](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/describe)*

**NAME**

: **gcloud datastream routes describe - show details about the route**

**SYNOPSIS**

: **`gcloud datastream routes describe` (`[ROUTE](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/describe#ROUTE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/describe#--location)`=`LOCATION` `[--private-connection](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/describe#--private-connection)`=`PRIVATE_CONNECTION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details about the route.

**EXAMPLES**

: To show details about a device, run:

```
gcloud datastream routes describe my-route --private-connection=pc --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Route resource - The route you want to describe. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `route` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ROUTE`**:
ID of the route or fully qualified identifier for the route.
To set the `route` attribute:

- provide the argument `route` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the resources.
To set the `location` attribute:

- provide the argument `route` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--private-connection**:
The private connection name.
To set the `private-connection` attribute:

- provide the argument `route` on the command line with a fully
specified name;
- provide the argument `--private-connection` on the command line.**

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
gcloud beta datastream routes describe
```