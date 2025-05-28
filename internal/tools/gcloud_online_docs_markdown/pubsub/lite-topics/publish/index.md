# gcloud pubsub lite-topics publish  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish)*

**NAME**

: **gcloud pubsub lite-topics publish - publish Pub/Sub Lite messages**

**SYNOPSIS**

: **`gcloud pubsub lite-topics publish` (`[TOPIC](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish#TOPIC)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish#--location)`=`LOCATION`) [`[--attributes](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish#--attributes)`=[`KEY`=`VALUE`,…]] [`[--event-time](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish#--event-time)`=`DATETIME`] [`[--message](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish#--message)`=`MESSAGE`] [`[--ordering-key](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish#--ordering-key)`=`ORDERING_KEY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/publish#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Publishes a message to the specified Pub/Sub Lite topic. This command requires
Python 3.6 or greater, and requires the grpcio Python package to be installed.
For MacOS, Linux, and Cloud Shell users, to install the gRPC client libraries,
run:

```
sudo pip3 install grpcio
export CLOUDSDK_PYTHON_SITEPACKAGES=1
```

**EXAMPLES**

: To publish a message to a Pub/Sub Lite topic, run:

```
gcloud pubsub lite-topics publish mytopic --location=us-central1-a --message="Hello World!"
```

To publish a message to a Pub/Sub Lite topic with an ordering key and
attributes, run:

```
gcloud pubsub lite-topics publish mytopic --location=us-central1-a --message="Hello World!" --ordering-key="key" --attributes=KEY1=VAL1,KEY2=VAL2
```

To publish a message to a Pub/Sub Lite topic with an event time, run:

```
gcloud pubsub lite-topics publish mytopic --location=us-central1-a --message="Hello World!" --event-time="2021-01-01T12:00:00Z"
```

**POSITIONAL ARGUMENTS**

: **Topic resource - The pubsub lite topic to publish to. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TOPIC`**:
ID of the topic or fully qualified identifier for the topic.
To set the `topic` attribute:

- provide the argument `topic` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location of the Pub/Sub Lite resource.
To set the `location` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--attributes**:
Comma-separated list of attributes. Each ATTRIBUTE has the form name="value".
You can specify up to 100 attributes.

**--event-time**:
A user-specified event time. Run `[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)`
for information on time formats.

**--message**:
The body of the message to publish to the given topic name.

**--ordering-key**:
A string key, used for ordering delivery to subscribers. All messages with the
same ordering key will be assigned to the same partition for ordered delivery.

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
gcloud alpha pubsub lite-topics publish
```

```
gcloud beta pubsub lite-topics publish
```