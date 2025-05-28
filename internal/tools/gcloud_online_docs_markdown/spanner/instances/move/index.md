# gcloud spanner instances move  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/instances/move](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/move)*

**NAME**

: **gcloud spanner instances move - move the Cloud Spanner instance to the specified instance configuration**

**SYNOPSIS**

: **`gcloud spanner instances move` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/move#INSTANCE)` `[--target-config](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/move#--target-config)`=`TARGET_CONFIG` [`[--target-database-move-configs](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/move#--target-database-move-configs)`=[^:^`database-id`=`DATABASE_ID`:`kms-key-names`=`KEY1`,`[KEY2](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/move#KEY2)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/move#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Move the Cloud Spanner instance to the specified instance configuration.

**EXAMPLES**

: To move the Cloud Spanner instance, which has two CMEK-enabled databases db1 and
db2 and a database db3 with Google-managed encryption keys, to the target
instance configuration nam3 (us-east4, us-east1, us-central1), run:
```
gcloud spanner instances move my-instance-id --target-config=nam3 --target-database-move-configs=^:^database-id=db1:kms-key-names=projects/myproject/locations/us-east4/keyRings/mykeyring/cryptoKeys/cmek-key,projects/myproject/locations/us-east1/keyRings/mykeyring/cryptoKeys/cmek-key,projects/myproject/locations/us-central1/keyRings/mykeyring/cryptoKeys/cmek-key --target-database-move-configs=^:^database-id=db2:kms-key-names=projects/myproject/locations/us-east4/keyRings/mykeyring/cryptoKeys/cmek-key,projects/myproject/locations/us-east1/keyRings/mykeyring/cryptoKeys/cmek-key,projects/myproject/locations/us-central1/keyRings/mykeyring/cryptoKeys/cmek-key
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud Spanner instance ID.

**REQUIRED FLAGS**

: **--target-config**:
Target Instance configuration to move the instances.

**OPTIONAL FLAGS**

: **--target-database-move-configs**:
Database level configurations for each database to be moved. Currently only used
for CMEK-enabled databases to specificy the target database KMS keys. Sets
`target_database_move_configs` value.

**`database-id`**:
Required, sets `database-id` value.

**`kms-key-names`**:
Sets `kms-key-names` value.

`Shorthand Example:`

```
--target-database-move-configs=database-id=string,kms-key-names=string --target-database-move-configs=database-id=string,kms-key-names=string
```

`JSON Example:`

```
--target-database-move-configs='[{"database-id": "string", "kms-key-names": "string"}]'
```

`File Example:`

```
--target-database-move-configs=path_to_file.(yaml|json)
```

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
gcloud alpha spanner instances move
```

```
gcloud beta spanner instances move
```