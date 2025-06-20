# gcloud storage buckets notifications create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create)*

**NAME**

: **gcloud storage buckets notifications create - create a notification configuration on a bucket**

**SYNOPSIS**

: **`gcloud storage buckets notifications create` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#URL)` [`[--custom-attributes](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#--custom-attributes)`=[`KEY`=`VALUE`,…], `[-m](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#-m)` [`[KEY](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#KEY)`=`VALUE`,…]] [`[--event-types](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#--event-types)`=[`NOTIFICATION_EVENT_TYPE`,…], `[-e](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#-e)` [`[NOTIFICATION_EVENT_TYPE](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#NOTIFICATION_EVENT_TYPE)`,…]] [`[--object-prefix](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#--object-prefix)`=`OBJECT_PREFIX`, `[-p](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#-p)` `[OBJECT_PREFIX](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#OBJECT_PREFIX)`] [`[--payload-format](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#--payload-format)`=`PAYLOAD_FORMAT`, `[-f](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#-f)` `[PAYLOAD_FORMAT](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#PAYLOAD_FORMAT)`; default="json"] [`[--skip-topic-setup](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#--skip-topic-setup)`, `[-s](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#-s)`] [`[--topic](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#--topic)`=`TOPIC`, `[-t](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#-t)` `[TOPIC](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#TOPIC)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage buckets notifications create` creates a notification
configuration on a bucket, establishing a flow of event notifications from Cloud
Storage to a Cloud Pub/Sub topic. As part of creating this flow, it also
verifies that the destination Cloud Pub/Sub topic exists, creating it if
necessary, and verifies that the Cloud Storage bucket has permission to publish
events to that topic, granting the permission if necessary.
If a destination Cloud Pub/Sub topic is not specified with the `-t`
flag, Cloud Storage chooses a topic name in the default project whose ID is the
same as the bucket name. For example, if the default project ID specified is
`default-project` and the bucket being configured is
`gs://example-bucket`, the create command uses the Cloud Pub/Sub
topic `projects/default-project/topics/example-bucket`.
In order to enable notifications, your project's [Cloud
Storage service agent](https://cloud.google.com/storage/docs/projects#service-accounts) must have the IAM permission "pubsub.topics.publish".
This command checks to see if the destination Cloud Pub/Sub topic grants the
service agent this permission. If not, the create command attempts to grant it.
A bucket can have up to 100 total notification configurations and up to 10
notification configurations set to trigger for a specific event.

**EXAMPLES**

: Send notifications of all changes to the bucket `example-bucket` to
the Cloud Pub/Sub topic
`projects/default-project/topics/example-bucket`:

```
gcloud storage buckets notifications create gs://example-bucket
```

The same as the above but sends no notification payload:

```
gcloud storage buckets notifications create --payload-format=none gs://example-bucket
```

Include custom metadata in notification payloads:

```
gcloud storage buckets notifications create --custom-attributes=key1:value1,key2:value2 gs://example-bucket
```

Create a notification configuration that only sends an event when a new object
has been created or an object is deleted:

```
gcloud storage buckets notifications create --event-types=OBJECT_FINALIZE,OBJECT_DELETE gs://example-bucket
```

Create a topic and notification configuration that sends events only when they
affect objects with the prefix `photos/`:

```
gcloud storage buckets notifications create --object-prefix=photos/ gs://example-bucket
```

Specifies the destination topic ID `files-to-process` in the default
project:

```
gcloud storage buckets notifications create --topic=files-to-process gs://example-bucket
```

The same as above but specifies a Cloud Pub/Sub topic belonging to the specific
cloud project `example-project`:

```
gcloud storage buckets notifications create --topic=projects/example-project/topics/files-to-process gs://example-bucket
```

Skip creating a topic when creating the notification configuraiton:

```
gcloud storage buckets notifications create --skip-topic-setup gs://example-bucket
```

**POSITIONAL ARGUMENTS**

: **`URL`**:
URL of the bucket to create the notification configuration on.

**FLAGS**

: **--custom-attributes**:
Specifies key:value attributes that are appended to the set of attributes sent
to Cloud Pub/Sub for all events associated with this notification configuration.

**--event-types**:
Specify event type filters for this notification configuration. Cloud Storage
will send notifications of only these types. By default, Cloud Storage sends
notifications for all event types. * OBJECT_FINALIZE: An object has been
created. * OBJECT_METADATA_UPDATE: The metadata of an object has changed. *
OBJECT_DELETE: An object has been permanently deleted. * OBJECT_ARCHIVE: A live
version of an object has become a noncurrent version.
`NOTIFICATION_EVENT_TYPE` must be one of:
`OBJECT_ARCHIVE`, `OBJECT_DELETE`,
`OBJECT_FINALIZE`, `OBJECT_METADATA_UPDATE`.

**--object-prefix**:
Specifies a prefix path for this notification configuration. Cloud Storage will
send notifications for only objects in the bucket whose names begin with the
prefix.

**--payload-format**:
Specifies the payload format of notification messages. Notification details are
available in the message attributes. 'none' sends no payload.
`PAYLOAD_FORMAT` must be one of: `json`,
`none`.

**--skip-topic-setup**:
Skips creation and permission assignment of the Cloud Pub/Sub topic. This is
useful if the caller does not have permission to access the topic in question,
or if the topic already exists and has the appropriate publish permission
assigned.

**--topic**:
Specifies the Cloud Pub/Sub topic to send notifications to. If not specified,
this command chooses a topic whose project is your default project and whose ID
is the same as the Cloud Storage bucket name.

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

: This variant is also available:

```
gcloud alpha storage buckets notifications create
```