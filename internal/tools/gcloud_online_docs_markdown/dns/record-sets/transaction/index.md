# gcloud dns record-sets transaction  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction)*

**NAME**

: **gcloud dns record-sets transaction - make scriptable and transactional changes to your record-sets**

**SYNOPSIS**

: **`gcloud dns record-sets transaction` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction#COMMAND)` [`[--transaction-file](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction#--transaction-file)`=`TRANSACTION_FILE`; default="transaction.yaml"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Make scriptable and transactional changes to your record-sets.

**EXAMPLES**

: To start a transaction, run:

```
gcloud dns record-sets transaction start --zone=MANAGED_ZONE
```

To append a record-set addition to the transaction, run:

```
gcloud dns record-sets transaction add --name RECORD_SET_NAME --ttl TTL --type TYPE DATA --zone=MANAGED_ZONE
```

To append a record-set removal to the transaction, run:

```
gcloud dns record-sets transaction remove --name RECORD_SET_NAME --ttl TTL --type TYPE DATA
```

To look at the details of the transaction, run:

```
gcloud dns record-sets transaction describe --zone=MANAGED_ZONE
```

To delete the transaction, run:

```
gcloud dns record-sets transaction abort --zone=MANAGED_ZONE
```

To execute the transaction, run:

```
gcloud dns record-sets transaction execute --zone=MANAGED_ZONE
```

**FLAGS**

: **--transaction-file**:
Path of the file which contains the transaction.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[abort](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/abort)`**:
Abort transaction.

**`[add](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/add)`**:
Append a record-set addition to the transaction.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/describe)`**:
Describe the transaction.

**`[execute](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/execute)`**:
Execute the transaction on Cloud DNS.

**`[remove](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/remove)`**:
Append a record-set deletion to the transaction.

**`[start](https://cloud.google.com/sdk/gcloud/reference/dns/record-sets/transaction/start)`**:
Start a transaction.

**NOTES**

: These variants are also available:

```
gcloud alpha dns record-sets transaction
```

```
gcloud beta dns record-sets transaction
```