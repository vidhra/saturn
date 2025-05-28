# gcloud managed-kafka acls create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create)*

**NAME**

: **gcloud managed-kafka acls create - create a Managed Service for Apache Kafka acl**

**SYNOPSIS**

: **`gcloud managed-kafka acls create` (`[ACL](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create#ACL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create#--location)`=`LOCATION`) (`[--acl-entries-from-file](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create#--acl-entries-from-file)`=`PATH_TO_FILE`     | `[--acl-entry](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create#--acl-entry)`=[`host`=`HOST`],[`operation`=`OPERATION`],[`permission-type`=`PERMISSION-TYPE`],[`principal`=`PRINCIPAL`]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Managed Service for Apache Kafka acl.

**EXAMPLES**

: To create an acl for the Kafka cluster resource pattern (acl ID = cluster), in a
cluster named mycluster located in us-central1, run the following:

```
gcloud managed-kafka acls create cluster --cluster=mycluster --location=us-central1 --acl-entry=principal='User:admin@project.iam.gserviceaccount.com',operation=ALL,permission-type=ALLOW,host='*' --acl-entry=principal='User:reader@project.iam.gserviceaccount.com',operation=DESCRIBE,permission-type=ALLOW,host='*' --acl-entry=principal='User:reader@project.iam.gserviceaccount.com',operation=DESCRIBE_CONFIGS,permission-type=ALLOW,host='*'
```

This acl grants an "admin" service account access to ALL cluster-level
operations, and grants a "reader" service account access to cluster-level
DESCRIBE and DESCRIBE_CONFIGS operations.

**POSITIONAL ARGUMENTS**

: **Acl resource - Identifies the name of the acl that this command creates.
The structure of the acl ID defines the Resource Pattern for which the acl
entries apply in the Kafka cluster. The acl ID must be structured like one of
the following:

```
For acls on the cluster:
  cluster
```

```
For acls on a single resource within the cluster:
  topic/{resource_name}
  consumerGroup/{resource_name}
  transactionalId/{resource_name}
```

```
For acls on all resources that match a prefix:
  topicPrefixed/{resource_name}
  consumerGroupPrefixed/{resource_name}
  transactionalIdPrefixed/{resource_name}
```

```
For acls on all resources of a given type (i.e. the wildcard literal "*"):
  allTopics (represents topic/*)
  allConsumerGroups (represents consumerGroup/*)
  allTransactionalIds (represents transactionalId/*)
The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways.
```

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

: **--acl-entries-from-file**

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
gcloud alpha managed-kafka acls create
```

```
gcloud beta managed-kafka acls create
```