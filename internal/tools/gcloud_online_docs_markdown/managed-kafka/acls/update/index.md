# gcloud managed-kafka acls update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update)*

**NAME**

: **gcloud managed-kafka acls update - update a Managed Service for Apache Kafka acl**

**SYNOPSIS**

: **`gcloud managed-kafka acls update` (`[ACL](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update#ACL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update#--location)`=`LOCATION`) `[--etag](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update#--etag)`=`ETAG` (`[--acl-entries-from-file](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update#--acl-entries-from-file)`=`PATH_TO_FILE`     | `[--acl-entry](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update#--acl-entry)`=[`host`=`HOST`],[`operation`=`OPERATION`],[`permission-type`=`PERMISSION-TYPE`],[`principal`=`PRINCIPAL`]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Managed Service for Apache Kafka acl.
NOTE: update performs a FULL REPLACEMENT of acl entries. For incremental
updates, use add-acl-entry and remove-acl-entry commands.

**EXAMPLES**

: To update an acl for the Kafka cluster resource pattern, with etag W/XYZ123
returned from a previous create or describe command, in a cluster named
mycluster located in us-central1, run the following:

```
gcloud managed-kafka acls update cluster --cluster=mycluster --location=us-central1 --acl-entry=principal='User:admin@project.iam.gserviceaccount.com',operation=ALL,permission-type=ALLOW,host='*' --etag=W/XYZ123
```

**POSITIONAL ARGUMENTS**

: **Acl resource - Identifies the name of the acl that this command updates. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `acl` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ACL`**:
ID of the acl or fully qualified identifier for the acl.
To set the `acl` attribute:

- provide the argument `acl` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
The cluster name.
To set the `cluster` attribute:

- provide the argument `acl` on the command line with a fully specified
name;
- provide the argument `--cluster` on the command line.

**--location**:
ID of the location of the Managed Service for Apache Kafka resource. See [https://cloud.google.com/managed-service-for-apache-kafka/docs/locations](https://cloud.google.com/managed-service-for-apache-kafka/docs/locations)
for a list of supported locations.
To set the `location` attribute:

- provide the argument `acl` on the command line with a fully specified
name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--etag**:
etag returned in the response to a previous create or describe command. The etag
is used for concurrency control, to ensure that the client and server agree on
the current set of acl entries in the Kafka cluster, before full replacement in
the update command.

**--acl-entries-from-file**

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

: This command uses the `managedkafka/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/managed-service-for-apache-kafka/docs](https://cloud.google.com/managed-service-for-apache-kafka/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha managed-kafka acls update
```

```
gcloud beta managed-kafka acls update
```