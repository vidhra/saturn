# gcloud datastore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastore](https://cloud.google.com/sdk/gcloud/reference/datastore)*

**NAME**

: **gcloud datastore - manage your Cloud Datastore resources**

**SYNOPSIS**

: **`gcloud datastore` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/datastore#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/datastore#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cloud Datastore is a highly-scalable NoSQL database for your applications. Cloud
Datastore automatically handles sharding and replication, providing you with a
highly available and durable database that scales automatically to handle your
applications' load.
More information on Cloud Datastore can be found here: [https://cloud.google.com/datastore](https://cloud.google.com/datastore)
and detailed documentation can be found here: [https://cloud.google.com/datastore/docs](https://cloud.google.com/datastore/docs)
export -- Export data to Google Cloud Storage
import -- Import data from Google Cloud Storage
indexes -- Manage your Cloud Firestore indexes.
operations -- Manage Long Running Operations for Cloud Firestore.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[indexes](https://cloud.google.com/sdk/gcloud/reference/datastore/indexes)`**:
Manage your Cloud Datastore indexes.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/datastore/operations)`**:
Manage Long Running Operations for Cloud Datastore.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[export](https://cloud.google.com/sdk/gcloud/reference/datastore/export)`**:
Export Cloud Datastore entities to Google Cloud Storage.

**`[import](https://cloud.google.com/sdk/gcloud/reference/datastore/import)`**:
Import Cloud Datastore entities from Google Cloud Storage.

**NOTES**

: These variants are also available:

```
gcloud alpha datastore
```

```
gcloud beta datastore
```