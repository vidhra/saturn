# gcloud network-security intercept-endpoint-group-associations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create)*

**NAME**

: **gcloud network-security intercept-endpoint-group-associations create - create an Intercept Endpoint Group Association**

**SYNOPSIS**

: **`gcloud network-security intercept-endpoint-group-associations create` (`[INTERCEPT_ENDPOINT_GROUP_ASSOCIATION](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create#INTERCEPT_ENDPOINT_GROUP_ASSOCIATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create#--location)`=`LOCATION`) `[--network](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create#--network)`=`NETWORK` (`[--intercept-endpoint-group](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create#--intercept-endpoint-group)`=`INTERCEPT_ENDPOINT_GROUP` : `[--intercept-endpoint-group-location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create#--intercept-endpoint-group-location)`=`INTERCEPT_ENDPOINT_GROUP_LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create#--max-wait)`=`MAX_WAIT`; default="20m"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an intercept endpoint group association. Successful creation of an
association results in an association in ACTIVE state. Check the progress of
association creation by using `[gcloud
network-security intercept-endpoint-group-associations list](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/list)`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To create an intercept endpoint group association called
`my-association`, in project ID `my-project`, run:
$ [gcloud
network-security intercept-endpoint-group-associations](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations) \
```
create my-association --project=my-project --location=global \
--intercept-endpoint-group=my-endpoint-group \
--network=my-network
```

OR
$ [gcloud
network-security intercept-endpoint-group-associations](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations) \
```
create my-association --project=my-project --location=global \
--intercept-endpoint-group=my-endpoint-group \
--network=projects/my-project/global/networks/my-network
```

OR
$ [gcloud
network-security intercept-endpoint-group-associations](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations) \
```
create \
projects/my-project/locations/global/\
interceptEndpointGroupAssociations/my-association \
    --intercept-endpoint-group=projects/my-project/locations/\
global/interceptEndpointGroups/my-endpoint-group \
    --network=projects/my-project/global/networks/my-network
```

**POSITIONAL ARGUMENTS**

: **Intercept endpoint group association resource - Intercept Endpoint Group
Association. The arguments in this group can be used to specify the attributes
of this resource. (NOTE) Some attributes are not given arguments in this group
but can be set in other ways.
To set the `project` attribute:

- provide the argument `INTERCEPT_ENDPOINT_GROUP_ASSOCIATION` on the
command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERCEPT_ENDPOINT_GROUP_ASSOCIATION`**:
ID of the intercept endpoint group association or fully qualified identifier for
the intercept endpoint group association.
To set the `endpoint-group-association-id` attribute:

- provide the argument `INTERCEPT_ENDPOINT_GROUP_ASSOCIATION` on the
command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the intercept endpoint group association.
To set the `location` attribute:

- provide the argument `INTERCEPT_ENDPOINT_GROUP_ASSOCIATION` on the
command line with a fully specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **Network resource - Intercept Endpoint Group Association. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--network**:
ID of the network or fully qualified identifier for the network.
To set the `network-name` attribute:

- provide the argument `--network` on the command line.**

**Intercept endpoint group resource - Intercept Endpoint Group. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--intercept-endpoint-group` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--intercept-endpoint-group**:
ID of the intercept endpoint group or fully qualified identifier for the
intercept endpoint group.
To set the `id` attribute:

- provide the argument `--intercept-endpoint-group` on the command
line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--intercept-endpoint-group-location**:
Location of the intercept endpoint group.
To set the `location` attribute:

- provide the argument `--intercept-endpoint-group` on the command line
with a fully specified name;
- provide the argument `--intercept-endpoint-group-location` on the
command line;
- provide the argument `--location` on the command line;
- provide the argument
`networksecurity.projects.locations.interceptEndpointGroupAssociations`
on the command line with a fully specified name.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--max-wait**:
Time to synchronously wait for the operation to complete, after which the
operation continues asynchronously. Ignored if --no-async isn't specified. See $
[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

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
gcloud alpha network-security intercept-endpoint-group-associations create
```

```
gcloud beta network-security intercept-endpoint-group-associations create
```