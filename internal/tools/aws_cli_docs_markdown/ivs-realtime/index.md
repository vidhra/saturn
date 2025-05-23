# ivs-realtimeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# ivs-realtime

## Description

The Amazon Interactive Video Service (IVS) real-time API is REST compatible, using a standard HTTP API and an AWS EventBridge event stream for responses. JSON is used for both requests and responses, including errors.

**Key Concepts**

- **Stage** â A virtual space where participants can exchange video in real time.
- **Participant token** â A token that authenticates a participant when they join a stage.
- **Participant object** â Represents participants (people) in the stage and contains information about them. When a token is created, it includes a participant ID; when a participant uses that token to join a stage, the participant is associated with that participant ID. There is a 1:1 mapping between participant tokens and participants.

For server-side composition:

- **Composition process** â Composites participants of a stage into a single video and forwards it to a set of outputs (e.g., IVS channels). Composition operations support this process.
- **Composition** â Controls the look of the outputs, including how participants are positioned in the video.

For more information about your IVS live stream, also see [Getting Started with Amazon IVS Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started.html) .

**Tagging**

A *tag* is a metadata label that you assign to an AWS resource. A tag comprises a *key* and a *value* , both set by you. For example, you might set a tag as `topic:nature` to label a particular video category. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS stages has no service-specific constraints beyond what is documented there.

Tags can help you identify and organize your AWS resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see [Access Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) ).

The Amazon IVS real-time API has these tag-related operations:  TagResource ,  UntagResource , and  ListTagsForResource . The following resource supports tagging: Stage.

At most 50 tags can be applied to a resource.

## Available Commands

- [create-encoder-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-encoder-configuration.html)
- [create-ingest-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-ingest-configuration.html)
- [create-participant-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-participant-token.html)
- [create-stage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-stage.html)
- [create-storage-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-storage-configuration.html)
- [delete-encoder-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-encoder-configuration.html)
- [delete-ingest-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-ingest-configuration.html)
- [delete-public-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-public-key.html)
- [delete-stage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-stage.html)
- [delete-storage-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-storage-configuration.html)
- [disconnect-participant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/disconnect-participant.html)
- [get-composition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-composition.html)
- [get-encoder-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-encoder-configuration.html)
- [get-ingest-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-ingest-configuration.html)
- [get-participant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-participant.html)
- [get-public-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-public-key.html)
- [get-stage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-stage.html)
- [get-stage-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-stage-session.html)
- [get-storage-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-storage-configuration.html)
- [import-public-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/import-public-key.html)
- [list-compositions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-compositions.html)
- [list-encoder-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-encoder-configurations.html)
- [list-ingest-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-ingest-configurations.html)
- [list-participant-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-participant-events.html)
- [list-participants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-participants.html)
- [list-public-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-public-keys.html)
- [list-stage-sessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-stage-sessions.html)
- [list-stages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-stages.html)
- [list-storage-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-storage-configurations.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-tags-for-resource.html)
- [start-composition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/start-composition.html)
- [stop-composition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/stop-composition.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/untag-resource.html)
- [update-ingest-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/update-ingest-configuration.html)
- [update-stage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/update-stage.html)