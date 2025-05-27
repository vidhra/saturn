# gcloud database-migration private-connections create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create)*

**NAME**

: **gcloud database-migration private-connections create - create a Database Migration private connection**

**SYNOPSIS**

: **`gcloud database-migration private-connections create` (`[PRIVATE_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create#PRIVATE_CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create#--region)`=`REGION`) `[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create#--display-name)`=`DISPLAY_NAME` (`[--subnet](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create#--subnet)`=`SUBNET` `[--vpc](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create#--vpc)`=`VPC`) [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--skip-validation](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create#--skip-validation)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/private-connections/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Database Migration private connection

**EXAMPLES**

: To create a private connection called 'my-private-connection', run:

```
gcloud database-migration private-connections create my-private-connection --region=us-central1 --display-name=my-private-connection --vpc=vpc-example --subnet=10.0.0.0/29
```

```
To use a private connection, all migrations and connection profiles that use this configuration must be in the same region.
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

**--region**:
The Cloud region for the private_connection.
To set the `region` attribute:

- provide the argument `private_connection` on the command line with a
fully specified name;
- provide the argument `--region` on the command line.**

**REQUIRED FLAGS**

: **--display-name**:
A user-friendly name for the private connection. The display name can include
letters, numbers, spaces, and hyphens, and must start with a letter. The maximum
length allowed is 60 characters.

**--subnet**

**OPTIONAL FLAGS**

: **--no-async**:
Waits for the operation in progress to complete before returning.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--skip-validation**:
Creates the private connection without running prior verifications.

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