# ivsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# ivs

## Description

**Introduction**

The Amazon Interactive Video Service (IVS) API is REST compatible, using a standard HTTP API and an Amazon Web Services EventBridge event stream for responses. JSON is used for both requests and responses, including errors.

The API is an Amazon Web Services regional service. For a list of supported regions and Amazon IVS HTTPS service endpoints, see the [Amazon IVS page](https://docs.aws.amazon.com/general/latest/gr/ivs.html) in the *Amazon Web Services General Reference* .

- **All API request parameters and URLs are case sensitive.** *

For a summary of notable documentation changes in each release, see [Document History](https://docs.aws.amazon.com/ivs/latest/userguide/doc-history.html) .

**Allowed Header Values**

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/index.html#id1)**Accept:** `` application/json
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/index.html#id3)**Accept-Encoding:** `` gzip, deflate
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/index.html#id5)**Content-Type:** `` application/json

**Key Concepts**

- **Channel** â Stores configuration data related to your live stream. You first create a channel and then use the channelâs stream key to start your live stream.
- **Stream key** â An identifier assigned by Amazon IVS when you create a channel, which is then used to authorize streaming. * **Treat the stream key like a secret, since it allows anyone to stream to the channel.** *
- **Playback key pair** â Video playback may be restricted using playback-authorization tokens, which use public-key encryption. A playback key pair is the public-private pair of keys used to sign and validate the playback-authorization token.
- **Recording configuration** â Stores configuration related to recording a live stream and where to store the recorded content. Multiple channels can reference the same recording configuration.
- **Playback restriction policy** â Restricts playback by countries and/or origin sites.

For more information about your IVS live stream, also see [Getting Started with IVS Low-Latency Streaming](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started.html) .

**Tagging**

A *tag* is a metadata label that you assign to an Amazon Web Services resource. A tag comprises a *key* and a *value* , both set by you. For example, you might set a tag as `topic:nature` to label a particular video category. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging Amazon Web Services Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS has no service-specific constraints beyond what is documented there.

Tags can help you identify and organize your Amazon Web Services resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see [Access Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) ).

The Amazon IVS API has these tag-related operations:  TagResource ,  UntagResource , and  ListTagsForResource . The following resources support tagging: Channels, Stream Keys, Playback Key Pairs, and Recording Configurations.

At most 50 tags can be applied to a resource.

**Authentication versus Authorization**

Note the differences between these concepts:

- *Authentication* is about verifying identity. You need to be authenticated to sign Amazon IVS API requests.
- *Authorization* is about granting permissions. Your IAM roles need to have permissions for Amazon IVS API requests. In addition, authorization is needed to view [Amazon IVS private channels](https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html) . (Private channels are channels that are enabled for âplayback authorization.â)

**Authentication**

All Amazon IVS API requests must be authenticated with a signature. The Amazon Web Services Command-Line Interface (CLI) and Amazon IVS Player SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS API directly, itâs your responsibility to sign the requests.

You generate a signature using valid Amazon Web Services credentials that have permission to perform the requested action. For example, you must sign PutMetadata requests with a signature generated from a user account that has the `ivs:PutMetadata` permission.

For more information:

- Authentication and generating signatures â See [Authenticating Requests (Amazon Web Services Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) in the *Amazon Web Services General Reference* .
- Managing Amazon IVS permissions â See [Identity and Access Management](https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html) on the Security page of the *Amazon IVS User Guide* .

**Amazon Resource Names (ARNs)**

ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see [Amazon Resource Names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference* .

## Available Commands

- [batch-get-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/batch-get-channel.html)
- [batch-get-stream-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/batch-get-stream-key.html)
- [batch-start-viewer-session-revocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/batch-start-viewer-session-revocation.html)
- [create-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-channel.html)
- [create-playback-restriction-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-playback-restriction-policy.html)
- [create-recording-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-recording-configuration.html)
- [create-stream-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-stream-key.html)
- [delete-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-channel.html)
- [delete-playback-key-pair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-playback-key-pair.html)
- [delete-playback-restriction-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-playback-restriction-policy.html)
- [delete-recording-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-recording-configuration.html)
- [delete-stream-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-stream-key.html)
- [get-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-channel.html)
- [get-playback-key-pair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-playback-key-pair.html)
- [get-playback-restriction-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-playback-restriction-policy.html)
- [get-recording-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-recording-configuration.html)
- [get-stream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream.html)
- [get-stream-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream-key.html)
- [get-stream-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream-session.html)
- [import-playback-key-pair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/import-playback-key-pair.html)
- [list-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-channels.html)
- [list-playback-key-pairs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-playback-key-pairs.html)
- [list-playback-restriction-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-playback-restriction-policies.html)
- [list-recording-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-recording-configurations.html)
- [list-stream-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-stream-keys.html)
- [list-stream-sessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-stream-sessions.html)
- [list-streams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-streams.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-tags-for-resource.html)
- [put-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/put-metadata.html)
- [start-viewer-session-revocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/start-viewer-session-revocation.html)
- [stop-stream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/stop-stream.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/untag-resource.html)
- [update-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/update-channel.html)
- [update-playback-restriction-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/update-playback-restriction-policy.html)