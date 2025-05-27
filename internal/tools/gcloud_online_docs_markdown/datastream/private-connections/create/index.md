# gcloud datastream private-connections create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create)*

**NAME**

: **gcloud datastream private-connections create - create a Datastream private connection**

**SYNOPSIS**

: **`gcloud datastream private-connections create` (`[PRIVATE_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create#PRIVATE_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create#--location)`=`LOCATION`) `[--display-name](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create#--display-name)`=`DISPLAY_NAME` (`[--network-attachment](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create#--network-attachment)`=`NETWORK_ATTACHMENT`     | `[--subnet](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create#--subnet)`=`SUBNET` `[--vpc](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create#--vpc)`=`VPC`) [`[--labels](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Datastream private connection

**EXAMPLES**

: To create a privateConnection with VPC Peering called 'my-privateConnection',
run:

```
gcloud datastream private-connections create my-privateConnection --location=us-central1 --display-name=my-privateConnection --vpc=vpc-example --subnet=10.0.0.0/29
```

To create a privateConnection with PSC Interface called 'my-privateConnection',
run:

```
gcloud datastream private-connections create my-privateConnection --location=us-central1 --display-name=my-privateConnection --network-attachment=network-attachment-example
```

**POSITIONAL ARGUMENTS**

: **Private connection resource - The private connection to create. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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
The Cloud location for the private_connection.
To set the `location` attribute:

- provide the argument `private_connection` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--display-name**:
Friendly name for the private connection.

**--network-attachment**

**OPTIONAL FLAGS**

: **--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--validate-only**:
If set, the request will retrieve the project id to allow in the network
attachment Datastream will connect to.

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
gcloud beta datastream private-connections create
```