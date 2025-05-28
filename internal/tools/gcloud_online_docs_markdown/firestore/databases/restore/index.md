# gcloud firestore databases restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/databases/restore](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/restore)*

**NAME**

: **gcloud firestore databases restore - restores a Cloud Firestore database from a backup**

**SYNOPSIS**

: **`gcloud firestore databases restore` `[--destination-database](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/restore#--destination-database)`=`DESTINATION_DATABASE` `[--source-backup](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/restore#--source-backup)`=`SOURCE_BACKUP` [`[--encryption-type](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/restore#--encryption-type)`=`ENCRYPTION_TYPE` : `[--kms-key-name](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/restore#--kms-key-name)`=`KMS_KEY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/restore#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To restore a database from a backup.

```
gcloud firestore databases restore --source-backup=projects/PROJECT_ID/locations/LOCATION_ID/backups/BACKUP_ID --destination-database=DATABASE_ID
```

To restore to a CMEK-enabled database.

```
gcloud firestore databases restore --source-backup=projects/PROJECT_ID/locations/LOCATION_ID/backups/BACKUP_ID --destination-database=DATABASE_ID --encryption-type=customer-managed-encryption --kms-key-name=projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KEY_RING_ID/cryptoKeys/CRYPTO_KEY_ID
```

**REQUIRED FLAGS**

: **--destination-database**:
Destination database to restore to. Destination database will be created in the
same location as the source backup.
This value should be 4-63 characters. Valid characters are /[a-z][0-9]-/ with
first character a letter and the last a letter or a number. Must not be
UUID-like /[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/.
Using "(default)" database ID is also allowed.
For example, to restore to database `testdb`:

```
gcloud firestore databases restore --destination-database=testdb
```

**--source-backup**:
The source backup to restore from.
For example, to restore from backup
`cf9f748a-7980-4703-b1a1-d1ffff591db0` in us-east1:

```
gcloud firestore databases restore --source-backup=projects/PROJECT_ID/locations/us-east1/backups/cf9f748a-7980-4703-b1a1-d1ffff591db0
```

**OPTIONAL FLAGS**

: **The encryption configuration of the new database being created from the backup.
If not specified, the same encryption settings as the backup will be used.
To create a CMEK-enabled database:

```
gcloud firestore databases restore --encryption-type=customer-managed-encryption --kms-key-name=projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KEY_RING_ID/cryptoKeys/CRYPTO_KEY_ID
```

To create a Google-default-encrypted database:

```
gcloud firestore databases restore --encryption-type=google-default-encryption
```

To create a database using the same encryption settings as the backup:

```
gcloud firestore databases restore --encryption-type=use-source-encryption
```

**--encryption-type**:
The encryption type of the destination database.
`ENCRYPTION_TYPE` must be one of:
`use-source-encryption`, `customer-managed-encryption`,
`google-default-encryption`.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--kms-key-name**:
The resource ID of a Cloud KMS key. If set, the database created will be a
Customer-Managed Encryption Key (CMEK) database encrypted with this key. This
feature is allowlist only in initial launch.
Only a key in the same location as this database is allowed to be used for
encryption. For Firestore's nam5 multi-region, this corresponds to Cloud KMS
location us. For Firestore's eur3 multi-region, this corresponds to Cloud KMS
location europe. See [https://cloud.google.com/kms/docs/locations](https://cloud.google.com/kms/docs/locations).
This value should be the KMS key resource ID in the format of
`projects/{project_id}/locations/{kms_location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.
How to retrieve this resource ID is listed at [https://cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version](https://cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version).
This flag must only be specified when encryption-type is
`customer-managed-encryption`.**

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
gcloud alpha firestore databases restore
```

```
gcloud beta firestore databases restore
```