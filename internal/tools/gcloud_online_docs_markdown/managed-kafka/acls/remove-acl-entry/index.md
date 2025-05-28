# gcloud managed-kafka acls remove-acl-entry  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry)*

**NAME**

: **gcloud managed-kafka acls remove-acl-entry - remove an acl entry from a Managed Service for Apache Kafka acl**

**SYNOPSIS**

: **`gcloud managed-kafka acls remove-acl-entry` (`[ACL](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry#ACL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry#--location)`=`LOCATION`) `[--operation](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry#--operation)`=`OPERATION` `[--principal](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry#--principal)`=`PRINCIPAL` [`[--host](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry#--host)`=`HOST`; default=`"*"`] [`[--permission-type](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry#--permission-type)`=`PERMISSION_TYPE`; default="ALLOW"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove an acl entry from a Managed Service for Apache Kafka acl.

**EXAMPLES**

: To remove an acl entry for the Kafka cluster resource pattern (acl_id=cluster),
in a cluster named `mycluster` located in `us-central1`,
run the following:

```
gcloud managed-kafka acls remove-acl-entry cluster --cluster=mycluster --location=us-central1 --principal='User:admin@project.iam.gserviceaccount.com' --operation=ALL --permission-type=ALLOW --host='*'
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

: **--operation**:
The operation type. Allowed values are: ALL, READ, WRITE, CREATE, DELETE, ALTER,
DESCRIBE, CLUSTER_ACTION, DESCRIBE_CONFIGS, ALTER_CONFIGS, IDEMPOTENT_WRITE.
See [https://kafka.apache.org/documentation/#operations_resources_and_protocols](https://kafka.apache.org/documentation/#operations_resources_and_protocols)
for the mapping of operations to Kafka protocols.

**--principal**:
The principal. Specified as Google Cloud account, with the Kafka
StandardAuthorizer prefix "User:". For example:
"User:admin@project.iam.gserviceaccount.com". Can be the wildcard
"User:`*`" to refer to all users.

**OPTIONAL FLAGS**

: **--host**:
The host. Must be set to "`*`" for Managed Service for Apache Kafka.

**--permission-type**:
The permission type. Allowed values are: ALLOW, DENY.

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
gcloud alpha managed-kafka acls remove-acl-entry
```

```
gcloud beta managed-kafka acls remove-acl-entry
```