# gcloud looker instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/looker/instances](https://cloud.google.com/sdk/gcloud/reference/looker/instances)*

**NAME**

: **gcloud looker instances - manage Looker instances**

**SYNOPSIS**

: **`gcloud looker instances` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/looker/instances#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/looker/instances#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create an instance with the name `my-looker-instance`, with an
edition of "LOOKER_CORE_STANDARD", run:

```
gcloud looker instances create my-looker-instance --oauth-client-id='looker' --oauth-client-secret='looker' --edition="core-standard" --async
```

Note: It is `recommended` that the `--async` argument is
provided when creating a Looker instance.
To delete an instance with the name `my-looker-instance`, run:

```
gcloud looker instances delete my-looker-instance --async
```

To display the details for an instance with name
`my-looker-instance`, run:

```
gcloud looker instances describe my-looker-instance
```

To restart an instance with the name `my-looker-instance`, run:

```
gcloud looker instances restart my-looker-instance --async
```

To update an instance with the name `my-looker-instance`, run:

```
gcloud looker instances update my-looker-instance --async
```

To restore a backup with id of `7e504e66-c389-4d8d` that belongs to
an instance named `my-looker-instance`, in the region
`us-central1`, run:
$ [gcloud looker
instances restore](https://cloud.google.com/sdk/gcloud/reference/looker/instances/restore) my-looker-instance \
```
--backup="7e504e66-c389-4d8" --region="us-central1" --async
```

To export an instance with the name `my-looker-instance`, run:

```
gcloud looker instances export my-looker-instance --target-gcs-uri='gs://bucketName/folderName' --kms-key='projects/my-project/locations/us-central1/keyRings/my-key-ring/cryptoKeys/my-key'
```

To import an instance with the name `my-looker-instance`, run:

```
gcloud looker instances import my-looker-instance --source-gcs-uri='gs://bucketName/folderName'
```

To list all the instances, run:

```
gcloud looker instances list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/looker/instances/create)`**:
Create a Looker instance.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/looker/instances/delete)`**:
Delete a Looker instance.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/looker/instances/describe)`**:
Show metadata for a Looker instance.

**`[export](https://cloud.google.com/sdk/gcloud/reference/looker/instances/export)`**:
Export a Looker instance.

**`[import](https://cloud.google.com/sdk/gcloud/reference/looker/instances/import)`**:
Import a Looker instance.

**`[list](https://cloud.google.com/sdk/gcloud/reference/looker/instances/list)`**:
List Looker instances.

**`[restart](https://cloud.google.com/sdk/gcloud/reference/looker/instances/restart)`**:
Restart a Looker instance.

**`[restore](https://cloud.google.com/sdk/gcloud/reference/looker/instances/restore)`**:
Restore a Looker instance from a backup.

**`[update](https://cloud.google.com/sdk/gcloud/reference/looker/instances/update)`**:
Update a Looker instance.

**NOTES**

: This variant is also available:

```
gcloud alpha looker instances
```