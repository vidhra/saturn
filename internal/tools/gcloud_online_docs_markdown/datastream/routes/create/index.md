# gcloud datastream routes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create)*

**NAME**

: **gcloud datastream routes create - create a Datastream private connection route**

**SYNOPSIS**

: **`gcloud datastream routes create` (`[ROUTE](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create#ROUTE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create#--location)`=`LOCATION` `[--private-connection](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create#--private-connection)`=`PRIVATE_CONNECTION`) `[--destination-address](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create#--destination-address)`=`DESTINATION_ADDRESS` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create#--display-name)`=`DISPLAY_NAME` [`[--destination-port](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create#--destination-port)`=`DESTINATION_PORT`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/routes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Datastream private connection route

**EXAMPLES**

: To create a route called 'my-route', run:

```
gcloud datastream routes create my-route --location=us-central1 --private-connection=private-connection --display-name=my-display-name --destination-address=addr.path.to.somewhere --destination-port=33665
```

**POSITIONAL ARGUMENTS**

: **Route resource - The route to create. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
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
The Cloud location for the route.
To set the `location` attribute:

- provide the argument `route` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--private-connection**:
The private connection of the route.
To set the `private-connection` attribute:

- provide the argument `route` on the command line with a fully
specified name;
- provide the argument `--private-connection` on the command line.**

**REQUIRED FLAGS**

: **--destination-address**:
Destination address for connection.

**--display-name**:
Friendly name for the route.

**OPTIONAL FLAGS**

: **--destination-port**:
Destination port for connection.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud beta datastream routes create
```